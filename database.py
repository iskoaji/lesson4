import sqlite3

DB_PATH = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_text TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_task(user_id, task_text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_id, task_text) VALUES (?, ?)", (user_id, task_text))
    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, task_text FROM tasks WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def clear_tasks(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
