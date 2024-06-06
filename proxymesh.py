from selenium.webdriver.chrome.options import Options

def get_driver_with_proxy(proxy_url):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy_url}')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Example usage:
proxy_url = "http://your_proxymesh_proxy:port"
driver = get_driver_with_proxy(proxy_url)
