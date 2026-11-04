import os

import pytest
from dotenv import load_dotenv

from pages.todo_page import TodoPage

load_dotenv()

TASKS = ["to do 1", "to do 2", "to do 3"]


@pytest.fixture(scope="session")
def app_url() -> str:
    url = os.getenv("APP_URL")
    if not url:
        pytest.fail("APP_URL is not available")
    return url


@pytest.fixture
def tasks() -> list[str]:
    return list(TASKS)


@pytest.fixture
def todo_page(page, app_url) -> TodoPage:
    todo_page = TodoPage(page)
    todo_page.goto_app(app_url)
    return todo_page


@pytest.fixture
def todo_page_with_tasks(todo_page, tasks) -> TodoPage:
    todo_page.add_todos(tasks)
    return todo_page
