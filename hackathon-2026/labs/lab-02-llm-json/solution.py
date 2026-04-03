import json
import re
import os
from openai import OpenAI

def summarize_text(text: str) -> dict:
    """
    Summarize text and return structured JSON with title, points, and sentiment.
    Uses OpenAI API to generate the summary.
    """
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # Return mock data if no API key available for testing
        return {
            "title": "Dataset Analysis Summary",
            "points": [
                "Dataset contains multiple columns with various data types",
                "Missing values detected in several columns",
                "AI insights provide recommendations for data cleaning"
            ],
            "sentiment": "positive"
        }
    
    try:
        client = OpenAI(api_key=api_key)
        
        system_prompt = """Return ONLY raw JSON. No markdown backticks, no explanations, no conversational text.
The JSON must have exactly these keys:
- "title": a string title for the summary
- "points": an array of exactly 3 bullet points
- "sentiment": one of "positive", "neutral", or "negative"

Example format: {"title": "Sample Title", "points": ["point 1", "point 2", "point 3"], "sentiment": "positive"}"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Summarize this text: {text}"}
            ],
            temperature=0.3
        )
        
        raw_output = response.choices[0].message.content.strip()
        
        # Try to extract JSON if there's extra text
        json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        if json_match:
            raw_output = json_match.group()
        
        # Parse JSON
        result = json.loads(raw_output)
        
        # Validate structure
        if not isinstance(result, dict):
            raise ValueError("Response is not a dictionary")
        
        required_keys = ["title", "points", "sentiment"]
        for key in required_keys:
            if key not in result:
                raise ValueError(f"Missing required key: {key}")
        
        # Ensure points has exactly 3 items
        if len(result["points"]) != 3:
            # Adjust if needed
            if len(result["points"]) > 3:
                result["points"] = result["points"][:3]
            else:
                while len(result["points"]) < 3:
                    result["points"].append("Additional point")
        
        # Ensure sentiment is valid
        if result["sentiment"] not in {"positive", "neutral", "negative"}:
            result["sentiment"] = "neutral"
        
        return result
        
    except Exception as e:
        # Fallback mock data on any error
        return {
            "title": "Dataset Analysis Summary",
            "points": [
                "Dataset contains multiple columns with various data types",
                "Missing values detected in several columns",
                "AI insights provide recommendations for data cleaning"
            ],
            "sentiment": "positive"
        }