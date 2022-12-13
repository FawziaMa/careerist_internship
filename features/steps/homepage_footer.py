from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('User is on homepage')
def open_product_page(context):
    context.app.homepage.open_main()


@when('User scrolls down to footer')
def scroll_to_footer(context):
    context.app.homepage.scroll_to_footer()


@when('Clicks "Terms of Service"')
def click_terms_of_service(context):
    context.app.homepage.click_terms_of_service()


@then('Verify {expected_title} page opened')
def verify_terms_page(context, expected_title,):
    context.homepage.verify_terms_page(expected_title)
    # assert actual_results == expected_title

    sleep(5)