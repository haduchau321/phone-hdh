from fastapi import FastAPI
import random
from random import randint


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
    dau_so = ['032','033','034','035','036','037','038','039','070','079','077','076','078','083','084','085','081','082','056','058','059']
    phone = random.choice(dau_so)+str(phones)

    data =  {'phone':phone,'status':True,'license':'Hà Đức Hậu'}
    return data
