#!/usr/bin/env python3
"""
Script to remove background from Python logo using rembg library.
"""

from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path=None):
    """
    Remove background from an image using rembg.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the output image (optional)
                          If not provided, will use input filename with _nobg suffix
    """
    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove background
        output_image = remove(input_image)
        
        # Determine output path
        if output_path is None:
            # Create output filename with _nobg suffix
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_nobg{ext}"
        
        # Save the result
        output_image.save(output_path)
        print(f"Background removed successfully!")
        print(f"Input: {input_path}")
        print(f"Output: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

if __name__ == "__main__":
    # Configuration
    input_image = "python-logo-11609373642q9ewsev5ea.png"
    output_image = "python-logo-11609373642q9ewsev5ea_nobg.png"
    
    # Check if input file exists
    if not os.path.exists(input_image):
        print(f"Error: Input file '{input_image}' not found!")
    else:
        # Remove background
        result = remove_background(input_image, output_image)
        if result:
            print(f"✓ Successfully created: {output_image}")
        else:
            print("✗ Failed to remove background")
