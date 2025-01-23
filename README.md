
# 🦜 LangChain Translator API

![banner](./langserve-playground.gif)

A simple yet powerful translation API built with LangChain and FastAPI. This project demonstrates how to create a translation service using OpenAI's language models through LangChain's interfaces.


## Demo

Insert gif or link to demo


## Badges

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-white?style=for-the-badge)](https://www.langchain.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## 🚀 Tech Stack

- FastAPI - Web framework
- LangChain - LLM framework
- OpenAI - Language model provider
- Python-dotenv - Environment management
- Uvicorn - ASGI server
- Docker - Containerization


## 🛠️ Installation

1. Clone the repository:
```bash
bash
git clone https://github.com/pakagronglb/simple-langchain-translator.git
cd simple-langchain-translator
```

2. Create a virtual environment:
```bash
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


    
## Environment Variables

OPENAI_API_KEY=''



## 🏃‍♂️ Run Locally

```
bash
python app.py
```
This will redirect you to `http://localhost:8000` with a json string reading:
```json
{
  "message": "This is the home page of the LangChain Server!"
}
```
Go to the `http://localhost:8000/chain/playground` to load the LangServe interface

## API Reference

The API will be available at:
- API Documentation: http://localhost:8000/docs
- Translation Playground: http://localhost:8000/chain/playground

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker build -t langchain-translator .
docker run -p 8000:8000 --env-file .env langchain-translator
```

# 📝 API Usage

Make a POST request to `/chain/invoke` with the following JSON structure:
```json
{
"input": {
"target_language": "Spanish",
"text": "Hello, how are you?"
}
}
```


## 🌟 Features

- Text translation to any language
- Interactive API documentation
- Built-in playground interface
- Docker support
- Environment variable configuration
- Production-ready setup


## 📄 License

MIT License - feel free to use this project for your own learning and development!

## ⚠️ Important Notes

- Keep your `.env` file secure and never commit it to version control
- Consider implementing rate limiting for production use
- Add authentication for secure deployment


## Acknowledgements

### 👨‍🏫 Creator & Tutorial

This project was created following the excellent tutorial by **Jie Jenn**. 
- 📺 Tutorial: [Build a Language Translator using LangChain and FastAPI](https://www.youtube.com/watch?v=sBMsfDbrLXY)
- 🎥 YouTube Channel: [@jiejenn](https://www.youtube.com/@jiejenn)

Please show your support by subscribing to Jie Jenn's channel for more amazing tutorials!

