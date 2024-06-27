# ВАРИАНТ


import logging
import requests
from requests.exceptions import RequestException

# Настройка логгеров для разных типов ответов
logging.basicConfig(level=logging.INFO)
success_logger = logging.getLogger('success')
bad_logger = logging.getLogger('bad')
blocked_logger = logging.getLogger('blocked')

# Настройка обработчиков файлов для каждого логгера
success_handler = logging.FileHandler('success_responses.log')
bad_handler = logging.FileHandler('bad_responses.log')
blocked_handler = logging.FileHandler('blocked_responses.log')

# Настройка формата логирования
formatter = logging.Formatter('%(levelname)s: %(message)s')
success_handler.setFormatter(formatter)
bad_handler.setFormatter(formatter)
blocked_handler.setFormatter(formatter)

# Добавление обработчиков к логгерам
success_logger.addHandler(success_handler)
bad_logger.addHandler(bad_handler)
blocked_logger.addHandler(blocked_handler)

# Список URL для проверки
urls = [
    'https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

# Функция для выполнения запросов и логирования результатов
def log_site_responses(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                success_logger.info(f"'{url}', response - {response.status_code}")
            else:
                bad_logger.warning(f"'{url}', response - {response.status_code}")
        except RequestException:
            blocked_logger.error(f"'{url}', NO CONNECTION")

# Вызов функции
log_site_responses(urls)











# ВАРИАНТ



# import requests as rq
# import logging
# from requests.exceptions import ConnectionError, HTTPError, Timeout
# from bs4 import BeautifulSoup
#
# # Настройка логирования
# logging.basicConfig(level=logging.INFO)
# success_logger = logging.getLogger('success')
# bad_logger = logging.getLogger('bad')
# blocked_logger = logging.getLogger('blocked')
#
# # Создание обработчиков файлов для каждого логгера
# success_handler = logging.FileHandler('success_responses.log')
# bad_handler = logging.FileHandler('bad_responses.log')
# blocked_handler = logging.FileHandler('blocked_responses.log')
#
# # Настройка формата логирования
# formatter = logging.Formatter('%(levelname)s: \'%(message)s\', response - %(response)s')
# success_handler.setFormatter(formatter)
# bad_handler.setFormatter(formatter)
# blocked_handler.setFormatter(formatter)
#
# # Добавление обработчиков к логгерам
# success_logger.addHandler(success_handler)
# bad_logger.addHandler(bad_handler)
# blocked_logger.addHandler(blocked_handler)
#
# # Список сайтов для проверки
# sites = [
#     'https://www.youtube.com/',
#     'https://instagram.com',
#     'https://wikipedia.org',
#     'https://yahoo.com',
#     'https://yandex.ru',
#     'https://whatsapp.com',
#     'https://twitter.com',
#     'https://amazon.com',
#     'https://tiktok.com',
#     'https://www.ozon.ru'
# ]
#
# # Функция для выполнения запросов, логирования результатов и парсинга HTML
# def log_site_responses_and_parse_html(sites):
#     for site in sites:
#         try:
#             response = rq.get(site, timeout=3)
#             if response.status_code == 200:
#                 success_logger.info(f"'{site}'", extra={'response': response.status_code})
#                 # Парсинг HTML и вывод ссылок
#                 soup = BeautifulSoup(response.text, 'lxml')
#                 for tag in soup.find_all('a'):
#                     href = tag.get('href')
#                     if href and 'https' not in href:
#                         print('https://www.youtube.com' + href)
#             else:
#                 bad_logger.warning(f"'{site}'", extra={'response': response.status_code})
#         except (ConnectionError, Timeout):
#             blocked_logger.error(f"'{site}', NO CONNECTION")
#
# # Выполнение функции
# log_site_responses_and_parse_html(sites)














# ПАРСИТ, НО НЕ ЗАПИСЫВАЕТ
# import logging
# import requests as rq
#
# # Настройка логгера
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# # Создание обработчика логирования
# handler = logging.FileHandler('logfile.log')
# handler.setLevel(logging.INFO)
#
# # Форматирование логов
# formatter = logging.Formatter('%(levelname)s: %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# # Функция для логирования ответов сайтов и парсинга HTML
# def log_site_responses_and_parse_html(sites):
#     for site in sites:
#         try:
#             response = rq.get(site, timeout=3)
#             if response.status_code == 200:
#                 logger.info(f"Успешный запрос к {site}")
#                 # Здесь может быть ваш код для парсинга HTML
#             else:
#                 logger.warning(f"Запрос к {site} вернул статус-код: {response.status_code}")
#         except rq.exceptions.ConnectTimeout:
#             logger.error(f"'{site}', NO CONNECTION - Connection timed out")
#         except Exception as e:
#             logger.error(f"Произошла ошибка при запросе к {site}: {e}")
#
# # Список сайтов для проверки
# sites = ['https://www.youtube.com/',
#     'https://instagram.com',
#     'https://wikipedia.org',
#     'https://yahoo.com',
#     'https://yandex.ru',
#     'https://whatsapp.com',
#     'https://twitter.com',
#     'https://amazon.com',
#     'https://tiktok.com',
#     'https://www.ozon.ru']
#
# # Вызов функции
# log_site_responses_and_parse_html(sites)


# import logging
# import requests
# from requests.exceptions import RequestException
#
# # Настройка логгеров для разных типов ответов
# logging.basicConfig(level=logging.INFO)
# success_logger = logging.getLogger('success')
# bad_logger = logging.getLogger('bad')
# blocked_logger = logging.getLogger('blocked')
#
# # Настройка обработчиков файлов для каждого логгера
# success_handler = logging.FileHandler('success_responses.log')
# bad_handler = logging.FileHandler('bad_responses.log')
# blocked_handler = logging.FileHandler('blocked_responses.log')
#
# # Настройка формата логирования
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# success_handler.setFormatter(formatter)
# bad_handler.setFormatter(formatter)
# blocked_handler.setFormatter(formatter)
#
# # Добавление обработчиков к логгерам
# success_logger.addHandler(success_handler)
# bad_logger.addHandler(bad_handler)
# blocked_logger.addHandler(blocked_handler)
#
# # Список URL для проверки
# urls = [
#     'https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
#     'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
#     'https://www.ozon.ru']
#
# # Функция для выполнения запросов и логирования результатов
# def log_site_responses(urls):
#     for url in urls:
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 success_logger.info(f"Успешный запрос к {url}, статус-код: {response.status_code}")
#             else:
#                 bad_logger.warning(f"Запрос к {url} вернул статус-код: {response.status_code}")
#         except RequestException as e:
#             blocked_logger.error(f"Нет соединения с {url}: {e}")
#
# # Вызов функции
# log_site_responses(urls)