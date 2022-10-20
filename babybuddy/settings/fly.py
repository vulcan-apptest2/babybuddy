import dj_database_url

from .base import *

# Default to not allow uploads.
# Fly.io has no persistent storage by default.

BABY_BUDDY["ALLOW_UPLOADS"] = bool(
    strtobool(os.environ.get("ALLOW_UPLOADS") or "False")
)


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(conn_max_age=500)}
