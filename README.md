# fakerhelp - The Overkill CLI Help Tool for the Faker Library

Let's be real - we've all been there. You're coding away, merrily using the `faker` library to populate your system with mock data, when suddenly...you hit a roadblock.

You find yourself asking, "What on earth does this specific provider in the `faker` library do?" or "How do I use this particular function?".

Naturally, you could go ahead and check out the official `faker` documentation. We're sure it's a fine source of wisdom. But why settle for the fine when you can have the _ridiculously fine_?

Welcome to `fakerhelp` - the grossly over-engineered, laughably overkill CLI help tool you never asked for, but we built anyway.

## Why fakerhelp?

Why not? Isn't everything better when you can access it from the terminal? If we can't do it in the terminal, do we even want to do it at all?

`fakerhelp` exists for no reason other than to provide you with a shiny, new, and completely unnecessary way to view help on the `faker` module. We promise, it's at least 78% as good as reading the official documentation, and 100% more likely to give you that delightful, command line-infused adrenaline rush.

And let's be honest, who needs web browser tabs when you can type away in the terminal, feel like a real hacker, and occasionally make cool `faker` discoveries?

## Usage

`fakerhelp` has several commands, all designed to enhance your faker knowledge. Simply run `fakerhelp --help` (yo dawg) for a quick overview of everything you can do. For a more detailed, command-by-command introduction, read on!

### Providers

Want to know what providers `faker` has in store for you? It's as easy as pie with `fakerhelp`. Just run:

```
$ fakerhelp providers
Providers:
  faker.providers.address
  faker.providers.automotive
  faker.providers.bank
  faker.providers.barcode
  faker.providers.color
  ...
```

### Provider Help

Curious about a particular provider? `fakerhelp` has got you covered:

```
$ fakerhelp provider internet
Help on class Provider in module faker.providers.internet:

class Provider(faker.providers.BaseProvider)
 |  ...
 |
 |  ascii_company_email(self) -> str
 |
 |  ascii_email(self) -> str
 |
 |  ascii_free_email(self) -> str
 |
 |  ascii_safe_email(self) -> str
 |
 |  company_email(self) -> str
 |
 |  dga(self, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None, tld: Optional[str] = None, length: Optional[int] = None) -> str
 |      Generates a domain name by given date
 |      https://en.wikipedia.org/wiki/Domain_generation_algorithm
 |
 |      :type year: int
 |      :type month: int
 |      :type day: int
 |      :type tld: str
 |      :type length: int
 |      :rtype: str
 ...
```

### Function Help
Ever wondered what a specific `faker` function does? `fakerhelp` is here to enlighten you:

```
$ fakerhelp func enum
Help on method enum in module faker.providers.python:

enum(enum_cls: Type[~TEnum]) -> ~TEnum method of faker.providers.python.Provider instance
    Returns a random enum of the provided input `Enum` type.

    :param enum_cls: The `Enum` type to produce the value for.
    :returns: A randomly selected enum value.
  ...
```

### Find Function

Need help finding a function? Give `fakerhelp` a whirl:

```
$ fakerhelp find date
Faker functions containing 'date':
  date
  date_between
  date_between_dates
  date_object
  date_of_birth
  date_this_century
  date_this_decade
  date_this_month
  date_this_year
  date_time
  date_time_ad
  date_time_between
  date_time_between_dates
  date_time_this_century
  date_time_this_decade
  date_time_this_month
  date_time_this_year
  future_date
  future_datetime
  passport_dates
  past_date
  past_datetime
```

### List Functions

Do you have an unquenchable thirst to know about all the functions in a provider? Say no more:

```
$ fakerhelp ls address
faker.providers.address:
  address
  building_number
  city
  city_suffix
  country
  country_code
  current_country
  current_country_code
  postcode
  street_address
  street_name
  street_suffix
```

So there you have it. `fakerhelp`, your overly complicated companion for the `faker` library. Because let's be real - the more terminal tools we have, the more hacker we feel. Happy faking!

Disclaimer: No documentation was harmed during the making of this tool. The `faker` docs are awesome, but we simply couldn't resist the allure of building a shiny new command line toy. Please use responsibly, and remember to hydrate between hacking sessions.
