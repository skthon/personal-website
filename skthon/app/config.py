class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@postgres:5432/skthon'
    JWT_SECRET_KEY = 'hello'

class Production(object):
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@postgres:5432/skthon'
    JWT_SECRET_KEY = "hello"

app_config = {
    'development': Development,
    'production': Production,
}