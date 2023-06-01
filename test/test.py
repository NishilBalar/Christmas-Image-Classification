import requests

resp = requests.post("https://christmas-model-b04.herokuapp.com/predict", files={'file':open('santa.png', 'rb')})

print(resp.text)