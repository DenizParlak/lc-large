"""Support helpers for util_031."""


def helper_31_a(value):
    return str(value).upper()


def helper_31_b(items):
    return [item for item in items if item]


def helper_31_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
