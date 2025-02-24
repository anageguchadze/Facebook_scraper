# Facebook_scraper

This is a Django-based web application that scrapes and saves Facebook posts using the Facebook Graph API. The project is structured with a `scraper` app handling API requests and saving data to a CSV file.

## Features
- Scrapes Facebook posts using the Facebook Graph API
- Saves posts in CSV format
- Django REST API endpoint for fetching and processing data
- Docker support

## Installation
### Prerequisites
- Python 3.8+
- Django 5.1.6+
- Facebook Developer Account with an access token

### Steps
1. Clone the repository:
   git clone https://github.com/anageguchadze/Facebook_scraper.git
   cd Facebook-scraper
   
3. Create a virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
  
4. Set up environment variables for your Facebook API credentials.
5. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver
  
6. Access the API at `http://localhost:8000/facebook_data/`

## API Endpoint
- **GET /facebook_data/** - Fetches and saves Facebook posts to CSV.

## License
This project is licensed under the MIT License.

## Contact
For issues, open a GitHub issue or reach out via email.

