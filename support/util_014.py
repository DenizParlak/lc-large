"""Support helpers for util_014."""


def helper_14_a(value):
    return str(value).upper()


def helper_14_b(items):
    return [item for item in items if item]


def helper_14_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
