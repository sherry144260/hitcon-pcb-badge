from pymongo import AsyncMongoClient
from config import Config

config = Config("config.yaml")

mongo = AsyncMongoClient(f"mongodb://{config['mongo']['username']}:{config['mongo']['password']}@{config['mongo']['host']}:{config['mongo']['port']}?uuidRepresentation=standard")
db = mongo[config["mongo"]["db"]]