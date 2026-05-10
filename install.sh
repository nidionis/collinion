#!/bin/bash

# Create the virtual environment using virtualenv
virtualenv .venv

# Upgrade pip to ensure smooth installation
./.venv/bin/pip install --upgrade pip

# Install requirements
./.venv/bin/pip install -r requirements.txt

echo "--------------------------------------------------------"
echo "Setup complete!"
echo "To activate the virtual environment, run the following command:"
echo "source .venv/bin/activate"
echo "--------------------------------------------------------"