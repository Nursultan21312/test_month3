import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TASK)
    print('база данных подключена')
    conn.commit()
    conn.close()
    

def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def get_tasks(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASK)

    if filter_type =='purchased':
        cursor.execute(queries.SELECT_TASK_PURCHASED)
    elif filter_type =='unpurchased':
        cursor.execute(queries.SELECT_TASK_UNPURCHASED)
    else:
        cursor.execute(queries.SELECT_TASK)


    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task(task_id , new_task=None , purchased=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if new_task is not None:
        cursor.execute(queries.UPDATE_TASK,(new_task, task_id))
    if purchased is not None:
        cursor.execute("UPDATE tasks SET purchased =? WHERE id = ?" , (purchased , task_id))
        
    conn.commit()
    conn.close()    


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id, ))
    conn.commit()
    conn.close()

    