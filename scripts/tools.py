from scripts.configs import CONFIG_FILEPATH


def get_dotenv_contents():
    results = {
        "PALM_APIKEY": None,
        "PALM_CONTEXT": None,
        "PALM_TEMPERATURE": None
    }
    with open(CONFIG_FILEPATH, "r") as file:
        for line in file:
            line_list = line.replace("\n", "").split("=")
            results[line_list[0]] = line_list[1]
    
    return results.copy()
    