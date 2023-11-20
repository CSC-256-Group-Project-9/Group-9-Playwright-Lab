# This program will open up a website, check the name (to ensure it is correct for the test),
# then tests the radio button in Test 4
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


def test_radio_button_java(page: Page):
    # Clicks the Java radio button
    page.locator('#java').click()

    # Check to see if the Java radio button is selected
    expect(page.locator('#java')).to_be_checked()

    # Clicks the Test 4 Submit button
    page.locator('#test4-button').click()

    # Checks if output value has the correct language
    expect(page.locator('#result')).to_have_text('Favorite Language: Java')


def test_radio_button_change(page: Page):
    # Clicks the Java radio button
    page.locator('#java').click()

    # Check to see if the Java radio button is selected
    expect(page.locator('#java')).to_be_checked()

    # Clicks the Python radio button
    page.locator('#python').click()

    # Check to see if the Python radio button is selected
    expect(page.locator('#python')).to_be_checked()

    # Clicks the Test 4 Submit button
    page.locator('#test4-button').click()

    # Checks if output value has the correct language
    expect(page.locator('#result')).to_have_text('Favorite Language: Python')
