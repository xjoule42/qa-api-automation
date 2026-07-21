from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

TIMEOUT = int(os.getenv("TIMEOUT"))


