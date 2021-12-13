from typing import Union

from selenium import webdriver

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class RefreshableDriver:
    def __init__(self, url: str, flavour: Literal["chrome", "firefox"]):
        self.url = url
        self.driver = get_driver(flavour)

    def reload(self):
        self.driver.refresh()

    def load(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


def get_driver(flavour: str) -> Union[webdriver.Firefox, webdriver.Chrome]:
    if flavour == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        return webdriver.Firefox(executable_path="geckodriver", firefox_profile=profile)
    elif flavour == "chrome":
        return webdriver.Chrome(executable_path="chromedriver")
