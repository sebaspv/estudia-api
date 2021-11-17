from fastapi import FastAPI
import uvicorn
from Questgen import main

app = FastAPI()

model = main.QGen()
@app.get("/api/faq/{prompt}")
async def hello(prompt: str):
    payload = {"input_text": prompt}
    output = model.predict_shortq(payload)
    return output

if __name__ == "__main__":
    uvicorn.run(app, port=8000)