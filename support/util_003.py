"""Support helpers for util_003."""


def helper_3_a(value):
    return str(value).upper()


def helper_3_b(items):
    return [item for item in items if item]


def helper_3_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
