"""Support helpers for util_021."""


def helper_21_a(value):
    return str(value).upper()


def helper_21_b(items):
    return [item for item in items if item]


def helper_21_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
