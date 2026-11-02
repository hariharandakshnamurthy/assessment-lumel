import os
import pytest
from dotenv import load_dotenv

from pages.todo_page import TodoPage
from playwright.sync_api import Page,sync_playwright

load_dotenv()

URL = os.getenv("APP_URL")

TASKS = ['to do 1','to do 2', 'to do 3']

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        context = p.chromium.launch()
        browser = context.new_context()
        return browser

@pytest.fixture(scope="function")
def create_todo_list(browser,page:Page):
        page = browser.new_page()

        todo_page = TodoPage(page)
            
        todo_page.goto_app(URL)
        todo_page.app_loaded()
            
        todo_page.add_todo_list(TASKS)


""""
    Due to Time constraint unable to configure fixture states for certain cases
"""

    