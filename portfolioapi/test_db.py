import psycopg2
import dj_database_url

# URL de la base de données
DATABASE_URL = "postgresql://portfolio_bdd_x8hx_user:5iK0qK18dCfSYtRD7mMLDn0el3j8Zi6v@dpg-d0greojuibrs73ftdr70-a.oregon-postgres.render.com/portfolio_bdd_x8hx"

# Test 1: Vérifier que dj-database-url fonctionne
try:
    print("Test 1: Vérification de dj-database-url")
    config = dj_database_url.parse(DATABASE_URL)
    print(f"Configuration générée: {config}")
    print("Test 1: Réussi ✅")
except Exception as e:
    print(f"Test 1: Échec ❌ - {e}")

# Test 2: Vérifier la connexion directe à PostgreSQL
try:
    print("\nTest 2: Connexion directe à PostgreSQL")
    # Extraire les informations de connexion
    db_config = dj_database_url.parse(DATABASE_URL)
    
    # Se connecter à la base de données
    conn = psycopg2.connect(
        dbname=db_config['NAME'],
        user=db_config['USER'],
        password=db_config['PASSWORD'],
        host=db_config['HOST'],
        port=db_config.get('PORT', 5432)
    )
    
    # Test simple
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    
    print(f"Résultat de la requête: {result}")
    cursor.close()
    conn.close()
    print("Test 2: Réussi ✅ - Connexion établie avec succès")
except Exception as e:
    print(f"Test 2: Échec ❌ - {e}")