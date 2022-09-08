from fastapi import FastAPI,Body, status

from utils import to_dict
from chatbot import wikibot, wikibot_test
from reply import replier
from blendrbot import blenderbot



app = FastAPI()

@app.post(
    path = "/",
    status_code=status.HTTP_200_OK,
    tags = ['Home']
)
async def message(res: str = Body(...)):
    response = to_dict(res)
    
    if response["message"].startswith('/'):

        #intent = wikibot_test(response['message'].split("/")[1])
        #reply = replier(intent[0]['intent'])
        #print(reply.encode('utf-8'))
        #return {"reply": reply.encode('utf-8')} 
        print(response['sender'],response['message'].split("/")[1])
        return {"reply":blenderbot(response['message'].split("/")[1])}
        