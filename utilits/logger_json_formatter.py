from pythonjsonlogger import json
from opentelemetry import trace
from pythonjsonlogger.core import LogRecord


class LoggerJsonFormater(json.JsonFormatter):
    def process_log_record(self, log_record: LogRecord) -> LogRecord:
        span = trace.get_current_span()
        if span:
            log_record["trace_id"] = format(span.get_span_context().trace_id, "032x")
            log_record["span_id"] = format(span.get_span_context().span_id, "016x")

        log_record.setdefault("user_id", "default_user_id")
        log_record.setdefault("duration_ms", None)
        log_record.setdefault("context", {})

        return super().process_log_record(log_record)