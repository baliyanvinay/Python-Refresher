# Super function in python allows to access parent class attributes
# Super is extremely useful with OOP and inheritance and follow DRY principle

class BaseAccess(object):
    def __init__(self):
        self.root_access = True

    def is_authorized(self, some_value=10):
        print(f'Authorized with {some_value}')


class MainFormPage(BaseAccess):
    def __init__(self):
        # This will call the BaseAccess constructor
        super().__init__()

    def display_info(self):
        some_value = 15
        # We can also overload the parent class method using Super()
        super().is_authorized(some_value)
        print('Viewing something because Authorized')


# Instance of MainFormPage will have access to BaseAccess methods and attributes
page_link = MainFormPage()
print(page_link.root_access)
page_link.display_info()


# Workflow of Super with muti-level inheritance
class MainFormContent(MainFormPage):
    def display_content(self):
        print('Some static content')
        super().display_info()


content_link = MainFormContent()
content_link.display_content()

# Note in case of multiple inheritance the inheritance order resolution from right to left will work
