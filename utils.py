import os
import psycopg2
from flask import g
from langchain_groq import ChatGroq
from config import get_packing_list_prompt
import json
from dotenv import load_dotenv
load_dotenv()

# Load Grok API key from environment variable
groq_api_key = os.environ.get('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

# Initialize Grok model
chat = ChatGroq(
    temperature=0,  # Low temperature for consistent, predictable output
    groq_api_key=groq_api_key,
    model_name="mixtral-8x7b-32768"
)

# Database connection parameters (optional)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'packing_list_db')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_db():
    """Connect to PostgreSQL database if credentials are provided."""
    if not DB_USER or not DB_PASSWORD:
        return None
    if 'db' not in g:
        conn_str = f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"
        g.db = psycopg2.connect(conn_str)
    return g.db

def close_db(e=None):
    """Close database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize database with packing_lists table."""
    db = get_db()
    if db:
        with db:
            with db.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS packing_lists (
                        list_id SERIAL PRIMARY KEY,
                        trip_type VARCHAR(50),
                        duration VARCHAR(20),
                        weather VARCHAR(50),
                        packing_list JSONB,
                        timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

def generate_packing_list(trip_type, duration, weather):
    """Generate a packing list using LangChain-Grok."""
    prompt = get_packing_list_prompt()
    chain = prompt | chat
    
    # Invoke the chain with input variables
    response = chain.invoke({
        "trip_type": trip_type,
        "duration": duration,
        "weather": weather
    })
    
    # Extract and parse the response content
    result = response.content.strip()
    try:
        packing_list = json.loads(result)
    except json.JSONDecodeError:
        raise ValueError("Failed to parse Grok response as JSON")
    
    # Optionally log to database
    db = get_db()
    if db:
        with db:
            with db.cursor() as cur:
                cur.execute('''
                    INSERT INTO packing_lists (trip_type, duration, weather, packing_list)
                    VALUES (%s, %s, %s, %s)
                ''', (trip_type, duration, weather, json.dumps(packing_list)))
    
    return packing_list

def get_packing_history():
    """Retrieve past packing lists (optional feature)."""
    db = get_db()
    if not db:
        return []
    with db:
        with db.cursor() as cur:
            cur.execute('SELECT trip_type, duration, weather, packing_list FROM packing_lists ORDER BY timestamp DESC')
            return cur.fetchall()