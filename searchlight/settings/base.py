from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['*']
