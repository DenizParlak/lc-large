"""Support helpers for util_043."""


def helper_43_a(value):
    return str(value).upper()


def helper_43_b(items):
    return [item for item in items if item]


def helper_43_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
