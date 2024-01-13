import os
import google.generativeai as genai
from dotenv import load_dotenv
from scripts.configs import DOTENV_FILEPATH as DOTENV

configs_message = {
    "GENAI_APIKEY": "API Key",
    "GENAI_MAX_OUTPUT_TOKENS": "Max-Output-Tokens",
    "GENAI_NAME": "Nickname",
    "GENAI_TEMPERATURE": "Temperature"
}

class GenAI:
    def __init__(self):
        load_dotenv(DOTENV)
        self.configs = {
            "GENAI_APIKEY": os.getenv("GENAI_APIKEY"),
            "GENAI_MAX_OUTPUT_TOKENS": int(os.getenv("GENAI_MAX_OUTPUT_TOKENS")),
            "GENAI_MODEL": "gemini-pro",
            "GENAI_NAME": os.getenv("GENAI_NAME"),
            "GENAI_TEMPERATURE": float(os.getenv("GENAI_TEMPERATURE"))
        }

    def set_configs(self, key, value):
        self.configs[key] = value
        print(f"Set {configs_message[key]} Successfully...")

    def get_configs(self):
        print(f"---")
        print(f"GENAI_APIKEY = {self.configs['GENAI_APIKEY']}")
        print(f"GENAI_MAX_OUTPUT_TOKENS = {self.configs['GENAI_MAX_OUTPUT_TOKENS']}")
        print(f"GENAI_MODEL = {self.configs['GENAI_MODEL']}")
        print(f"GENAI_NAME = {self.configs['GENAI_NAME']}")
        print(f"GENAI_TEMPERATURE = {self.configs['GENAI_TEMPERATURE']}")
        print(f"---")

    def save_configs(self):
        with open(DOTENV, "w") as file:
            file.write(f"GENAI_APIKEY={self.configs['GENAI_APIKEY']}\n")
            file.write(f"GENAI_MAX_OUTPUT_TOKENS={self.configs['GENAI_MAX_OUTPUT_TOKENS']}\n")
            file.write(f"GENAI_MODEL={self.configs['GENAI_MODEL']}\n")
            file.write(f"GENAI_NAME={self.configs['GENAI_NAME']}\n")
            file.write(f"GENAI_TEMPERATURE={self.configs['GENAI_TEMPERATURE']}\n")
        
    def init_genai(self):
        genai.configure(api_key=self.configs['GENAI_APIKEY'])
        self.model = genai.GenerativeModel(self.configs['GENAI_MODEL'])
        self.chat = self.model.start_chat()
    
    def send(self, input):
        response = self.chat.send_message(
            content=input,
            generation_config={
                "temperature": self.configs['GENAI_TEMPERATURE'],
                "max_output_tokens": self.configs['GENAI_MAX_OUTPUT_TOKENS']
            }
        )
        return f"{self.configs['GENAI_NAME']}: {response.text}"

    def history(self):
        return self.chat.history
    