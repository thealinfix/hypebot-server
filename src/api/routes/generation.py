from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextGenerationRequest(BaseModel):
   title: str
   context: str = ""

@router.post("/text")
async def generate_text(request: TextGenerationRequest):
   return {"text": f"Generated text for {request.title}"}
