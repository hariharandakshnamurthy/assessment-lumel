import os
from dotenv import load_dotenv

from pages.todo_page import TodoPage
from playwright.sync_api import Page

load_dotenv()

URL = os.getenv("APP_URL")

TASKS = ['to do 1','to do 2', 'to do 3']

# Verify if the item is added to the list

def test_add_todo(page:Page):
    todo_page = TodoPage(page)

    todo_page.goto_app(URL)
    todo_page.app_loaded()

    todo_page.add_todo_list(TASKS)
    todo_page.get_todo_count()