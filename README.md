# MultiBot with AIOGram3 and Docker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository provides a simple example of creating a multi-bot application using AIOGram3 and Docker. With this setup, you can easily develop and deploy multiple Telegram bots within a Docker environment.

## Setup:

1. **Clone the Repository:**
```
git clone https://github.com/yourusername/multibot-aiogram.git
```
```
cd multibot-aiogram
```
2.**Start Ngrok:**
- Before running the Docker container, start Ngrok to expose your local server to the internet:
```
ngrok http 2000
```
3. **Build the Docker Container:**
```
docker compose build
```
4.**Run the Docker Container:**
   ```
   docker compose up
   ```
