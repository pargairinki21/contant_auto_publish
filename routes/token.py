# routes/token.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.token import get_long_lived_token

router = APIRouter(
    prefix="/token",
    tags=["Token"]
)

class TokenRequest(BaseModel):
    short_lived_token: str

@router.post("/get-long-lived-token")
def generate_long_lived_token(data: TokenRequest):
    """
    POST /token/get-long-lived-token
    Pass your short lived token → get back long lived token (60 days)
    
    How to get short lived token:
    1. Go to developers.facebook.com/tools/explorer
    2. Select MyTestApp
    3. Select TechPost Studio
    4. Click Generate Access Token
    5. Copy and paste here
    """
    try:
        long_lived_token = get_long_lived_token(data.short_lived_token)
        return {
            "success": True,
            "message": "✅ Long lived token generated! Valid for 60 days.",
            "long_lived_token": long_lived_token,
            "expires_in": "60 days",
            "next_step": "Copy this token and paste in config.py as LONG_LIVED_TOKEN"
        }
    except Exception as e:
        return {
            "success": False,
            "message": "❌ Failed to generate token",
            "error": str(e)
        }