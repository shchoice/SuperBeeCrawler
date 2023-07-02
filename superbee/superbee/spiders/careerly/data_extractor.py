def get_data(driver):
    posts = driver.find_elements("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div")

    for post in posts:
        more_button = post.find_element("css selector", ".tw-text-slate-400.tw-cursor-pointer")
        more_button.click()