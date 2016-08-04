import os


TEST_BROWSER = os.environ.get('TEST_BROWSER', 'chrome')


def from_env(env_var):
    value = os.environ.get(env_var)

    if value is None:
        raise Exception(
            '[CONFIG ERROR]: {} environment variable is either'
            ' invalid or not set'
            .format(env_var)
        )

    return value


class DefaultConfig():
    TESTING = False
    SQLALCHEMY_DATABASE_URI = from_env('SYRUP_DATABASE_URL')


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestConfig(DefaultConfig):
    TESTING = True
    SERVER_NAME = ''
