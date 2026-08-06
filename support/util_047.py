"""Support helpers for util_047."""


def helper_47_a(value):
    return str(value).upper()


def helper_47_b(items):
    return [item for item in items if item]


def helper_47_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
