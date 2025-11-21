import flet as ft
from db import main_db

def main(page:ft.Page):
    page.title ='Список покупок'
    page.theme_mode = ft.ThemeMode.DARK

    task_list = ft.Column(spacing=10)

    filter_type ='all'

    def load_task():
        task_list.controls.clear()
        for task_id, task_text , purchased in main_db.get_tasks(filter_type):
            task_list.controls.append(create_task_row(task_id=task_id , task_text=task_text , purchased=purchased))
        page.update()


    def create_task_row(task_id , task_text , purchased):
        task_field = ft.TextField(value=task_text, expand=True , read_only=True)

        checkbox_task = ft.Checkbox(value=bool(purchased) , on_change=lambda e: toogle_task(task_id , e.control.value))

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(_):
            main_db.update_task(task_id=task_id , new_task=task_field.value)
            task_field.read_only =True
            task_field.update()
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE , on_click=save_task)

        return ft.Row([checkbox_task , task_field , edit_button , save_button])
        

    def toogle_task(task_id , is_purchased):
        main_db.update_task(task_id=task_id , purchased = int(is_purchased))
        load_task()


    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            print(task_id)
            task_list.controls.append(create_task_row(task_id=task_id , task_text=task , purchased=None))
            task_input.value = None
            page.update()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_task()


    filter_buttons = ft.Row([
        ft.ElevatedButton('Все', icon = ft.Icons.ALL_INBOX , on_click=lambda e: set_filter("all")),
        ft.ElevatedButton('Некупленные' , icon = ft.Icons.STOP_OUTLINED , on_click=lambda e: set_filter("unpurchased") , color=ft.Colors.YELLOW_700),
        ft.ElevatedButton('Купленные' , icon = ft.Icons.STOP_OUTLINED , on_click=lambda e: set_filter("purchased") , color=ft.Colors.GREEN_700)
    ],alignment = ft.MainAxisAlignment.SPACE_AROUND)

    task_input = ft.TextField(label='Введите продукт' , expand=True , on_submit=add_task)
    task_button = ft.TextButton(text='send', icon =ft.Icons.SEND_ROUNDED , on_click=add_task)

    page.add(ft.Row([task_input , task_button]),filter_buttons, task_list)
    load_task()
    

if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)

    
