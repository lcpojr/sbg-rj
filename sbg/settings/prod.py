from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = "/site/staticfiles/"
MEDIA_ROOT = "/site/mediafiles/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {"format": "%(levelname)s %(asctime)s %(message)s"},
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "()": "logging.Formatter",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "server_file": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": BASE_DIR + "/logs/server.log",
        },
        "request_file": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": BASE_DIR + "/logs/request.log",
        },
        "template_file": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": BASE_DIR + "/logs/template.log",
        },
        "gunicorn_file": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": BASE_DIR + "/logs/gunicorn.log",
        },
    },
    "loggers": {
        "django.server": {
            "handlers": ["server_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["request_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["template_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "gunicorn.errors": {
            "handlers": ["gunicorn_file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
