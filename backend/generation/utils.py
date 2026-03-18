def enum_labels(enum_value: str) -> str:
    return ' '.join(part.capitalize() for part in enum_value.lower().split('_'))