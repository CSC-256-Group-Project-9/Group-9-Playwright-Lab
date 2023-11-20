# This program will open up a website, check the name (to ensure it is correct for the test), then tests the input box
# in Test 1
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
    # Click the input box.
    page.locator('#test1-input').click()

    # Type in the input box.
    input_data = 'hamburger'
    page.locator('#test1-input').fill(input_data)

    # Check input box data is equivalent to output
    expect(page.locator('#test1-output')).to_have_text(input_data)
