import argparse
import faker
import importlib
import inspect
import pkgutil
from faker import Faker
from types import FunctionType
from typing import Any
from typing import Callable


class _Abort(Exception):
    ...


def _list_providers() -> list[type[faker.providers.BaseProvider]]:
    """
    Find the list of provider classes within the :mod:`faker` library.
    """
    faker_module = importlib.import_module('faker')
    providers = []

    for module_info in pkgutil.iter_modules(
        faker_module.providers.__path__, 'faker.providers.'
    ):
        module = importlib.import_module(module_info.name)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(cls, faker.providers.BaseProvider)
                and cls != faker.providers.BaseProvider
            ):
                providers.append(cls)

    return sorted(providers, key=lambda x: x.__module__)


def _list_provider_funcs(
    provider: type[faker.providers.BaseProvider],
) -> list[Callable[..., Any]]:
    funcs = [
        member
        for name, member in inspect.getmembers(provider)
        if inspect.isfunction(member)
        and member.__qualname__.startswith(provider.__name__ + '.')
        and not name.startswith('_')
    ]
    return sorted(funcs, key=lambda x: x.__name__)


def _handle_list_providers() -> None:
    print('Faker providers:')
    for provider in _list_providers():
        print(f'  {provider.__module__}')


def _handle_show_provider_help(
    provider_name: str,
) -> None:
    provider = next(
        (
            provider
            for provider in _list_providers()
            if provider.__module__.split('.')[-1] == provider_name
        ),
        None,
    )
    if not provider:
        raise _Abort(f'No Faker provider named {provider_name!r}')
    help(provider)


def _handle_show_func_help(
    func_name: str,
) -> None:
    try:
        func = getattr(Faker(), func_name)
    except AttributeError as error:
        raise _Abort(f'No Faker function named {func_name!r}') from error
    help(func)


def _handle_find_func(
    partial_func_name: str,
) -> None:
    print(f'Faker functions containing {partial_func_name!r}:')
    for func_name in sorted(dir(Faker())):
        if partial_func_name in func_name:
            print(f'  {func_name}')


def _handle_list_funcs(
    provider_name: str | None = None,
) -> None:
    providers = _list_providers()

    if provider_name:
        matching_providers = [
            provider
            for provider in providers
            if provider.__module__.split('.')[-1] == provider_name
        ]

        if not matching_providers:
            raise _Abort(f'No Faker provider named {provider_name!r}')

        for provider in matching_providers:
            print(f'{provider.__module__}:')
            for func in _list_provider_funcs(provider):
                print(f'  {func.__name__}')

    else:
        for provider in providers:
            print(f'{provider.__module__}:')
            for func in _list_provider_funcs(provider):
                print(f'  {func.__name__}')


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Help on faker module.')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('providers', help='show list of providers')
    parser_provider = subparsers.add_parser('provider', help='show help for a provider')
    parser_provider.add_argument('provider', help='provider name')

    parser_func = subparsers.add_parser('func', help='show help for a function')
    parser_func.add_argument('func', help='function name')

    parser_find = subparsers.add_parser('find', help='find a function by partial name')
    parser_find.add_argument('partial_func', help='partial function name')

    parser_ls = subparsers.add_parser(
        'ls', help='list faker functions - optionally by provider'
    )
    parser_ls.add_argument('provider', nargs='?', help='provider name')

    return parser


def main() -> None:
    parser = _get_parser()
    args = parser.parse_args()
    try:
        if args.command == 'providers':
            _handle_list_providers()
        elif args.command == 'provider':
            _handle_show_provider_help(args.provider)
        elif args.command == 'func':
            _handle_show_func_help(args.func)
        elif args.command == 'find':
            _handle_find_func(args.partial_func)
        elif args.command == 'ls':
            _handle_list_funcs(args.provider)
        else:
            parser.print_help()
    except _Abort as abort:
        print(str(abort))
