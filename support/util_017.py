"""Support helpers for util_017."""


def helper_17_a(value):
    return str(value).upper()


def helper_17_b(items):
    return [item for item in items if item]


def helper_17_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
