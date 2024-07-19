import logging
from pathlib import Path


def setup_logging(log_path: Path):
    log_path.mkdir(parents=True, exist_ok=True)

    # Настраиваем логирование
    logger_info = logging.getLogger('info')
    logger_info.setLevel(logging.INFO)
    handler_info = logging.FileHandler(log_path / 'info.log', mode='a', encoding='utf-8')
    formatter_info = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler_info.setFormatter(formatter_info)
    logger_info.addHandler(handler_info)

    logger_error = logging.getLogger('error')
    logger_error.setLevel(logging.ERROR)
    handler_error = logging.FileHandler(log_path / 'errors.log', mode='a', encoding='utf-8')
    formatter_error = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler_error.setFormatter(formatter_error)
    logger_error.addHandler(handler_error)

    return logger_info, logger_error
