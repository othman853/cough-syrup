from app import factory


if __name__ == '__main__':

    try:
        app = factory('etc.config.DevelopmentConfig')
        app.run()
    except Exception as error:
        print(str(error))
