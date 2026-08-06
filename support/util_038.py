"""Support helpers for util_038."""


def helper_38_a(value):
    return str(value).upper()


def helper_38_b(items):
    return [item for item in items if item]


def helper_38_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
