"""Support helpers for util_010."""


def helper_10_a(value):
    return str(value).upper()


def helper_10_b(items):
    return [item for item in items if item]


def helper_10_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
