from fastapi import FastAPI,Body, status

from utils import to_dict
from chatbot import wikibot

app = FastAPI()

@app.get(
    path = '/',
    status_code=status.HTTP_200_OK,
    tags= ['Home']
)
def home():
    return {'reply':'Hi im wiki'}

@app.post(
    path = "/",
    status_code=status.HTTP_200_OK,
    tags = ['Home']
)
async def message(res: str = Body(...)):
    response = to_dict(res)
    if response["message"].startswith('/'):
        reply = wikibot(response['message'].split("/")[1])
        return {"reply": reply} 
        