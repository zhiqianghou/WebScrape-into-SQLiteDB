import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('data.db')


def scrape(url):
	"""scrape the page source from the URL"""
	response = requests.get(url, headers=HEADERS)
	source = response.text
	return source


def extract(source):
	extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
	value = extractor.extract(source)['tours']
	return value


def send_email(message):
	host = "smtp.gmail.com"
	port = 465
	username = "houzh.py@gmail.com"
	password = os.getenv("PASSWORD")
	receiver = "houzh.py@gmail.com"
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)
	print("Emai was sent!")


def store(extracted):
	row = extracted.split(",")
	row = [item.strip() for item in row]
	cursor = connection.cursor()
	cursor.execute("insert into events values(?,?,?)", row)
	connection.commit()


def read(extracted):
	cursor = connection.cursor()
	cursor.execute("select * from events")
	rows = cursor.fetchall()
	print(rows)
	return rows


if __name__ == "__main__":
	while True:
		scraped = scrape(URL)
		extracted = extract(scraped)
		print(extracted)
		contents = read(extracted)
		if extracted != "No upcoming tours":
			if extracted not in contents:
				store(extracted)
				send_email(message="Hey, new event was sent")
	time.sleep(2)
