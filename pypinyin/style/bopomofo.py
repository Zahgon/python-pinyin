# -*- coding: utf-8 -*-
"""BOPOMOFO 相关的几个拼音风格实现:

Style.BOPOMOFO
Style.BOPOMOFO_FIRST
"""
from __future__ import unicode_literals
import re

from pypinyin.constants import Style
from pypinyin.style import register
from pypinyin.style._constants import RE_TONE3
from pypinyin.style._utils import replace_symbol_to_number

# 注音转换表
BOPOMOFO_REPLACE = (
    (re.compile(r'^m(\d)$'), 'mu\\1'),  # 呣
    (re.compile(r'^n(\d)$'), 'N\\1'),  # 嗯
    (re.compile(r'^r5$'), 'er5'),  # 〜兒
    (re.compile(r'iu'), 'iou'),
    (re.compile(r'ui'), 'uei'),
    (re.compile(r'ong'), 'ung'),
    (re.compile(r'^yi?'), 'i'),
    (re.compile(r'^wu?'), 'u'),
    (re.compile(r'iu'), 'v'),
    (re.compile(r'^([jqx])u'), '\\1v'),
    (re.compile(r'([iuv])n'), '\\1en'),
    (re.compile(r'^zhi?'), 'Z'),
    (re.compile(r'^chi?'), 'C'),
    (re.compile(r'^shi?'), 'S'),
    (re.compile(r'^([zcsr])i'), '\\1'),
    (re.compile(r'ai'), 'A'),
    (re.compile(r'ei'), 'I'),
    (re.compile(r'ao'), 'O'),
    (re.compile(r'ou'), 'U'),
    (re.compile(r'ang'), 'K'),
    (re.compile(r'eng'), 'G'),
    (re.compile(r'an'), 'M'),
    (re.compile(r'en'), 'N'),
    (re.compile(r'er'), 'R'),
    (re.compile(r'eh'), 'E'),
    (re.compile(r'([iv])e'), '\\1E'),
    (re.compile(r'([^0-4])$'), '\\g<1>0'),
    (re.compile(r'1$'), ''),
)
BOPOMOFO_TABLE = dict(zip(
    'bpmfdtnlgkhjqxZCSrzcsiuvaoeEAIOUMNKGR2340ê',
    'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˊˇˋ˙ㄝ'
))


class BopomofoConverter(object):




converter = BopomofoConverter()
register(Style.BOPOMOFO, func=converter.to_bopomofo)
register(Style.BOPOMOFO_FIRST, func=converter.to_bopomofo_first)
