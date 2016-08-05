from app import factory
import os

if __name__ == '__main__':

    try:
        app = factory(os.env.get('SYRUP_CONFIG', 'DevelopmentConfig'))
        app.run()
    except Exception as error:
        print(str(error))
