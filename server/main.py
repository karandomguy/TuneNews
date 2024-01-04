from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import song_gen
lyricist = song_gen.TuneNewsModel()

class Paragraph(BaseModel):
    paragraph: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def get_root():
    return "This is the RESTful API for TuneNews"

@app.post("/generated_song")
async def lyrics(text: Paragraph):
    song_lyrics = lyricist.tnm_pipeline(text.paragraph)

    return {
        "song": song_lyrics
    }