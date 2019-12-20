# -*- coding: utf-8 -*-

import hashlib


def md5(data):
    return hashlib.md5(data.encode()).hexdigest()


if __name__ == '__main__':
    print(md5("md5"))
    # 1bc29b36f623ba82aaf6724fd3b16718

