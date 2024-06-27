from loguru import logger

# Налаштування виведення логів у файл
logger.add("bot.log", level="INFO", rotation="500 MB")  # Записувати логи рівня INFO та в ротаційний файл "bot.log" кожні 500 МБ

# Логування повідомлень різних рівнів
logger.debug("Це повідомлення рівня DEBUG")
logger.info("Це повідомлення рівня INFO")
logger.warning("Це повідомлення рівня WARNING")
logger.error("Це повідомлення рівня ERROR")
logger.critical("Це повідомлення рівня CRITICAL")