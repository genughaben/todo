import os

BASE_PATH = os.path.abspath(".")

# print(BASE_PATH)
# print(f'{os.listdir(BASE_PATH)}')

FLASK_SERVER_NAME = 'locahost:7001'
# FLASK_DEBUG = True # change before deployment
FLASK_THREADED = True

RESTPLUS_SWAGGER_EXPANSION = 'list'
RESTPLUS_VAL = True
RESTPLUS_MASK_SWAGGER = False

# SQLALCHEMY_DATABASE_URI = f'sqlite:////{BASE_PATH}/server/database/test.db'
SQLALCHEMY_TRACK_MODS = False

# INVOICE_FILES_FOLDER = f"{BASE_PATH}/server/invoice_files/invoices"
# WORK_REPORT_FILES_FOLDER = f"{BASE_PATH}/server/invoice_files/reports"