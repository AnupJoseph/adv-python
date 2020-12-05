import requests

response = requests.get("https://xkcd.com/353/")

# print(response.content)

print(response.text)

image_url_response = requests.get("https://imgs.xkcd.com/comics/python.png")

# print(image_url_response.content)
with open("image.png","wb") as file:
    file.write(image_url_response.content)