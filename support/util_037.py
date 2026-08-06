"""Support helpers for util_037."""


def helper_37_a(value):
    return str(value).upper()


def helper_37_b(items):
    return [item for item in items if item]


def helper_37_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
