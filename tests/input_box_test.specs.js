// @ts-check
import { test, expect } from '@playwright/test';

def test_get_page(page: Page):
    await page.goto("https://group-9-webapp-official.vercel.app/testing")

    // Expect a title "to contain" a substring.
    await expect(page).to_have_title(re.compile("Testing"))

def test_validation(page: Page):
    await page.locator('#test1-input').click()

    // Click the input box.
    await page.get_by_role("link", name="Get started").click()

    // Type in the input box.
    input_data = 'hamburger'
    await page.locator('#test1-input').fill(input_data)

    // Check input box data is equivalent to output
    await expect(page.locator('#test1-output')).toHaveText(input_data)

