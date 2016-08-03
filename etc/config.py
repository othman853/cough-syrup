import os


TEST_BROWSER = os.environ.get('TEST_BROWSER', 'chrome')

class DefaultConfig():
    TESTING = False

class DevelopmentConfig(DefaultConfig):
    DEBUG = True

class TestConfig(DefaultConfig):
    TESTING = True
    SERVER_NAME = ''
