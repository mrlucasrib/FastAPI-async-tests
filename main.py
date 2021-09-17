from time import sleep
from fastapi import FastAPI
import asyncio
import time
app = FastAPI()


@app.get("/thread_blocking")
def root():
    # Thread com sleep sincrono
    time.sleep(0.5)
    return {"message": "Hello World"}

@app.get("/thread_non_blocking")
def root():
    # Thread sem sleep
    return {"message": "Hello World"}

@app.get("/async_blocking")
async def root():
    # coroutina com codigo bloqueante
    time.sleep(0.5)
    return {"message": "Hello World"}

@app.get("/async_non_blocking")
async def root():
    # coroutina com codigo não bloqueante
    await asyncio.sleep(0.5)
    return {"message": "Hello World"}

@app.get("/async")
async def root():
    # coroutina vazia
    return {"message": "Hello World"}