def json_to_toon(data: list[dict]) -> str:
    """
    Convert dataset analysis or suggestions data to TOON format for token efficiency.

    Example for dataset analysis:
        Input:  [{"column": "age", "missing_percent": 12.5, "dtype": "int64"}]
        Output:
            # fields: column, missing_percent, dtype
            age | 12.5 | int64

    Example for suggestions:
        Input:  [{"column": "age", "suggestion": "Fill with median (25)", "confidence": "high"}]
        Output:
            # fields: column, suggestion, confidence
            age | Fill with median (25) | high

    Returns:
        A single TOON-format string optimized for LLM consumption.
    """
    if not data:
        return ""
    
    # Extract field names from the first dict
    field_names = list(data[0].keys())
    
    # Build the header line
    header = f"# fields: {', '.join(field_names)}"
    
    # Build each data row
    rows = []
    for item in data:
        values = [str(item.get(field, "")) for field in field_names]
        row = " | ".join(values)
        rows.append(row)
    
    # Join all lines
    return header + "\n" + "\n".join(rows)


def count_tokens(text: str) -> int:
    """
    A simple proxy for token count: split on whitespace and count words.
    
    Args:
        text: Any string.

    Returns:
        Integer word count.
    """
    if not text:
        return 0
    
    # Split on whitespace and count non-empty tokens
    tokens = text.split()
    return len(tokens)
