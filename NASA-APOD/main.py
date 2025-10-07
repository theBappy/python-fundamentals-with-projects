import wget
import requests

from credentials import API_KEY

url = "https://api.nasa.gov/planetary/apod?api_key=" + API_KEY

response = requests.get(url)
data = response.json()

date = data["date"]
title = data["title"]
image_url = data["url"]

image_filename = wget.download(image_url)
print("Image successfully downloaded", image_filename)