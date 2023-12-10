#!/bin/sh

tab="    "

echo "\n==================================="
echo "This is PaLM CLI-tool setup script."
echo "==================================="
sleep 1

echo "\nStart Installation..."
sleep 3


# A. Check if Python and Virtualenv is existed
echo "\nA. Check if Python and Virtualenv is existed...\n"
sleep 1

# A-1. Check if Python is existed.
python=`which python`
if [ $? -ne 0 ] ; then
    python=`which python3`
    if  [ $? -ne 0 ] ; then
        echo "${tab}* Installation FAILED *"
        echo "${tab}* Please install Python/Python3 first *"
        exit
    fi
fi
echo "${tab}A-1. You have installed Python ($python)!"
sleep 1

# A-2. Check if Pip is existed.
pip=`which pip`
if [ $? -ne 0 ] ; then
    pip=`which pip3`
    if  [ $? -ne 0 ] ; then
        echo "${tab}* Installation FAILED *"
        echo "${tab}* Please install Pip/Pip3 first *"
        exit
    fi
fi
echo "${tab}A-2. You have installed Pip ($pip)!"
sleep 1

# A-3. Check if Virtualenv is existed.
virtualenv=`$python -m virtualenv --version`
if [ $? -ne 0 ] ; then 
    $pip install virtualenv > /dev/null 2>&1
    virtualenv=`$python -m virtualenv --version`
fi
echo "${tab}A-3. You have installed Virtualenv ($virtualenv)!"


# B. Create virtual envirenments of PaLM
echo "\nB. Create virtual envirenments of PaLM...\n"
sleep 1

# B-1. Create virtual envirenments
$python -m virtualenv .venv > /dev/null 2>&1
echo "${tab}B-1. Virtual envirenments (.venv) is created!"
sleep 1

# B-2. Download necessary python package into venv
source $PWD/.venv/bin/activate
$PWD/.venv/bin/pip3 install -r $PWD/requirements.txt > /dev/null 2>&1
deactivate
echo "${tab}B-2. Necessary python packages in requirements.txt are all installed."
sleep 1


# C. Other configurations
echo "\nC. Set other configurations\n"
sleep 1

# C-1. Set scripts/configs.py
echo "DOTENV_FILEPATH = \"$PWD/.env\"" > $PWD/scripts/configs.py
echo "${tab}C-1. Setting scripts/configs.py...Success!"
sleep 1

# C-2 Set .env
echo "${tab}C-2. Setting API key created in MakerSuite (https://makersuite.google.com/app/apikey)..."
sleep 1

read -p "${tab}${tab} Please Enter you API key: " apikey
echo "PALM_APIKEY=$apikey\nPALM_CONTEXT=None\nPALM_TEMPERATURE=None" > $PWD/.env
unset apikey
echo "${tab}${tab} ...Success!\n"
sleep 1


# Complete installation!
echo "================================================================================================"
echo "\nYou have completed the installation of PaLM CLI-tool!"
echo "\nPlease use \`$PWD/.venv./bin/python3 main.py -m <your-question>\` to get a response from PaLM."
echo "\nOr use \`$PWD/.venv./bin/python3 main.py -h\` to get help information."
echo "\nYou can also make an alias in your startup file (e.g. ~/.bashrc) to make it more convenient.\n"
echo "\nHave fun!\n"
echo "================================================================================================"
