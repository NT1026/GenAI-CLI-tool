# PaLM CLI-tool

PaLM CLI-tool is a tool programming by PaLM Python package, which can help us get response from PaLM conveniently.

## Installation

Before using this tool, we need to create an API key from [MakerSuite](https://makersuite.google.com/app/apikey) first.

### Installation For Windows

1. Check that Python3 is installed in your machine.
2. Download PaLM CLI-tool ZIP from GitHub and extract it.
3. Double click `setup.bat` to start installing. (Or run `setup.bat` under PaLM CLI-tool directory.)

### Installation For Mac / Linux (Ubuntu is okay)

1. Check that Python3 is installed in your machine.
2. Download PaLM CLI-tool ZIP from GitHub and extract it.
3. Double click `setup` to start installing. (Or run `./setup` under PaLM CLI-tool directory.)

## Docker image

(TODO)

## Usage

Use `python main.py -m <your-message>` to ask PaLM and get a response.

And use `python main.py -h` to get more information.

For example,

```
$ python main.py -m "Hello, PaLM."
```

## Tips

Use virtual envirenment to avoid package dependency conflicting.

Maybe use an alias to make it more convenient. For example,

```
$ alias palm="~/PaLM-CLI-tool/.venv/bin/python3 ~/PaLM-CLI-tool/main.py"
$ palm -m "Hello, PaLM."
```
