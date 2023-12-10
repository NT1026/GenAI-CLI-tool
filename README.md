# PaLM CLI-tool

PaLM CLI-tool is a tool programming by PaLM Python package, which can help us get response from PaLM conveniently.

## Installation

### For Mac / Linux (Ubuntu is okay)

1. Check that Python3 is installed in your machine.
2. Download PaLM CLI-tool ZIP and extract it.
3. Open your shell, and change your working directory under PaLM CLI tool.
4. Run `./setup`.
5. Complete installation.

## Docker image

(TODO)

## Usage

Before using this tool, we need to create an API key from [MakerSuite](https://makersuite.google.com/app/apikey) first.

Use `python main.py --apikey <your-apikey>` to configure your API key to PaLM CLI-tool.

Then use `python main.py -m <your-message>` to ask PaLM, and get a response.

Use `python main.py -h` to get more information.

## Tips

Maybe use an alias to make it more convenient.

```
$ alias palm="python <path-to-this-tool>/main.py"

$ palm -m "Say hello world."
```
