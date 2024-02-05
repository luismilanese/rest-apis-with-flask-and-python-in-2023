# README.md
https://rest-apis-flask.teclado.com/

## Build da imagem
```docker build -t rest-apis-with-flask-and-python-in-2023 .```

## Rodando container
```docker run -p 5000:5000 -w /app -v "$(pwd):/app" rest-apis-with-flask-and-python-in-2023```