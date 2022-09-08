from transformers import   BlenderbotTokenizer,BlenderbotForConditionalGeneration

tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("blenderbot_model")
from googletrans import Translator
translator = Translator()

filt = {
    'á':'a',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u',
    'Á':'A',
    'É':'E',
    'Í':'I',
    'Ó':'O',
    'Ú':'U',
    'ñ':'n',
    'Ñ':'N',
    '¿':'',
    '!':''}

def blenderbot(sentence):
    sentence_trans = translator.translate(sentence)
    tokenize = tokenizer(sentence_trans.text, return_tensors="pt")
    resp = model.generate(**tokenize)
    reply = tokenizer.decode(resp[0]).replace("<s>","").replace("</s>","")
    reply = translator.translate(reply, dest='es').text
    print(reply)
    for key, value in filt.items():
        reply = reply.replace(key,value)
    return reply



