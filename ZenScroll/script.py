from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser and open Shorts
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/shorts")

# Let the page load
time.sleep(5)

try:
    while True:
        # ⏳ Wait a few seconds to ensure the new video loads
        time.sleep(2)

        #  Re-fetch the <video> element (very important!)
        video = driver.find_element(By.TAG_NAME, "video")

        #  Wait until the video ends
        while True:
            current_time = driver.execute_script("return arguments[0].currentTime;", video)
            duration = driver.execute_script("return arguments[0].duration;", video)

            #  If the video is about to end
            if duration - current_time <= 0.5:
                break
            time.sleep(1)

        #  Scroll to next Short
        print("Video ended. Scrolling to next Short...")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)

except KeyboardInterrupt:
    print("Script stopped.")
    driver.quit()
