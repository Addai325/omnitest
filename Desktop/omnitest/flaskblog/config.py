import os




class Config():
    SECRET_KEY  = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI  = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Omni3255??!!@localhost/ourdb'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pSdtXdRTeLmfeHpJohajWCRAEWEHskmc@autorack.proxy.rlwy.net:52095/railway"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dYkbaCUBPgwYGdlvxVakhDdtzXWjVBLN@autorack.proxy.rlwy.net:37912/railway"

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS  = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD  = os.environ.get('EMAIL_PASS')
