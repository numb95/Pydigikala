import requests as r

# dgkala api URL
__apiUrl = "https://service2.digikala.com/api/"
# ToDo Writing API Doc
__apiHeader = {'ApplicationVersion': "1.3.2",
               'cache-control': "no-cache",
               }


def sendrequests(__requestUrl):
    # send a GET Request to API URL with the header type.
    __request = r.request( "GET", url=__apiUrl + __requestUrl, headers=__apiHeader )
    return __request
