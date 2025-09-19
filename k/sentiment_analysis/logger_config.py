
import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# optional: get root logger to confirm config applied
logger = logging.getLogger(__name__)
logger.info("Logger configuration loaded successfully")
