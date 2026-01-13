# Chatbot4PolyU - Diet Recording Application

A web-based food/diet tracking application designed for the PolyU study. Users can record their daily meals with photos, descriptions, and timing information.

## Features

- **Personal Information**: Collect user demographics (name, ID, gender, age)
- **Flexible Recording**: Record meals for workdays and rest days
- **Photo Upload**: Capture or upload food photos
- **Meal Details**: Track meal type, time, location, and amount consumed
- **Multi-Meal Recording**: Support for main meals (breakfast, lunch, dinner) and snacks (morning, afternoon, evening)
- **Completion Tracking**: View daily progress and completion status
- **Summary Reports**: View all recorded meals with statistics

## Deployment on Render

This application is deployed using Render's free tier with Python Flask.

### Live Application
Visit: [Your Render URL will be here after deployment]

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/eftechust-team/chatbot4polyu_full.git
cd chatbot4polyu
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask app:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
├── app.py                  # Flask application server
├── form.html              # Main form/chatbot interface
├── form-script.js         # Main chatbot logic and meal recording
├── form-style.css         # Form styling
├── style.css              # General styling
├── index.html             # Landing page
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
└── README.md             # This file
```

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Backend**: Python Flask
- **Deployment**: Render
- **Version Control**: Git/GitHub

## Features in Detail

### Meal Recording Flow
1. User enters basic information (name, participant ID, gender, age)
2. Selects recording date (workday 1, workday 2, or rest day)
3. Chooses meal type to record
4. Uploads food photo(s)
5. Provides description of food and portion
6. Records meal time, location, and amount eaten
7. Views completion summary

### Data Tracking
- Tracks recorded meals throughout the day
- Shows progress towards completing all meal recordings
- Calculates total photos uploaded
- Displays meal counts by type

### Multi-Day Support
- Record data for multiple days
- Start new recording day with date selection
- Supplement records for current day
- View all historical records

## Notes

- No backend database - data is stored in browser's JavaScript variables during session
- Fully client-side form submission and data management
- Mobile-friendly responsive design
- Traditional Chinese language support
