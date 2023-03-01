import pymongo
import certifi

con_str = "mongodb+srv://Eperez813:Alex1406@cluster0.drxbfit.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db= client.get_database("onlinestore_ch34")