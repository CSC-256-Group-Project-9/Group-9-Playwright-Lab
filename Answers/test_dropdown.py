# This program will open up a website, check the name (to ensure it is correct for the test),
# then tests the dropdown in Test 6
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


def test_dropdown(page: Page):
    # Select Epps from dropdown
    page.locator('#student').select_option('Epps')

    # Clicks the Test 6 Submit button
    page.locator('#test6-button').click()

    # Checks if output value has the correct person
    expect(page.locator('#ddcontent')).to_have_text('Epps')


def test_dropdown_change(page: Page):
    # Clicks the Test 6 Submit button
    page.locator('#test6-button').click()

    # Checks if output value has the correct person (Default Branch)
    expect(page.locator('#ddcontent')).to_have_text('Branch')

    # Select West from dropdown
    page.locator('#student').select_option('West')

    # Clicks the Test 6 Submit button
    page.locator('#test6-button').click()

    # Checks if output value updated with the correct person
    expect(page.locator('#ddcontent')).to_have_text('West')
