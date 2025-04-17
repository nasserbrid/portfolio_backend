# Utiliser une image Python officielle légère
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt pour installer les dépendances
COPY requirements.txt .

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source dans le conteneur
COPY . .

# Exposer le port 8000 pour que l'application soit accessible
EXPOSE 8000

# Utiliser gunicorn pour exécuter l'application Django via WSGI
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolioapi.wsgi:application"]
