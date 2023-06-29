import logging
import os
import sys
import unittest
from urllib.parse import urlparse

import pytest

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_path)

from my_parser.pdf_parser import extract_links_from_pdf

# Настройка логгера
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/log.txt')


class ParserTestCase(unittest.TestCase):

    @pytest.mark.parser
    def test_extract_links_from_pdf(self):
        file_path = '/Users/jenya/Desktop/test.pdf'
        expected_links = [
            'https://translater.google.com/',
            'https://lms.ithillel.ua/',
            'https://pypi.org/project/lorem/',
            'https://gorest.co.in/',
            'https://uk.lipsum.com/',
            'https://www.linkedintoqa.com/feed/',
            'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
            'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
            'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
            'https://www.dyoutuber.com/',
            'https://metanit.com/python/tutorial/6.5.php'
        ]

        actual_links = extract_links_from_pdf(file_path)

        # Логирование информации
        logging.info(f"Actual links: {actual_links}")

        # Проверка наличия файла
        self.assertTrue(os.path.exists(file_path), "Файл не существует")

        # Проверка на пустой файл
        self.assertTrue(actual_links, "Файл пустой или не содержит ссылок")

        # Проверка на количество извлеченных ссылок
        self.assertEqual(len(actual_links), len(expected_links), "Неправильное количество ссылок")

        # Проверка на равенство списков ссылок
        self.assertListEqual(actual_links, expected_links, "Список ссылок не совпадает")

        # Проверка на правильность формата ссылок
        for link in actual_links:
            parsed_url = urlparse(link)
            self.assertTrue(parsed_url.scheme and parsed_url.netloc)


if __name__ == '__main__':
    unittest.main()
