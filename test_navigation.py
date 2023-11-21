# This program will open the website and check every navigation link on every page
# Author: Owen Cawlfield

import re
from playwright.sync_api import Page, expect


def test_navigation_home(page: Page):
    # Starting at the Home page
    page.goto("https://group-9-webapp-official.vercel.app/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Home"))

    # testing the "Testing" link
    page.get_by_role("link", name="Testing").click()
    expect(page).to_have_title(re.compile("Testing"))
    # return to home page
    page.goto("https://group-9-webapp-official.vercel.app/")
    expect(page).to_have_title(re.compile("Home"))

    # Testing the "API" link
    page.get_by_role("link", name="API").click()
    expect(page).to_have_title(re.compile("API Endpoints"))
    # return to home page
    page.goto("https://group-9-webapp-official.vercel.app/")
    expect(page).to_have_title(re.compile("Home"))

    # Testing the "About Us" link
    page.get_by_role("link", name="About Us").click()
    expect(page).to_have_title(re.compile("About us"))
    # return to home page
    page.goto("https://group-9-webapp-official.vercel.app/")
    expect(page).to_have_title(re.compile("Home"))

    # Testing the "Contact Us" link
    page.get_by_role("link", name="Contact Us").click()
    expect(page).to_have_title(re.compile("Contact us"))
    # return to home page
    page.goto("https://group-9-webapp-official.vercel.app/")
    expect(page).to_have_title(re.compile("Home"))

    # Testing the "Home" link
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title(re.compile("Home"))


def test_navigation_testing(page: Page):
    # Starting at the Testing page
    page.goto("https://group-9-webapp-official.vercel.app/testing")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Testing"))

    # Testing the "Home" link
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title(re.compile("Home"))

    # back to "Testing" page
    page.goto("https://group-9-webapp-official.vercel.app/testing")
    expect(page).to_have_title(re.compile("Testing"))

    # Testing the "API" link
    page.get_by_role("link", name="API").click()
    expect(page).to_have_title(re.compile("API Endpoints"))

    # back to "Testing" page
    page.goto("https://group-9-webapp-official.vercel.app/testing")
    expect(page).to_have_title(re.compile("Testing"))

    # Testing the "About Us" link
    page.get_by_role("link", name="About Us").click()
    expect(page).to_have_title(re.compile("About us"))

    # back to "Testing" page
    page.goto("https://group-9-webapp-official.vercel.app/testing")
    expect(page).to_have_title(re.compile("Testing"))

    # Testing the "Contact Us" link
    page.get_by_role("link", name="Contact Us").click()
    expect(page).to_have_title(re.compile("Contact us"))


def test_navigation_api(page: Page):
    # Starting at the API Endpoints page
    page.goto("https://group-9-webapp-official.vercel.app/endpoints")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Testing the "Home" link
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title(re.compile("Home"))

    # back to API Endpoints page
    page.goto("https://group-9-webapp-official.vercel.app/endpoints")
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Testing the "Testing" link
    page.get_by_role("link", name="Testing").click()
    expect(page).to_have_title(re.compile("Testing"))

    # back to API Endpoints page
    page.goto("https://group-9-webapp-official.vercel.app/endpoints")
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Testing the "About Us" link
    page.get_by_role("link", name="About Us").click()
    expect(page).to_have_title(re.compile("About us"))

    # back to API Endpoints page
    page.goto("https://group-9-webapp-official.vercel.app/endpoints")
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Testing the "Contact Us" link
    page.get_by_role("link", name="Contact Us").click()
    expect(page).to_have_title(re.compile("Contact us"))


def test_navigation_about_us(page: Page):
    # Start at the "About Us" page
    page.goto("https://group-9-webapp-official.vercel.app/about_us")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("About us"))

    # Testing the "Home" link
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title(re.compile("Home"))

    # Start back to at the "About Us" page
    page.goto("https://group-9-webapp-official.vercel.app/about_us")
    expect(page).to_have_title(re.compile("About us"))

    # Testing the "Testing" link
    page.get_by_role("link", name="Testing").click()
    expect(page).to_have_title(re.compile("Testing"))

    # Start back to at the "About Us" page
    page.goto("https://group-9-webapp-official.vercel.app/about_us")
    expect(page).to_have_title(re.compile("About us"))

    # Testing the "API" link
    page.get_by_role("link", name="API").click()
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Start back to at the "About Us" page
    page.goto("https://group-9-webapp-official.vercel.app/about_us")
    expect(page).to_have_title(re.compile("About us"))

    # Testing the "Contact Us" link
    page.get_by_role("link", name="Contact Us").click()
    expect(page).to_have_title(re.compile("Contact us"))


def test_navigation_contact_us(page: Page):
    # Start at the "Contact Us" page
    page.goto("https://group-9-webapp-official.vercel.app/contact")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Contact us"))

    # Testing the "Home" link
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_title(re.compile("Home"))

    # Start back at the "Contact Us" page
    page.goto("https://group-9-webapp-official.vercel.app/contact")
    expect(page).to_have_title(re.compile("Contact us"))

    # Testing the "Testing" link
    page.get_by_role("link", name="Testing").click()
    expect(page).to_have_title(re.compile("Testing"))

    # Start back at the "Contact Us" page
    page.goto("https://group-9-webapp-official.vercel.app/contact")
    expect(page).to_have_title(re.compile("Contact us"))

    # Testing the "API" link
    page.get_by_role("link", name="API").click()
    expect(page).to_have_title(re.compile("API Endpoints"))

    # Start back at the "Contact Us" page
    page.goto("https://group-9-webapp-official.vercel.app/contact")
    expect(page).to_have_title(re.compile("Contact us"))

    # Testing the "About Us" link
    page.get_by_role("link", name="About Us").click()
    expect(page).to_have_title(re.compile("About us"))

