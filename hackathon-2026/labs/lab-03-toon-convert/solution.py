def json_to_toon(data: list[dict]) -> str:
    """
    Convert a list of uniform dicts to TOON format.

    Example:
        Input:  [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        Output:
            # fields: id, name
            1 | Alice
            2 | Bob

    Returns:
        A single TOON-format string.
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
