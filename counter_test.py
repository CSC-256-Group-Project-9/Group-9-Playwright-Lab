# This program will open up a website, check the name (to ensure it is correct for the test), then tests the counter
# in Test 2
# Author: David Smedberg

# Imports all the required packages
import re, pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def test_get_page(page: Page):
    page.goto("https://group-9-webapp-official.vercel.app/testing")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Testing"))

def test_validation(page: Page):
    # Checks if default value is zero
    expect(page.locator('#test2-output')).to_have_text('0')

    # Clicks the counter button
    page.locator('#test2-button').click()

    # Checks if output value changed (expected value is 1)
    expect(page.locator('#test2-output')).to_have_text('1')

    # Clicks the button twice more
    page.locator('#test2-button').click()
    page.locator('#test2-button').click()

    # Checks if the output value matches the expected value (expected value is 3 now)
    expect(page.locator('#test2-output')).to_have_text('3')
