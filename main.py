from app import factory


if __name__ == '__main__':
    app = factory('etc.config.DevelopmentConfig')
    app.run()
