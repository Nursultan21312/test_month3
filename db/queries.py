import sqlite3 
CREATE_TASK = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        task TEXT NOT NULL,
        purchased INTEGER DEFAULT 0
    )
"""

INSERT_TASK = 'INSERT INTO tasks (task) VALUES (?)'

SELECT_TASK = 'SELECT id, task, purchased FROM tasks'

SELECT_TASK_PURCHASED = 'SELECT id, task, purchased FROM tasks WHERE purchased = 1'

SELECT_TASK_UNPURCHASED = 'SELECT id, task, purchased FROM tasks WHERE purchased = 0'

UPDATE_TASK = 'UPDATE tasks SET task = ? WHERE id = ?'

DELETE_TASK = 'DELETE FROM tasks WHERE id = ?'


