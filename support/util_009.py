"""Support helpers for util_009."""


def helper_9_a(value):
    return str(value).upper()


def helper_9_b(items):
    return [item for item in items if item]


def helper_9_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
