from requests.api import request
from fastapi import APIRouter
from Questgen.main import QGen
import requests
import urllib
from dotenv import dotenv_values

router = APIRouter()
model = QGen()
url_to_english = dotenv_values(".env")['URL'] + "to_english/"
url_to_spanish = dotenv_values(".env")['URL'] + "to_spanish/"

@router.get("/english/{prompt}")
async def faq(prompt: str) -> dict:
    try:
        payload = {"input_text": prompt}
        output = model.predict_shortq(payload)
        return output
    except:
        return {"questions": None}


@router.get("/spanish/{prompt}")
async def faq_spanish(prompt: str) -> dict:
    url = url_to_english + urllib.parse.quote(prompt, safe="")
    translated_prompt = requests.get(url=url).json()["translated"]
    payload = {"input_text": translated_prompt}
    output = model.predict_shortq(payload)
    spanish_questions = []
    if "questions" not in output:
        return {"questions": None, "translated_prompt": translated_prompt}
    for question in output["questions"]:
        new_question = {}
        question_url = url_to_spanish + urllib.parse.quote(question["Question"], safe="")
        answer_url = url_to_spanish + urllib.parse.quote(question["Answer"], safe="")
        new_question["Question"] = requests.get(url=question_url).json()[
            "translated"
        ]
        new_question["Answer"] = requests.get(url=answer_url).json()["translated"]
        spanish_questions.append(new_question)
    translated_questions = {"questions": spanish_questions, "translated_prompt": translated_prompt}
    return translated_questions
