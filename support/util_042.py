"""Support helpers for util_042."""


def helper_42_a(value):
    return str(value).upper()


def helper_42_b(items):
    return [item for item in items if item]


def helper_42_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
