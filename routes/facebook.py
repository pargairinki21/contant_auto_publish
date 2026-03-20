# routes/facebook.py - All Facebook routes go here

from fastapi import APIRouter
from pydantic import BaseModel
from services.facebook import post_image

router = APIRouter(
    prefix="/facebook",
    tags=["Facebook"]
)

# Request body
class ImagePost(BaseModel):
    image_url: str
    caption: str = "Posted via Facebook API!"

@router.post("/post-image")
def post_image_route(data: ImagePost):
    """
    POST /facebook/post-image
    Automatically posts image to Facebook Page
    """
    result = post_image(data.image_url, data.caption)

    if "id" in result:
        return {
            "success": True,
            "message": "✅ Image posted to Facebook!",
            "post_id": result["id"]
        }
    else:
        return {
            "success": False,
            "message": "❌ Failed to post",
            "error": result.get("error", {}).get("message", "Unknown error")
        }