#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Tesseract OCR
if ! command -v tesseract >/dev/null 2>&1; then
    echo "Tesseract not found. Installing Tesseract OCR..."
    brew install tesseract
fi

# Install poppler-utils
if ! command -v pdftoppm >/dev/null 2>&1; then
    echo "Poppler not found. Installing poppler-utils..."
    brew install poppler
fi

# Set the executable permission for the binary
chmod +x pdf_to_txt_converter

# Run the binary
./pdf_to_txt_converter
