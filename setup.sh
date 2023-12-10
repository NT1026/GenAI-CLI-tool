#!/bin/sh

tab="    "

echo "\n==================================="
echo "This is PaLM CLI-tool setup script."
echo "==================================="
sleep 1

echo "\nStart Installation..."
sleep 3


# A. Check if Python is existed.
echo "\nA. Check if Python is existed...\n"
sleep 1

python=`which python`
if [ $? -ne 0 ] ; then
    python=`which python3`
    if  [ $? -ne 0 ] ; then
        echo "${tab}* Installation FAILED *"
        echo "${tab}* Please install Python/Python3 first *"
        exit
    fi
fi
echo "${tab}You have installed Python ($python)!"
sleep 1


# B. Create virtual envirenments of PaLM
echo "\nB. Create virtual envirenments of PaLM...\n"
sleep 1

# B-1. Create virtual envirenments
$python -m venv .venv > /dev/null 2>&1
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
echo "CONFIG_FILEPATH = \"$PWD/palm.conf\"" > $PWD/scripts/configs.py
echo "${tab}C-1. Setting scripts/configs.py...Success!"
sleep 1

# C-2 Set palm.conf
echo "${tab}C-2. Setting API key created in MakerSuite (https://makersuite.google.com/app/apikey)..."
sleep 1

read -p "${tab}${tab} Please Enter you API key: " apikey
echo "PALM_APIKEY=$apikey\nPALM_CONTEXT=None\nPALM_TEMPERATURE=None" > $PWD/palm.conf
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
