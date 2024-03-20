# README.md
https://rest-apis-flask.teclado.com/

## Build da imagem
```docker build -t rest-apis-with-flask-and-python-in-2023 .```

## Rodando container
```docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --name rest-apis-with-flask-and-python-in-2023 rest-apis-with-flask-and-python-in-2023 sh -c "flask run --host 0.0.0.0"```