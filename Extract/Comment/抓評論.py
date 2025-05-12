from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def 建立瀏覽器():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

def 抓取評論(driver, url):
    result = []
    seen = set()

    driver.get(url)
    time.sleep(2)

    try:
        more_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label,"更多評論")]'))
        )
        more_btn.click()
        time.sleep(2)
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        import traceback
        traceback.print_exc()

    # 點擊所有顯示更多
    expand_buttons = driver.find_elements(By.XPATH, '//button[contains(@aria-label,"顯示更多")]')
    for btn in expand_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except Exception as e:
            print(f"❌ 錯誤：{e}")
            import traceback
            traceback.print_exc()

    reviews = driver.find_elements(By.XPATH, '//div[@data-review-id]')
    for review in reviews:
        try:
            author = review.find_element(By.XPATH, './/div[contains(@class,"d4r55")]').text
            rating = review.find_element(By.XPATH, './/span[contains(@class,"kvMYJc")]').get_attribute("aria-label")
            try:
                text = review.find_element(By.XPATH, './/span[@jsname="bN97Pc"]').text
            except:
                text = review.find_element(By.XPATH, './/span[contains(@class,"wiI7pd")]').text

            key = (author, text.strip())
            if key in seen:
                continue
            seen.add(key)

            result.append({
                "author": author,
                "rating": rating,
                "text": text.strip()
            })
        except Exception as e:
            print(f"❌ 錯誤：{e}")
            import traceback
            traceback.print_exc()

    return result
