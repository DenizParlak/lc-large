"""Support helpers for util_035."""


def helper_35_a(value):
    return str(value).upper()


def helper_35_b(items):
    return [item for item in items if item]


def helper_35_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
