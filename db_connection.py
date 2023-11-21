import pymongo

url = 'mongodb+srv://abc:anc@abcelectronics.nr1t8en.mongodb.net/'

client = pymongo.MongoClient(url)

db = client['additional_information']