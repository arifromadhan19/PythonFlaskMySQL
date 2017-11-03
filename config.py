# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

WTF_CSRF_ENABLED = False

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# DB CONFIG
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345619@127.0.0.1/db_product"
SQLALCHEMY_TRACK_MODIFICATIONS = True