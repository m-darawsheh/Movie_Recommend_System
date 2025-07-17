#!/bin/bash

# Script to run the Movie Recommendation System Flask application

echo "🎬 Starting Movie Recommendation System..."
echo "📂 Project Directory: $(pwd)"

# Activate virtual environment
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Please run:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "📦 Installing requirements..."
    pip install -r requirements.txt
fi

# Run the Flask application
echo "🚀 Starting Flask server..."
echo "🌐 Application will be available at: http://localhost:5001"
echo "👉 Press Ctrl+C to stop the server"
echo ""

python main.py
