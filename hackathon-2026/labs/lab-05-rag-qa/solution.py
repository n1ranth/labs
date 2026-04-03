def retrieve(chunks: list[str], question: str) -> str:
    """
    Retrieve the most relevant chunk using simple word overlap.

    Args:
        chunks:   List of text strings (the knowledge base).
        question: The user's question.

    Returns:
        The single chunk string with the highest word overlap score.
    """
    if not chunks:
        return "No relevant context found."
    
    # Tokenize question (split on spaces, lowercase)
    question_words = set(word.lower() for word in question.split() if word.strip())
    
    if not question_words:
        return chunks[0]  # Return first chunk if no question words
    
    # For each chunk, count how many question words appear in it
    best_chunk = chunks[0]
    best_score = 0
    
    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for word in question_words if word in chunk_lower)
        
        if score > best_score:
            best_score = score
            best_chunk = chunk
    
    return best_chunk


def answer(chunks: list[str], question: str) -> dict:
    """
    Retrieve the best context and build a simple answer.

    Args:
        chunks:   The knowledge base.
        question: The user's question.

    Returns:
        A dict with keys: 'context' (str) and 'answer' (str).
        'answer' must be a non-empty string.
    """
    # Call retrieve() to get the best chunk
    context = retrieve(chunks, question)
    
    # Return a simple answer based on the context
    if context == "No relevant context found.":
        answer_text = "I don't have enough information to answer that question."
    else:
        answer_text = "Based on the provided context, here's what I can tell you."
    
    return {
        "context": context,
        "answer": answer_text
    }
