LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
            "console":{
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(asctime)s | %(levelprefix)s | %(name)s | %(module)s | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": True,
            },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        }
    }
}