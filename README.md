# CurrencyConverter [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Tech Stack💻
- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- REST API

## API used
- CurrencyAPI

# Development Tools
- PyCharm IDE

# Deployment Tools
- Vercel

## Quick Start with Docker
1. Environment Variables
Create a `.env` file or pass them directly:

|       Variable     |         Description               |
|--------------------|-----------------------------------|
| `CURRENCY_API_KEY` | API key from currencyapi.com      |
| `FLASK_SECRET_KEY` | Secret key for session encryption |


2. Build the Docker Image
```shell
docker build -t currency-converter .
```
3. Run the Container
```shell
docker run -d -p 5000:5000 \
  --env-file .env \
  --name currency-app \
  currency-converter
```
4. Access the Application
Open your browser and navigate to:

```
http://localhost:5000
```


## Screenshots
<img width="1919" height="958" alt="currencyconverter_screenshot_1" src="https://github.com/user-attachments/assets/7626b075-a216-4d75-b869-cd283e12fcdb" />
<img width="1622" height="787" alt="image" src="https://github.com/user-attachments/assets/498bcfb4-3a2c-4934-8414-61635e06bf6f" />


## License
MIT License
