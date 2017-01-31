#!/bin/bash -e

if [ ! -d "ve/" ]; then
    virtualenv -q ve/ --no-site-packages
    echo "Virtualenv created."
fi

source ve/bin/activate

if [ ! -f "ve/updated" -o requirements.txt -nt ve/updated ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    touch ve/updated
    echo "Requirements installed."
fi

./run.sh
