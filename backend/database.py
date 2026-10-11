
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "students.db"


def initialize_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                topic TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                percentage REAL NOT NULL,
                recommendation TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_attempt(name, topic, score, total, percentage, recommendation):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            INSERT INTO quiz_attempts
            (student_name, topic, score, total, percentage, recommendation)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name, topic, score, total, percentage, recommendation
        ))
      
