"""Support helpers for util_006."""


def helper_6_a(value):
    return str(value).upper()


def helper_6_b(items):
    return [item for item in items if item]


def helper_6_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
