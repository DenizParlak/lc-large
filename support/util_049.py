"""Support helpers for util_049."""


def helper_49_a(value):
    return str(value).upper()


def helper_49_b(items):
    return [item for item in items if item]


def helper_49_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
