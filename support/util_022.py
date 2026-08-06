"""Support helpers for util_022."""


def helper_22_a(value):
    return str(value).upper()


def helper_22_b(items):
    return [item for item in items if item]


def helper_22_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
