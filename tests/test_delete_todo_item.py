import os
from dotenv import load_dotenv

from pages.todo_page import TodoPage
from playwright.sync_api import Page

load_dotenv()

task = 'todo_task'
URL = os.getenv("APP_URL")

def test_delete_todo_item(page:Page):
    todo_page = TodoPage(page)
    todo_page.goto_app(URL)
    todo_page.app_loaded()

    todo_page.create_item(task)
    todo_page.delete_todo_item(task)
