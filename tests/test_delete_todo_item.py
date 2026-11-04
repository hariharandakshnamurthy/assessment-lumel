import re

from playwright.sync_api import expect


def test_delete_todo_item(todo_page_with_tasks, tasks):
    todo_page = todo_page_with_tasks
    removed, remaining = tasks[0], tasks[1:]

    todo_page.delete(removed)

    expect(todo_page.item(removed)).to_have_count(0)
    expect(todo_page.todo_items).to_have_text(remaining)
    expect(todo_page.todo_counter).to_have_text(
        re.compile(rf"^{len(remaining)} items? left")
    )
