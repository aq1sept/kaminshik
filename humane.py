import pyautogui
import cv2
import time
import random
import os

def find_and_click(image_path, confidence=0.75):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл изображения не найден: {image_path}")

        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        if image is None:
            raise ValueError(f"Ошибка загрузки изображения: {image_path}")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = pyautogui.locateOnScreen(gray, confidence=confidence)

        if result:
            move_and_click(result)
            print(f"Кликнуто на {image_path} по координатам: {get_center_coordinates(result)}")
            return True  # Изображение найдено
        else:
            #print(f"{image_path} не найдено")
            return False  # Изображение не найдено

    except Exception as e:
        print(f"Ошибка при обработке {image_path}: {e}")
        return False  # Произошла ошибка

def move_and_click(result):
    x, y, _, _ = result
    center_x = x + _ // 2
    center_y = y + _ // 2

    offset_x = random.uniform(-5, 5)
    offset_y = random.uniform(-5, 5)
    pyautogui.moveTo(center_x + offset_x, center_y + offset_y, duration=0.5)
    pyautogui.click()


def get_center_coordinates(result):
    x, y, _, _ = result
    center_x = x + _ // 2
    center_y = y + _ // 2
    return center_x, center_y

def main():
    image_paths = ['images/big0.png', 'images/big32.png', 'images/big64.png', 'images/big96.png', 'images/big128.png', 'images/big160.png', 'images/big192.png', 'images/big224.png', 'images/big255.png']

    try:
        while True:
            for image_path in image_paths:
                if not find_and_click(image_path):
                    continue  # Перейти к следующему изображению, если текущее не найдено

                random_sleep = random.uniform(0.85, 1.3)
                print(f"Сон на {random_sleep:.2f} секунды...")
                time.sleep(random_sleep)
                pyautogui.click()
                time.sleep(random_sleep)
                pyautogui.click()

    except KeyboardInterrupt:
        print("\nСкрипт прерван пользователем.")
    finally:
        input("Нажмите Enter для выхода...")

if __name__ == "__main__":
    main()