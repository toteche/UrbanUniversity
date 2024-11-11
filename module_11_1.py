# тест библиотеки requests

import requests

def get_website_data(url):

	try:
		response = requests.get(url)
		response.raise_for_status()

		print(response.text)

	except requests.exceptions.RequestException as e:
		print(f'Ошибка при запросе к {url}: {e}')

if __name__ == "__main__":
	url = input('Введите URL сайта: ')
	get_website_data(url)


# тест библиотеки numpy
import numpy as np

# создание массива чисел
arr = np.array([1, 2, 3, 4, 5])
print('Исходный массив:\n ', arr)

# математические операции
arr_sum = arr + 2
print('\nСложение с 2:\n', arr_sum)
arr_sub = arr - 1
print('\nВычитание 1:\n', arr_sub)
arr_mul = arr * 3
print('\nУмножение на 3:\n', arr_mul)
arr_div = arr / 2
print('\nДеление на 2:\n', arr_div)


# библиотека pillow
from PIL import Image, ImageFilter, ImageEnhance

def process_image(image_path, output_path):

	try:
		img = Image.open(image_path)
		print(f'Исходный размер: {img.size}')

		# Изменяем размер
		new_size = (img.width // 2, img.height // 2)
		resized_img = img.resize(new_size, Image.LANCZOS)
		print(f'Новый размер: {resized_img.size}')

		# Размытие
		blurred_img = resized_img.filter(ImageFilter.BLUR)

		# Увеличение контраста
		enhancer = ImageEnhance.Contrast(blurred_img)
		enhanced_img = enhancer.enhance(1.5)

		# Сохраняем в PNG
		enhanced_img.save(output_path, "PNG")
		print(f'Изображение сохранено в {output_path}')

	except FileNotFoundError:
		print(f'Ошибка: файл {image_path} не найден.')
	except Exception as e:
		print(f'Произошла ошибка: {e}')

if __name__ == "__main__":
	image_path = input('Введите путь к изображению: ')
	output_path = input('Путь для сохранения изображения: ')
	process_image(image_path, output_path)

