from fastapi import FastAPI
import random
from random import randint
import requests

listkey = ['baodeonghe','randomphone','damchomayphat']
app = FastAPI()

@app.get('/getphone/key={key}')
async def home(key:str):
    loi = 1
    for acc in listkey:
        if acc == key:
            loi = 0
    if loi == 1:
        return {'status','key Sai hoặc hết hạn'}
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    phones = random_with_N_digits(7)
    dau_so = ['+8470','+8479','+8477','+8476','+8478','+8492','+8456','+8458','+8488','+8490','+8493']
    phone = random.choice(dau_so)+str(phones)
    data =  {'phone':phone,'status':true,'license':'Hà Đức Hậu'}
    return data
