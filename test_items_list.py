# This program will open up a website, check the name (to ensure it is correct for the test),
# then tests the items list in Test 5
# Author: Zach Walker

# Imports all the required packages
import re
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def test_get_page(page: Page):
    page.goto("https://group-9-webapp-official.vercel.app/testing")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Testing"))


def test_items_list(page: Page):
    # Click the input box.
    page.locator('#test5-input').click()

    # Create item variables
    item1 = 'Chicken Sandwich'
    item2 = 'Steak'
    item3 = 'Hamburger'

    # Type item 1 in the input box.
    page.locator('#test5-input').fill(item1)

    # Click the input box.
    page.locator('#test5-button').click()

    # Check input box data is equivalent to output
    expect(page.locator('#list-contents')).to_have_text(item1)

    # Type item 2 in the input box.
    page.locator('#test5-input').fill(item2)

    # Click the input box.
    page.locator('#test5-button').click()

    # Check input box data is equivalent to output
    expected_string = item1 + ',' + item2
    expect(page.locator('#list-contents')).to_have_text(expected_string)

    # Type item 3 in the input box.
    page.locator('#test5-input').fill(item3)

    # Click the input box.
    page.locator('#test5-button').click()

    # Check input box data is equivalent to output
    expected_string += ',' + item3
    expect(page.locator('#list-contents')).to_have_text(expected_string)
