"""
Lab 06: Healthcare Agents - Solution Template
"""

def is_anomaly(vitals: dict) -> bool:
    """
    Returns True if any vital sign is outside the normal range.
    
    Thresholds:
    - Heart Rate: [60, 100]
    - BP Systolic: [90, 140]
    - BP Diastolic: [60, 90]
    - Oxygen Saturation: [95, 100]
    """
    # Heart Rate check
    hr = vitals.get("heart_rate")
    if hr is not None and (hr < 60 or hr > 100):
        return True
    
    # Blood Pressure Systolic check
    bp_sys = vitals.get("blood_pressure_sys")
    if bp_sys is not None and (bp_sys < 90 or bp_sys > 140):
        return True
    
    # Blood Pressure Diastolic check
    bp_dia = vitals.get("blood_pressure_dia")
    if bp_dia is not None and (bp_dia < 60 or bp_dia > 90):
        return True
    
    # Oxygen Saturation check
    o2 = vitals.get("oxygen_saturation")
    if o2 is not None and o2 < 95:
        return True
    
    return False

def recommend_intervention(vitals: dict, history: list = None) -> str:
    """
    Suggests an intervention based on the anomaly status.
    """
    if is_anomaly(vitals):
        return "Immediate Physician Review"
    return "Continue Observation"
