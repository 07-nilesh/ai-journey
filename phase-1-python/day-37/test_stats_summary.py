import pytest
from typing import List, Dict
import statistics

# --- THIS IS THE ONE FUNCTION WE ARE TESTING ---
def stats_summary(numbers: List[float]) -> Dict[str, float]:
    if not numbers:
        raise ValueError("List cannot be empty")
    
    return {
        "mean": statistics.mean(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

# --- THESE 5 TESTS CHECK THAT ONE FUNCTION ---

def test_stats_normal_list():
    # We pass a normal list INTO stats_summary
    result = stats_summary([10, 20, 30, 40, 50])
    assert result["mean"] == 30.0
    assert result["max"] == 50
    assert result["min"] == 10

def test_stats_negative_numbers():
    # We pass negative numbers INTO stats_summary
    result = stats_summary([-10, -5, -20])
    assert result["max"] == -5
    assert result["min"] == -20

def test_stats_single_element():
    # We pass just one number INTO stats_summary
    result = stats_summary([42])
    assert result["mean"] == 42.0

def test_stats_floats():
    # We pass decimals INTO stats_summary
    result = stats_summary([1.5, 2.5, 3.5])
    assert result["mean"] == 2.5

def test_stats_empty_list():
    # We pass an empty list, and EXPECT it to crash with a ValueError
    with pytest.raises(ValueError):
        stats_summary([])