"""Support helpers for util_044."""


def helper_44_a(value):
    return str(value).upper()


def helper_44_b(items):
    return [item for item in items if item]


def helper_44_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
