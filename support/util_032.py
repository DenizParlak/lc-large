"""Support helpers for util_032."""


def helper_32_a(value):
    return str(value).upper()


def helper_32_b(items):
    return [item for item in items if item]


def helper_32_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
