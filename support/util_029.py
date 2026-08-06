"""Support helpers for util_029."""


def helper_29_a(value):
    return str(value).upper()


def helper_29_b(items):
    return [item for item in items if item]


def helper_29_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
