import re

"""Funkcja do usuwania liczb"""


def usun_liczby(tekst: str) -> str:
    wynik = re.sub(r'\d', '', tekst)
    return wynik


"""Funkcja do usuwania znaczników HTML"""


def usun_znaczniki_html(tekst: str) -> str:
    wynik = re.sub(r'<.*?>', '', tekst)
    return wynik


"""Funkcja do usuwania znaków interpunkcyjnych"""


def usun_interpunkcje(tekst: str) -> str:
    wynik = re.sub(r'\W(?<!\s)', '', tekst)
    return wynik
