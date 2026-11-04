import re

from playwright.sync_api import expect


def test_mark_completed(todo_page_with_tasks, tasks):
    todo_page = todo_page_with_tasks
    target, others = tasks[0], tasks[1:]

    todo_page.complete(target)

    expect(todo_page.item(target)).to_have_class(re.compile(r"\bcompleted\b"))

    for task in others:
        expect(todo_page.item(task)).not_to_have_class(re.compile(r"\bcompleted\b"))

    expect(todo_page.todo_counter).to_have_text(
        re.compile(rf"^{len(others)} items? left")
    )
