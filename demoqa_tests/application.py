from demoqa_tests.pages.left_panel import LeftPanel
from demoqa_tests.pages.registration_form import RegistrationForm


class ApplicationManager:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.registration = RegistrationForm()


app = ApplicationManager()
