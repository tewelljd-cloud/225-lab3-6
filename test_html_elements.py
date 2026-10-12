from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest


class TestH5Tag(unittest.TestCase):
    def setUp(self):
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_h5_tag_content(self):
        driver = self.driver
        driver.get("http://10.48.229.237")  # Target website address

        # Locate the <h5> tag and get its text
        h5_text = driver.find_element(By.TAG_NAME, "h5").text

        # Verify the expected text
        self.assertEqual(
            "Lab 3-6 Works!",
            h5_text,
            "The <h5> tag does not contain the text 'Lab 3-6 Works!'"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
