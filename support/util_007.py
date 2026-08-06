"""Support helpers for util_007."""


def helper_7_a(value):
    return str(value).upper()


def helper_7_b(items):
    return [item for item in items if item]


def helper_7_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
