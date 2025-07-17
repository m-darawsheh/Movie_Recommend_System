# 🎬 Movie Recommendation System

A Flask-based web application that allows users to search for movies by actor or director names using the TMDB dataset.

## Features

- 🔍 Search movies by actor or director name
- 🎭 Beautiful red and black themed interface
- 📱 Responsive design with Arabic support
- 🎨 Modern UI with animations and effects

## Prerequisites

- Python 3.7 or higher
- pip package manager
- Required CSV files:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

## Quick Start

### Option 1: Using the Bash Script (Recommended for Linux/Mac)

```bash
# Make the script executable (if not already)
chmod +x run.sh

# Setup and check packages
./run.sh

# Setup and run the application immediately
./run.sh run
```

### Option 2: Using the Python Script (Cross-platform)

```bash
# Run the setup script
python3 setup_and_run.py
```

### Option 3: Manual Setup

```bash
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage

1. Open your web browser and go to `http://localhost:5001`
2. Click "Start Search" on the main page
3. Enter an actor or director name in Arabic or English
4. View the search results

## Project Structure

```
Movie_Recommend_System/
├── main.py                 # Main Flask application
├── requirements.txt        # Python dependencies
├── run.sh                 # Bash setup and run script
├── setup_and_run.py       # Python setup and run script
├── tmdb_5000_movies.csv   # Movie data (required)
├── tmdb_5000_credits.csv  # Credits data (required)
└── templates/
    ├── index.html         # Main page
    ├── input_page.html    # Search page
    └── results.html       # Results page
```

## Required Packages

- Flask==2.3.3
- pandas==2.0.3
- Werkzeug==2.3.7

## Scripts Explanation

### `run.sh` (Bash Script)
- Checks Python and pip installation
- Creates virtual environment
- Installs dependencies
- Validates required files
- Optionally runs the application

### `setup_and_run.py` (Python Script)
- Cross-platform Python setup script
- Checks system requirements
- Installs packages
- Validates project files
- Interactive setup process

## Troubleshooting

1. **Missing CSV files**: Download the TMDB 5000 movie dataset
2. **Port already in use**: Change the port in `main.py` (line 46)
3. **Package installation issues**: Try upgrading pip: `pip install --upgrade pip`

## Color Theme

The application uses a red and black color scheme:
- Primary: #ff0000 (Red)
- Secondary: #cc0000 (Dark Red)
- Background: #000000 (Black)
- Accent: #330000 (Dark Red)

## License

This project is for educational purposes.
