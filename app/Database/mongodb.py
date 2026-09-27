import streamlit as st
from pymongo.mongo_client import MongoClient
import Database.models as models

class MongoDB:
    def __init__(self):
        self.config: dict = st.secrets.get("MONGODB", {})
        self.client = None

    def connect(self):
        if self.config.get("HOST", None):
            self.client = MongoClient(
                host = self.config["HOST"])
        else:
            print("unable to read the config")
            raise Exception("DB config missing.")

    def close(self):
        print("close called")

        if self.client:
            self.client.close()

    def register_user(self, data: models.UserRegRecords):
        try:
            self.connect()

            db = self.client["RecordVaultDB"]

            filter = {"email_id": data.email_id}
            data = {"$set": data.model_dump()}
            db.user_records.update_one(filter, data, upsert=True)

        except Exception as e:
            print("Error:", e)
            raise Exception("Failed to register user")
        finally:
            self.close()

    def login_user(self, email_id: str, password: str):
        try:
            self.connect()

        except Exception as e:
            print("Error:", e)
        finally:
            self.close()