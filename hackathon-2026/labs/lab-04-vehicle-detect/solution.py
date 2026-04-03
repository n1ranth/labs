from typing import Optional


def count_by_class(detections):
    """
    Count detections grouped by class name.

    Args:
        detections: List of detection dicts with 'class_name' key.

    Returns:
        A dict like {"car": 3, "truck": 1}
    """
    counts = {}
    for detection in detections:
        class_name = detection.get('class_name')
        if class_name:
            counts[class_name] = counts.get(class_name, 0) + 1
    return counts


def filter_by_confidence(detections, threshold):
    """
    Return only detections where confidence > threshold.

    Args:
        detections: List of detection dicts with 'confidence' key.
        threshold:  Minimum confidence value (e.g., 0.75).

    Returns:
        Filtered list of detection dicts.
    """
    return [d for d in detections if d.get('confidence', 0) > threshold]


def get_top_detection(detections):
    """
    Return the detection with the highest confidence score.

    Args:
        detections: List of detection dicts.

    Returns:
        Single dict with highest confidence, or None if list is empty.
    """
    if not detections:
        return None
    
    return max(detections, key=lambda d: d.get('confidence', 0))

