import csv

import json





import pandas as pd


if __name__ == '__main__':
	
	file_path=  "C:\\Users\\User\\Downloads\\Dataset of Malicious and Benign Webpages\\testdata\\Webpages_Classification_test_data.csv"

	i = 0
	with open(file_path, 'r', encoding='utf8') as f:
		csv_reader = csv.reader(f)
		for row in csv_reader:
			print("row: ", str(row).encode())


			if i == 20:
				break
			i += 1


	

	# df = pd.read_csv("C:\\Users\\User\\Downloads\\Dataset of Malicious and Benign Webpages\\testdata\\Webpages_Classification_test_data.csv")
	# # print("df: ", df)
	# print(df.content.)

