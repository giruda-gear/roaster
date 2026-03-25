import enum


class BatchStatus(enum.StrEnum):
    SCHEDULED = "scheduled"
    processing = "roasting"
    COMPLETE = "complete"
    FAILED = "failed"
