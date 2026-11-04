from playwright.sync_api import Page, Locator


class TodoPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.app_title = page.get_by_role("heading", name="Todos", level=1)
        self.input_field = page.get_by_placeholder("What needs to be done?")
        self.footer_area = page.locator(".info").first
        self.todo_counter = page.locator(".todo-count")
        self.todo_items = page.locator(".todo-list li")
        self.toggle_all_chkbx = (
            page.locator("div")
            .filter(has_text="Toggle All Input")
            .get_by_role("checkbox")
        )
        self.clear_btn = page.get_by_role("button", name="Clear completed")
        self.filter_all_link = page.get_by_role("link", name="All")
        self.filter_active_link = page.get_by_role("link", name="Active")
        self.filter_completed_link = page.get_by_role("link", name="Completed")

    def goto_app(self, url: str) -> None:
        self.page.goto(url)

    def item(self, task: str) -> Locator:
        return self.todo_items.filter(has_text=task)

    def add_todo(self, task: str) -> None:
        self.input_field.fill(task)
        self.input_field.press("Enter")

    def add_todos(self, tasks: list[str]) -> None:
        for task in tasks:
            self.add_todo(task)

    def complete(self, task: str) -> None:
        self.item(task).get_by_role("checkbox").check()

    def delete(self, task: str) -> None:
        row = self.item(task)
        row.hover()
        row.get_by_role("button", name="Delete todo").click()

    def toggle_all(self) -> None:
        self.toggle_all_chkbx.click()

    def clear_completed(self) -> None:
        self.clear_btn.click()

    def switch_to_all(self) -> None:
        self.filter_all_link.click()

    def switch_to_active(self) -> None:
        self.filter_active_link.click()

    def switch_to_completed(self) -> None:
        self.filter_completed_link.click()
