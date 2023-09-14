import requests
import selectorlib
import smtplib, ssl
import os
import streamlit as st
from datetime import datetime


URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
	"""scrape the page source from the URL"""
	response = requests.get(url, headers=HEADERS)
	source = response.text
	return source


def extract(source):
	extractor = selectorlib.Extractor.from_yaml_file("vis_tempt_extract.yaml")
	value = extractor.extract(source)['home']
	return value


def store(extracted):
	now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
	with open("../data_vis_tempt.txt", "a") as file:
		line = f"{now},{extracted}\n"
		file.write(line)


if __name__ == "__main__":
	scraped = scrape(URL)
	extracted = extract(scraped)
	print(extracted)
	store(extracted)