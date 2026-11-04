import re

from playwright.sync_api import expect


def test_add_todo(todo_page, tasks):
    todo_page.add_todos(tasks)

    expect(todo_page.todo_items).to_have_count(len(tasks))
    expect(todo_page.todo_items).to_have_text(tasks)
    expect(todo_page.todo_counter).to_have_text(
        re.compile(rf"^{len(tasks)} items? left")
    )
