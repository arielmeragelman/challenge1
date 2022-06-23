def registrar():
    import logging
    LOG_FILE= "loggs_info.log"
    logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S',
    handlers=[logging.FileHandler(LOG_FILE)])
