from urllib.parse import unquote
from datetime import datetime

def to_dict(res:str):
    res_dict = {}
    resquest = res.split("&")
    resquest.pop()
    for res in resquest:
            res_dict[res.split("=")[0]] = unquote(res.split("=")[1].replace("+"," "))
            res_dict["time"] =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return res_dict