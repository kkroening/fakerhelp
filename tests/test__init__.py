import faker
import fakerhelp


def test_list_providers():
    providers = fakerhelp._list_providers()
    assert all(isinstance(x, type) for x in providers)
    assert faker.providers.internet.Provider in providers


# TODO: do additional overkill testing
