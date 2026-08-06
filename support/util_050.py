"""Support helpers for util_050."""


def helper_50_a(value):
    return str(value).upper()


def helper_50_b(items):
    return [item for item in items if item]


def helper_50_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
