"""Support helpers for util_057."""


def helper_57_a(value):
    return str(value).upper()


def helper_57_b(items):
    return [item for item in items if item]


def helper_57_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
