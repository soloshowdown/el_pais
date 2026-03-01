
import logging
import os

os.makedirs("output", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("output/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)