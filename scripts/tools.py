DOTENV_FILEPATH = f"/Users/nt1026/Documents/PaLM-CLI-tool/palm.conf"


def get_dotenv_contents():
    results = {
        "PALM_APIKEY": None,
        "PALM_CONTEXT": None,
        "PALM_TEMPERATURE": None
    }
    with open(DOTENV_FILEPATH, "r") as file:
        for line in file:
            line_list = line.replace("\n", "").split("=")
            results[line_list[0]] = line_list[1]
    
    return results.copy()
    