from playwright.sync_api import Page,expect


class TodoPage:
    def __init__(self,page: Page) -> None:
        self.page = page
        self.app_title = page.get_by_role('heading',name="Todos",level=1)
        self.input_field = page.get_by_placeholder("What needs to be done?")
        self.footer_area = page.locator('.info').first
        self.todo_counter = page.locator(".todo-count")
        self.todo_chkbx = page.locator("app-todo-item").get_by_role("checkbox")
        self.todo_list = page.locator(".todo-list")
        self.toggle_all_btn = page.locator("div").filter(has_text="Toggle All Input").get_by_role("checkbox")
        self.clear_btn = page.get_by_role("button", name="Clear completed")
        self.delete_btn = page.get_by_role("button", name="Delete todo")
        self.filter_all_link = page.get_by_role("link",name="All")
        self.filter_compltd_link = page.get_by_role("link",name="Completed")
        self.filter_active_link = page.get_by_role("link",name="Active")
        self.completed_list = page.locator(".completed").locator("div[class='view'] label")

    def goto_app(self,url):
        self.page.goto(url)

    def app_loaded(self):
        expect(self.app_title).to_be_visible()
        expect(self.input_field).to_be_visible()
        expect(self.input_field).to_be_focused()
        expect(self.footer_area).to_be_visible()

    def add_todo_list(self,TASKS):
        for task in TASKS:
            self.input_field.fill(task)
            self.page.keyboard.press("Enter")
            expect(self.page.get_by_text(task)).to_be_visible()
        todo_count = self.get_todo_count()   
        assert todo_count == len(TASKS)    

    def get_todo_count(self):
        todo_counter = self.todo_counter.text_content()
        todo_count_num = todo_counter.split()[0]
        return int(todo_count_num)

    def clear_completed(self):
        self.toggle_all_btn.click()
        self.clear_btn.click()

    def mark_completed(self):
        self.input_field.fill('task to mark')
        self.page.keyboard.press("Enter")
        expect(self.todo_chkbx.first).to_be_visible()
        todo_count = self.get_todo_count()
        self.todo_chkbx.first.click()
        assert todo_count == 0, "completed count doesn't match"

    def create_item(self,task):
        self.input_field.fill(task)
        self.page.keyboard.press("Enter")
        expect(self.todo_chkbx.first).to_be_visible()

    def delete_todo_item(self,task):
        added_task = self.page.get_by_text(task)
        added_task.hover()
        self.delete_btn.click()
        expect(added_task).not_to_be_visible()

    def switch_to_active(self):
        self.filter_active_link.click()

    def switch_to_completed(self):
        self.filter_compltd_link.click()
        




        



        

    

    

    