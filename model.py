import os
import google.generativeai as palm
from dotenv import load_dotenv
from tools import DOTENV_FILEPATH


def PaLM(input):
    load_dotenv(DOTENV_FILEPATH)
    palm.configure(api_key=os.getenv("PALM_APIKEY"))

    if os.getenv("PALM_TEMPERATURE"):
        response = palm.chat(
            messages=input,
            context=os.getenv("PALM_CONTEXT")
        )
    else:
        response = palm.chat(
            messages=input,
            context=os.getenv("PALM_CONTEXT"),
            temperature=os.getenv("PALM_TEMPERATURE")
        )

    return response.last
