import sqlite3

DB_NAME = "data/database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        image_path TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_all_notes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")

    notes = cursor.fetchall()

    conn.close()

    return notes

def update_note(note_id, title, content):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE notes
    SET title=?, content=?
    WHERE id=?
    """, (
        title,
        content,
        note_id
    ))

    conn.commit()
    conn.close()

def delete_note(note_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM notes
    WHERE id=?
    """, (
        note_id,
    ))

    conn.commit()
    conn.close()

def get_all_questions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quiz")

    questions = cursor.fetchall()

    conn.close()

    return questions

def delete_question(question_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM quiz
    WHERE id=?
    """, (
        question_id,
    ))

    conn.commit()
    conn.close()