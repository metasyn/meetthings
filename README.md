# meetthings

meetthings is a tool for centralizing meeting planning and organization for [noisebridge](noisebridge.net)

# repo organization

The directory `schema` holds json files which describe data requirements. Right now only `meetthings.json` is important.

The model is:

`form_name: { field name : {'type': field type, 'validators': validator, ...}}}`

A dictionary of the forms is passed to the rendered, and used by the templates.

# setup

First, make sure you've installed all the dependencies:

```bash
make setup install
```

After that, update `instance/meetup-test-api.cfg` with your `MEETUP_API_SECRET` if necessary.

Then:

```bash
make server
```

which will lauch a wsgi on port 5000. you can go to `localhost:5000/NewEvent` to see if everything went well.

# development

You can format, lint, and typecheck your code with the make targets:

```
make format lint typecheck
```

which uses [black](https://github.com/python/black), [flake8](http://flake8.pycqa.org/en/latest/), and [mypy](https://mypy.readthedocs.io/en/latest/) respectively.

# testing

Run:

```
make tests
```

to run the unit tests.