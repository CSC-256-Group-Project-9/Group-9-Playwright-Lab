# Group-9-Playwright-Lab
A resource to guide students towards successfully completing the PlayWright lab.
## Getting Started:
- A quick review of understanding [PlayWright with a simple to follow example](Understanding_PlayWright.docx)
- Another great resource for understanding [PlayWright:](https://www.browserstack.com/guide/playwright-python-tutorial) and [another resource](https://www.youtube.com/watch?v=y8zY14HHiPI&list=PLP5_A7hnY1Tggph0F0cRqf5iyyZuIBXYC) as well as [this resource](https://playwright.dev/python/docs/writing-tests#first-test)
## Project Overview
-  The purpose of this project is to understand and use PlayWright.
- This repo shows a real-world example of using PlayWright to test some features that were in the mini projects issued in the Selenium lab such as using a radio button.
## Installation Guidelines:
- In order to use PlayWright in a **Python** coding environment
- you just need to:
`pip install playwright`
- Install components from specified browser that will communicate with playwright(Ex Google Chrome):
`playwright install chromium`
-Import playwright to file for usage:
`from playwright.sync_api import sync_playwright`
- Remember-- For a better understanding you can always Google and Youtube how to install playwright. There is also a guide that explains a little more specifically on how to install playwright listed above
 - Worst case: If that  doesn't work then try this [resource.](https://playwright.dev/docs/intro).
## Understanding This Repo:
- This lab uses playwright as well as pytest here is the [docs website for pytest for any troubles you may find:](https://docs.pytest.org/en/7.1.x/how-to/index.html)
- Each file tests a feature using playwright using file name "test..." you can find what is being tested by the "..." part
- `import re` -- allows you to do regular expression in python here is [a guide to regular experession](https://www.w3schools.com/python/python_regex.asp)
- **Remember:** If lost plase check links or work cited websites for additional help
## Additional Notes
 ### Works cited:

Shrivastva, Arjun M. “The Ultimate Playwright Python Tutorial.” Browserstack, 4 May 2023, https://www.browserstack.com/guide/playwright-python-tutorial. Accessed 26 Nov. 2023.

Playwright. “Installation.” Microsoft, https://playwright.dev/docs/intro. Accessed 26 Nov. 2023.

Playwright. “PlayWright.” Microsoft, https://github.com/microsoft/playwright-python. Accessed 26 Nov. 2023.

SimpliLearn. “Node.js Tutorial.” SimpliLearn, 11 Oct. 2023, https://www.simplilearn.com/tutorials/nodejs-tutorial. Accessed 26 Nov. 2023.


