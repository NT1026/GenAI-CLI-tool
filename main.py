import argparse
import google.generativeai as palm
import os
from dotenv import load_dotenv


def PaLM(input):
    palm.configure(api_key=os.getenv("PALM_APIKEY"))
    response = palm.chat(messages=input)

    return response.last

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    configs = parser.add_argument_group(title="Usage")
    configs.add_argument("--apikey", help="Set your API key created in MakerSuite.")
    configs.add_argument("-m", "--message", help="Set your input message you want to ask PaLM.")
    
    args = parser.parse_args()
    
    if args.apikey:
        with open("/Users/nt1026/Documents/PaLM-CLI-tool/.env", "w") as dotenv:
            dotenv.write(f"PALM_APIKEY={args.apikey}")
            print("Successfully!")
    
    if args.message:
        load_dotenv("/Users/nt1026/Documents/PaLM-CLI-tool/.env")
        response = PaLM(input=args.message)
        print(response)
