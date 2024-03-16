from selene import have

from demoqa_tests.application import app
from demoqa_tests.data import users


def test_simple_registration_form():
    user = users.admin

    app.left_panel.open_simple_registration_form()
    app.simple_registration.fill_full_name(f'{user.first_name} {user.last_name}')
    app.simple_registration.fill_email(user.email)
    app.simple_registration.fill_current_address(user.current_address)
    app.simple_registration.fill_permanent_address(user.permanent_address)
    app.simple_registration.submit_form()

    app.simple_registration.output.should(have.texts(
        f'{user.first_name} {user.last_name}',
        user.email,
        user.current_address,
        user.permanent_address
    )
    )
