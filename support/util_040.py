"""Support helpers for util_040."""


def helper_40_a(value):
    return str(value).upper()


def helper_40_b(items):
    return [item for item in items if item]


def helper_40_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
