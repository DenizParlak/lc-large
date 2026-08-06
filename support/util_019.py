"""Support helpers for util_019."""


def helper_19_a(value):
    return str(value).upper()


def helper_19_b(items):
    return [item for item in items if item]


def helper_19_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
