from selenium.webdriver.chrome.options import Options


def chrome_driver_configuration() -> Options:
    """
    Configures Chrome WebDriver options for Selenium.

    This scrapers method creates a set of options that can be passed to the Chrome WebDriver
    when creating an instance of it. These options modify the behavior of the Chrome browser
    during automated testing or scraping.

    Returns:
        Options: A configured ChromeOptions instance to be used with Chrome WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    chrome_options.add_argument(
        "--enable-features=NetworkService,NetworkServiceInProcess"
    )
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options
