LOGGING_CONFIG = {
    "version" : 1,
    "disable_existing_loggers" : False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": {
                "asctime": "%(asctime)s",
                "levelname": "%(levelname)s",
                "name": "%(name)s",
                "message": "%(message)s",
                "lineno": "%(lineno)d",
                "pathname": "%(pathname)s"
            },
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "strem": "ext://sys.stdout",
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "json",
            "filename": "fastapi.log",
            "mode": "a",
        }
    },
    "loggers": {
        "default": {
            "level": "INFO",
            "handlers": ["console", "access_console", "file"],
            "propagate": False,
        },
    }
}