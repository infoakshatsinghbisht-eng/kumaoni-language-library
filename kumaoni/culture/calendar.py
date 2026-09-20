"""
Kumaoni solar calendar and seasonal calculations.
"""

from typing import Dict, List, Optional
from kumaoni.constants import KUMAONI_MONTHS, SEASONS, DAYS_OF_WEEK


def get_months() -> List[Dict]:
    """Returns the twelve months of the Kumaoni solar calendar."""
    return list(KUMAONI_MONTHS)


def get_seasons() -> Dict[str, Dict]:
    """Returns the traditional Himalayan seasonal divisions."""
    return dict(SEASONS)


def get_days_of_week() -> List[Dict]:
    """Returns days of the week in Kumaoni."""
    return list(DAYS_OF_WEEK)


def get_current_season(month_name: str) -> Optional[Dict]:
    """Find the traditional season associated with a Kumaoni month."""
    for s_key, s_info in SEASONS.items():
        if month_name in s_info["months"]:
            return s_info
    return None
