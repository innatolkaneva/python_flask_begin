import getpass
import hashlib
import logging


logger = logging.getLogger('password_check')
def input_and_check_password():
    logger.debug('Начало input')
    password: str = getpass.getpass()
    if not password:
        logger.warning('Пусто!')
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode('latin-1'))
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception('Некорретный символ', exc_info=ex)

    return False
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
            if input_and_check_password():
                exit(0)
            count_number -= 1
    logger.error('Трижды неверный пароль')
    exit(1)