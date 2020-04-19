import sys
import argparse
from VK_API import *


def create_parser():
    parser = argparse.ArgumentParser(usage="console.py [-h] domain")
    parser.add_argument('domain', help="VK_API: для запуска введите в терминале console.py с "
                                       "аргументом domain, который является коротким именем пользователя ВК."
                                       " Пример: python console.py b1um3r. Шершнев П.С. КН-202(МЕН-280207)"
                                       "для запуска, прошу, использовать свой личный токен")
    return parser


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])

if namespace.domain:
    all_posts = take_friends(namespace.domain)
    file_writer(all_posts)
