# CurrencyConverter [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
<p align="center">
  <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Freshmaharidhas%2FCurrencyConverter&label=Visitors&labelColor=%2300ff00&countColor=%23000000&style=plastic&labelStyle=none"/>
  <img src="https://img.shields.io/github/forks/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/languages/top/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/repo-size/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/languages/code-size/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/languages/count/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/contributors/reshmaharidhas/CurrencyConverter?labelColor=%23000&color=%23FF5B00"/>
  <img src="https://img.shields.io/github/created-at/reshmaharidhas/CurrencyConverter"/>
  <img src="https://img.shields.io/github/license/reshmaharidhas/CurrencyConverter"/>  
</p>
Web app to calculate all international currency conversion based on latest currency exchange rates.

# Tech Stack💻
- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- REST API

## API used
- CurrencyAPI

## Development Tools
- PyCharm IDE

## Deployment Tools
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
<img width="1919" height="965" alt="currencyconverter_screenshot_2" src="https://github.com/user-attachments/assets/cc27ba36-8c74-49be-baf8-a3c2203ca264" />

## License
MIT License
