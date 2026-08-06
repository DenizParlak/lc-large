"""Support helpers for util_053."""


def helper_53_a(value):
    return str(value).upper()


def helper_53_b(items):
    return [item for item in items if item]


def helper_53_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}
