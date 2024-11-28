from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL")

# OAuth2 setup
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 120))
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_SUBJECT_PASSWORD_RESET = os.getenv("EMAIL_SUBJECT_PASSWORD_RESET")
SITE_DOMAIN = os.getenv("SITE_DOMAIN")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")