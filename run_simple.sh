#!/bin/bash

echo "Installing rembg and processing Python logo..."

# Install directly to user site-packages
pip3 install --user rembg pillow 2>/dev/null

# Try to run the script directly
python3 remove_background.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Background removal completed successfully!"
    echo "Check for: python-logo-11609373642q9ewsev5ea_nobg.png"
else
    echo ""
    echo "Installation may have failed. Trying alternative method..."
    
    # Try using pipx or direct installation
    pip3 install rembg --break-system-packages 2>/dev/null || \
    pip3 install rembg 2>/dev/null
    
    # Run again
    python3 remove_background.py
fi

echo ""
echo "Done!"
