# GenAI CLI-tool

GenAI CLI-tool is a tool programming by Gemini Python API, which can help us get response from Gemini conveniently.

## Installation

Before using this tool, we need to create an API key from [MakerSuite](https://makersuite.google.com/app/apikey) first.

### Installation For Windows

1. Check that Python3 is installed in your machine.
2. Download GenAI CLI-tool ZIP from GitHub and extract it.
3. Double click `setup.bat` to start installing. (Or run `setup.bat` under GenAI CLI-tool directory.)

### Installation For Mac / Linux (Ubuntu is okay)

1. Check that Python3 is installed in your machine.
2. Download GenAI CLI-tool ZIP from GitHub and extract it.
3. Double click `setup` to start installing. (Or run `./setup` under GenAI CLI-tool directory.)

## Docker image

(TODO)

## Discord bot

(TODO)

## Usage

Use `python main.py -m <your-message>` to ask Gemini and get a response.

For example,

```
$ python main.py -m "Hello, Gemini."
$ python main.py -m "請告訴我 Gemini 是什麼"
```

Use `python main.py -i` to enter the interactive mode. 

You can use command `!exit()` to exit interactive mode, or `!history()` to check your chat history in this session.

Use `python main.py -h` to get more information.

## Tips

Use virtual envirenment to avoid package dependency conflicting.

Maybe use an alias to make it more convenient. For example,

```
$ alias gemini="~/GenAI-CLI-tool/.venv/bin/python3 ~/GenAI-CLI-tool/main.py"
$ gemini -m "Hello, Gemini."
```

## Release

2023-12-11: v1       -- PaLM-CLI-tool (You can find it at branch `GenAI-CLI-tool-v1`)

2024-01-05: v2.0.0 -- Since Google GenAI API update, rename PaLM-CLI-tool to GenAI-CLI-tool.

2024-01-13: v2.0.1 -- Interactive mode can view chat history now.
