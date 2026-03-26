from fastapi import FastAPI , BackgroundTasks
import httpx
from bs4 import BeautifulSoup
import asyncio

app = FastAPI()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

notebook = {"Company / Stock" : "waiting..." ,"current_price": "Waiting..."}

async def get_info(url : str):
    while True:
        async with httpx.AsyncClient() as client:
            res = await client.get(url , headers=headers)
            soup = BeautifulSoup(res.text , 'html.parser')
            price = soup.find("span" ,  {"data-testid" : "qsp-post-price" })
            cname = soup.find("h1" ,  {"class" : "yf-18s5v3y" })
            # TEMPORARY: Save the HTML to a file to see what Python sees

            if price:
                cname_txt = cname.text.strip()
                price_txt = price.text.replace("₹" , "").replace("," , "").strip()
                notebook['current_price'] = price_txt
                notebook["Company / Stock"] = cname_txt
    await asyncio.sleep(3)


@app.get('/s')
async def get_inf(url :str , backg : BackgroundTasks):
    backg.add_task(get_info , url)

    return "The server is checking"

@app.get('/show')
async def show_P():
    return notebook