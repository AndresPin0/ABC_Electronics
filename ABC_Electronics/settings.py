from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://abc:anc@abcelectronics.nr1t8en.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mongo',
        'NAME': 'additional_information',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}
