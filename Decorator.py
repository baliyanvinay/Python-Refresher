# Decorators are function defined to enhance the functionality of an existing function or class
# Common use of decorators are with login_required in web frameworks

# Example of a simple decorator
def login_required(access_page):
    def access_check():
        # Checking access related stuff
        print('Authenticated User!')
        access_page()  # calling the original function
    return access_check


# Function to check if permissions are available
def permission_required(access_page):
    def persmission_check():
        # Checking the required permissions
        print('Permissions available!')
        access_page()
    return persmission_check


def user_profile():
    print('Username: myusername \nRole: SE')


user_profile()  # Direct function call

# In order to access profile page, user must be logged in.
user_profile = login_required(user_profile)
user_profile()


# A more common way to use decorators
@login_required
def user_account():
    print('Logged In as username with Role SE')


user_account()


# Example of multiple decorators
@login_required
@permission_required
def update_account():
    print('Account has been updated for SE')


update_account()


# Decorator with agruements
def member_permission(access_page):
    def member_check(agrs):
        if agrs.lower() in ('developer'):
            print(f'{agrs} is a member!')
        access_page(agrs)
    return member_check


@member_permission
def member_page(agrs):
    print('Welcome to the Developers Page')


member_page('Developer')
