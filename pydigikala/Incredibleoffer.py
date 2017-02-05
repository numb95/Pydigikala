from pydigikala import connection

# DigiKala Incredible offer URL
__apiGetIncredibleOffer = "IncredibleOffer/GetIncredibleOffer"

# Product Link
__dgkalaProductLink = "https://digikala.com/product/DKP-"


def getincredibleoffer():
    # Send Incredible offer to GET request and fetch data as json
    __incredibleOffer = connection.sendrequests(__apiGetIncredibleOffer)
    return __incredibleOffer


# shitty part. i hate to write comment for what happened. it just work. later i will fix ut
__fetchOffer = getincredibleoffer().json()
# this is the shitiest part, should change the structure. for now it's 2:00 and i'm so tired :(. livin' in as is :))
for __row in __fetchOffer["Data"]:
    __link = __dgkalaProductLink + str(__row["ProductId"])
    __info = "English Title: " + __row["ProductTitleEn"] + "\n" + "Persian Title: " + __row[
        "ProductTitleFa"] + "\n" + "Price: " + str(__row["Price"]) + "\n" + "Discount: " + str(__row[
                                                                                                   "Discount"]) + "\n" + __link + "\n\n"
    print(__info)

# I belive i should completely change this section and of-course add other attribute of the product
# ToDO Writing Test using unittest
