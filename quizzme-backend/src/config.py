import os
from dotenv import load_dotenv

load_dotenv()

config = {"PORT": int(os.environ.get("PORT", 8000))}
