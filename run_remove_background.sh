#!/bin/bash

echo "Setting up environment for background removal..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv bg_removal_env

# Activate virtual environment
echo "Activating virtual environment..."
source bg_removal_env/bin/activate

# Install dependencies
echo "Installing rembg and dependencies..."
pip install rembg pillow

# Run the background removal script
echo "Running background removal script..."
python3 remove_background.py

echo ""
echo "Process completed! Check for the _nobg.png file."

# Keep the terminal open (optional, for user to see results)
echo ""
echo "Press Enter to exit..."
read
