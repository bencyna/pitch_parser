#!/bin/bash


python_file="Main.py"

python3 -m venv venv

source venv/bin/activate

pip install pydub

python3 "$python_file" 4