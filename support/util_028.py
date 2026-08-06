"""Support helpers for util_028."""


def helper_28_a(value):
    return str(value).upper()


def helper_28_b(items):
    return [item for item in items if item]


def helper_28_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
