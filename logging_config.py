from pythonjsonlogger import jsonlogger
from utilits.json_file_handler import JsonFilehandler
from opentelemetry import trace

span = trace.get_current_span()
context = span.get_span_context() if span else {}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
            "console":{
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s | %(asctime)s | %(name)s | %(module)s | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": True,
            },
            "json":{
                "()": "utilits.logger_json_formatter.LoggerJsonFormater",
                "format": """
                    timestamp: %(asctime)s
                    level: %(levelname)s
                    service: doc-comparator-service
                    trace_id: %(trace_id)s
                    span_id: %(span_id)s
                    user_id: %(user_id)s
                    message: %(message)s
                    duration_ms: %(duration_ms)s
                    context: %(context)s
                """,
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "json_ensure_ascii": False,
                "style": "%"
            }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "app": {
            "handlers": ["json"],
            "level": "INFO",
            "propagate": False
        }
    }
}