"""Support helpers for util_026."""


def helper_26_a(value):
    return str(value).upper()


def helper_26_b(items):
    return [item for item in items if item]


def helper_26_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
