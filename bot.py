from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as wait # waits in seconds
import numpy as np

# Define the form url and the number of answers :)

form_url = "https://forms.gle/XXXXXXXXXXXXXX"
answers_count = 100

# this function will click on a random choice from the list of inputs
# it's easy to add weights to the choices if needed
def answer(driver, inputs):
    choice = np.random.choice(inputs)
    driver.find_element(By.XPATH, choice).click()


def bot():
    driver = webdriver.Chrome()

    driver.get(form_url)

    # For each question, add the list of XPATHs of the options
    # answer(driver, [
    #     '//*[@id="i5"]',
    #     '//*[@id="i8"]',
    #     '//*[@id="i11"]',
    #     '//*[@id="i14"]',
    #     '//*[@id="i17"]',
    # ])

    # click on the submit button
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()

    wait(0.1)

if __name__ == "__main__":
    print("Bot is running...")
    for i in range(answers_count)
        bot()
    print("Done!! >))))))")
