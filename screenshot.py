import pyautogui


def test_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("/Users/loc6-mac05/Documents/Python_Test/insta.png")


if __name__ == "__main__":
    test_screenshot()
