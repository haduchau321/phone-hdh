from fastapi import FastAPI
import random
from random import randint


app = FastAPI()

@app.get('/')
async def home():
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    phones = random_with_N_digits(7)
    dau_so = ['+8470','+8479','+8477','+8476','+8478','+8492','+8456','+8458','+8488','+8490','+8493']
    data =  {'phone':random.choice(dau_so)+str(phones),'license':'Hà Đứu Hậu'}
    return data 



