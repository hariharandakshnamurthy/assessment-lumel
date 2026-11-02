import os
from dotenv import load_dotenv

from pages.todo_page import TodoPage
from playwright.sync_api import Page

load_dotenv()

URL = os.getenv("APP_URL")

TASKS = ['to do 1','to do 2', 'to do 3']  

# todo: need to migrate test data in seperate file


def test_mark_completed(page: Page):
    todo_page = TodoPage(page)
    
    todo_page.goto_app(URL)
    todo_page.app_loaded()
    
    todo_page.add_todo_list(TASKS)
    todo_page.get_todo_count()
    todo_page.clear_completed()
    todo_page.get_todo_count()

    todo_page.mark_completed()
