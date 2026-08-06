"""Support helpers for util_055."""


def helper_55_a(value):
    return str(value).upper()


def helper_55_b(items):
    return [item for item in items if item]


def helper_55_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
