# image Python officielle légère
FROM python:3.12-slim

# répertoire de travail dans le conteneur
WORKDIR /app

# fichiers requirements.txt pour installer les dépendances
COPY requirements.txt .

# dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le code source dans le conteneur
COPY . .

# Expose le port 8000 pour que l'application soit accessible
EXPOSE 8000

# Utilisation de gunicorn pour exécuter l'application Django via WSGI
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolioapi.wsgi:application"]
