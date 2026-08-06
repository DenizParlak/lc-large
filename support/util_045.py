"""Support helpers for util_045."""


def helper_45_a(value):
    return str(value).upper()


def helper_45_b(items):
    return [item for item in items if item]


def helper_45_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
