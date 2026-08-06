"""Support helpers for util_046."""


def helper_46_a(value):
    return str(value).upper()


def helper_46_b(items):
    return [item for item in items if item]


def helper_46_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
