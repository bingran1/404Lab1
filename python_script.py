import requests
# print the version of module requests
print(requests.__version__)
# using requests.get for geting Google Homepage
r1 = requests.get('http://google.com/')
print("For Google Homepage: ")
# print the contents of response r1
print(r1.text)

# getting the URL of my python file on GitHub
r2 = requests.get('https://raw.githubusercontent.com/bingran1/404Lab1/main/python_script.py')
# download my python file from GitHub
with open('py_script.py', 'wb') as f:
    # write the contents of response r2
    f.write(r2.content)
print("For my python script: ")
# print the contents of response r2
print(r2.text)