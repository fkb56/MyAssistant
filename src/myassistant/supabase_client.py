import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()



class Supabase:
    def __init__(self):
        self.url: str = os.getenv("SUPABASE_URL")
        self.key: str = os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(self.url, self.key)
        create_client(self.url, self.key)

    def get_client(self):
        return self.client


