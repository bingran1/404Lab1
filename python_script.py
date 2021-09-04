import requests
print(requests.__version__)
r1 = requests.get('http://google.com/')
print("For Google Homepage: ")
print(r1.text)

r2 = requests.get('https://raw.githubusercontent.com/bingran1/404Lab1/main/python_script.py')
print("For my python script: ")
print(r2.text)