import argparse
from scripts.model import PaLM
from scripts.tools import DOTENV_FILEPATH
from scripts.tools import get_dotenv_contents


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description="PaLM CLI-tool is a tool programming by PaLM Python package, which can help us get response from PaLM conveniently.")

    run = parser.add_argument_group(title="use PaLM to generate response")
    run.add_argument("-m", "--message", help="set your input message you want to ask PaLM.")

    configs = parser.add_argument_group(title="configurations")
    configs.add_argument("-s", "--show", help="show your palm configurations.", action="store_true")
    configs.add_argument("-a", "--apikey", help="set your API key created in MakerSuite.")
    configs.add_argument("-c", "--context", help="set the context of PaLM. These context will be provided to the model first, to ground the response.")
    configs.add_argument("-t", "--temperature", help="set the temperature of PaLM. The value is in [0.0, 1.0]. Higher values produce a more random and varied response.")

    args = parser.parse_args()
    

    # Handling .env file
    dotenv_content = get_dotenv_contents()
    with open(DOTENV_FILEPATH, "w") as file:
        if args.apikey:
            dotenv_content["PALM_APIKEY"] = args.apikey
            print("Set API Key Successfully...")
        if args.context:
            dotenv_content["PALM_CONTEXT"] = args.context
            print("Set Context Successfully...")
        if args.temperature:
            dotenv_content["PALM_TEMPERATURE"] = args.temperature
            print("Set Tempurature Successfully...")

        file.write(f"PALM_APIKEY={dotenv_content['PALM_APIKEY']}\n")
        file.write(f"PALM_CONTEXT={dotenv_content['PALM_CONTEXT']}\n")
        file.write(f"PALM_TEMPERATURE={dotenv_content['PALM_TEMPERATURE']}")


    # Show the configurations
    if args.show:
        dotenv_content = get_dotenv_contents()
        print("---")
        print(f"PALM_APIKEY = {dotenv_content['PALM_APIKEY']}")
        print(f"PALM_CONTEXT = {dotenv_content['PALM_CONTEXT']}")
        print(f"PALM_TEMPERATURE = {dotenv_content['PALM_TEMPERATURE']}")
        print("---")

    # Send message to PaLM
    if args.message:
        response = PaLM(input=args.message)
        print(response)
    