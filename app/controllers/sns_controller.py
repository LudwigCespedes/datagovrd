from fastapi import APIRouter

from app.services.sns_service import GeneralService, StatsService
from app.utils.data import institutions_dict

sns_info = institutions_dict["sns"]

router = APIRouter()

@router.get("/")
def get_general():
    return {
        "name": sns_info["name"],
        "abbreviation": sns_info["name"],
        "description": GeneralService.get_about(),
        "services": sns_info["services"]
    }

@router.get("/stats/info")
def get_stats_info():
    return {
        "title": StatsService.get_title(),
        "available_years": StatsService.get_available_years()
    }