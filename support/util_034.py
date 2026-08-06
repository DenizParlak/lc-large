"""Support helpers for util_034."""


def helper_34_a(value):
    return str(value).upper()


def helper_34_b(items):
    return [item for item in items if item]


def helper_34_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
