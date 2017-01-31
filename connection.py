import requests as r

# dgkala api URL
__apiservice1 = "https://service.digikala.com/api/"
__apiservice2 = "https://service2.digikala.com/api/"

# set what API Service should we use.in Iran's IP service1 is Ok but it's not ok with non-iranian IP.But Service2 is OK
#  for both non-iranian and iranian IP
if (str(r.get("https://service.digikala.com/api/", {"ApplicationVersion": "1.3.2"})) == "<Response [200]>"):
    __apiUrl = __apiservice1

else:
    __apiUrl = __apiservice2

# ToDo Writing API Doc

__apiHeader = {'ApplicationVersion': "1.3.2",
               'cache-control': "no-cache",
               }


def sendrequests(__requestUrl):
    # send a GET Request to API URL with the header type.
    __request = r.request("GET", url=__apiUrl + __requestUrl, headers=__apiHeader)
    return __request
