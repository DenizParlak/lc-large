"""Support helpers for util_056."""


def helper_56_a(value):
    return str(value).upper()


def helper_56_b(items):
    return [item for item in items if item]


def helper_56_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
