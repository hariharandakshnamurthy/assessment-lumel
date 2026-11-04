from playwright.sync_api import expect


def test_filter_items(todo_page_with_tasks, tasks):
    todo_page = todo_page_with_tasks
    done, active = tasks[0], tasks[1:]

    todo_page.complete(done)

    todo_page.switch_to_active()
    expect(todo_page.todo_items).to_have_text(active)
    expect(todo_page.item(done)).to_have_count(0)

    todo_page.switch_to_completed()
    expect(todo_page.todo_items).to_have_text([done])
    for task in active:
        expect(todo_page.item(task)).to_have_count(0)

    todo_page.switch_to_all()
    expect(todo_page.todo_items).to_have_text(tasks)
