import time
from multiprocessing import Pool

def read_info(file_name):
	all_data = []
	with open(file_name, 'r') as file:
		line = file.readline()
		while line:
			all_data.append(line.strip())
			line = file.readline()
	return

if __name__ == '__main__':
	# Список файлов
	file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

	# #Линейный подход
	# start_time = time.time()
	# for file_name in file_names:
	# 	read_info(file_name)
	# linear_time = time.time() - start_time
	# print(f'Линейный подход занял: {linear_time:.2f} секунд')

	#Многопроцессорный подход
	start_time = time.time()
	with Pool() as pool:
		pool.map(read_info, file_names)
	multiprocess_time = time.time() - start_time
	print(f'Мультипроцессорный подход занял: {multiprocess_time:.2f} секунд')
