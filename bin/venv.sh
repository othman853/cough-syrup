#! /bin/bash
SCRIPT_ROOT=$0
VENV_NAME=$1

if [ ! -d "$SCRIPT_ROOT/$VENV_NAME" ]; then
    pip3 install virtualenv
    mkdir $VENV_NAME
    python -m venv $VENV_NAME
else
    echo 'Virtualenv already created. Run: "source .venv/bin/activate" to use it'
fi
echo 'Done'
