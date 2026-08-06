"""Support helpers for util_027."""


def helper_27_a(value):
    return str(value).upper()


def helper_27_b(items):
    return [item for item in items if item]


def helper_27_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
