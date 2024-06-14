
import psycopg2

try:
    connection = psycopg2.connect(
        host='postgres',
        user='user',
        password='password',
        database='job_scraper'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT 1')
    print('Connection successful!')
    cursor.close()
    connection.close()
except Exception as e:
    print(f'Connection failed: {e}')

