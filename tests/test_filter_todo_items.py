import os
from dotenv import load_dotenv

from pages.todo_page import TodoPage
from playwright.sync_api import Page,expect

load_dotenv()

URL = os.getenv("APP_URL")

TASKS = ['to do 1','to do 2']


def test_filter_items(page: Page):
    todo_page = TodoPage(page)
    todo_page.goto_app(URL)
    todo_page.app_loaded()

    for task in TASKS:
        todo_page.create_item(task)   
    todo_page.switch_to_active()
    expect(page.get_by_text(TASKS[1])).to_be_visible
    items_count = todo_page.get_todo_count()
    print(items_count)
    assert items_count == len(TASKS), "active items count doesn't match"

    todo_page.toggle_all_btn.click()
    todo_page.switch_to_completed()

    for task in TASKS:
        item_counts = todo_page.completed_list.get_by_text(task).count()
    assert items_count == len(TASKS)
    items_count = todo_page.get_todo_count()
    assert items_count == 0, "failed to mark some list item as completed"


