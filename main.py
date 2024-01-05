import argparse
from scripts.model import GenAI

genai = GenAI()


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description="GenAI CLI-tool is a tool programming by Gemini Python API.")

    run = parser.add_argument_group(title="use Gemini to generate response")
    run.add_argument("-i", "--interactive", help="interactive mode.", action="store_true")
    run.add_argument("-m", "--message", help="set your question you want to ask Gemini.")

    configs = parser.add_argument_group(title="configurations")
    configs.add_argument("-s", "--show", help="show your configurations.", action="store_true")
    configs.add_argument("-a", "--apikey", help="set your API key created in MakerSuite.")
    # configs.add_argument("-c", "--context", help="set the context of PaLM. These context will be provided to the model first, to ground the response.")
    configs.add_argument("-o", "--maxOutputTokens", help="set the max output tokens of the response.")
    configs.add_argument("-n", "--name", help="customize the nickname of LLM.")
    configs.add_argument("-t", "--temperature", help="set the temperature of LLM. The value is in [0.0, 1.0]. Higher values produce a more random and varied response.")

    args = parser.parse_args()
    

    # Handling arguments
    if args.show:
        genai.get_configs()
        
    if args.apikey:
        genai.set_configs(key="GENAI_APIKEY", value=args.apikey)
        print("Set API Key Successfully...")

    # if args.context:
    #     dotenv_content["PALM_CONTEXT"] = args.context
    #     print("Set Context Successfully...")
    
    if args.maxOutputTokens:
        genai.set_configs(key="GENAI_MAX_OUTPUT_TOKENS", value=args.maxOutputTokens)
        print("Set Max-Output-Tokens Successfully...")

    if args.name:
        genai.set_configs(key="GENAI_NAME", value=args.name)
        print("Set Name Successfully...")

    if args.temperature:
        genai.set_configs(key="GENAI_TEMPERATURE", value=args.temperature)
        print("Set Tempurature Successfully...")


    # Initial GenAI
    genai.save_configs()
    genai.init_genai()


    # Start chatting
    if args.interactive:
        while True:
            message = input("You: ")
            if message == "!exit()":
                break

            genai.send(message)

    if args.message:
        genai.send(args.message)
