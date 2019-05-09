from flask import Flask

app = Flask(__name__, instance_relative_config=True)

try:
    app.config.from_envvar("APPLICATION_SETTINGS")
except RuntimeError as err:
    print("could not load app configuration")
    print(err)

# this is required to make the routes work
from . import routes # noqa
