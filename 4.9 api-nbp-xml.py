import xml.etree.ElementTree as ET
from pprint import pprint
from typing import List

import requests as re
from pydantic import BaseModel


class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRatesTable(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x000002179685C3B0>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")

data = root.find(".//EffectiveDate").text
print(f"Data tabeli: {data} ")

no = root.find(".//No").text
print(f"Numer tabeli: {no}")

rates = root.findall('.//Rate')
print(rates)

# preiterowac po liscie rates i wypisac obiekty i sprobowac find() wycignac tagi
# Currency, Code, Mid
# USD, 958, 4.09

currency_rates = []
for rate in rates:
    # print(rate)  # <Element 'Rate' at 0x00000216F2063330>
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = float(rate.find('Mid').text)
    print(f"Currency: {currency}, Code: {code}, Mid {mid}")
    # Currency: dolar amerykański, Code: USD, Mid 4.0181
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=mid))

exchange_rate_table = ExchangeRatesTable(table=table_name, date=data, number=no, rates=currency_rates)
print(exchange_rate_table)
pprint(exchange_rate_table)
# ExchangeRatesTable(table='A', date='2023-12-08', number='238/A/NBP/2023',
#                    rates=[CurrencyRate(currency='bat (Tajlandia)', code='THB', mid=0.1137),
#                           CurrencyRate(currency='dolar amerykański', code='USD', mid=4.0181),
#                           CurrencyRate(currency='dolar australijski', code='AUD', mid=2.6546),
#                           CurrencyRate(currency='dolar Hongkongu', code='HKD', mid=0.5145),
#                           CurrencyRate(currency='dolar kanadyjski', code='CAD', mid=2.959),
#                           CurrencyRate(currency='dolar nowozelandzki', code='NZD', mid=2.4699),
#                           CurrencyRate(currency='dolar singapurski', code='SGD', mid=3.0009),
#                           CurrencyRate(currency='euro', code='EUR', mid=4.3303),
#                           CurrencyRate(currency='forint (Węgry)', code='HUF', mid=0.011317),
#                           CurrencyRate(currency='frank szwajcarski', code='CHF', mid=4.5913),
#                           CurrencyRate(currency='funt szterling', code='GBP', mid=5.0458),
#                           CurrencyRate(currency='hrywna (Ukraina)', code='UAH', mid=0.1093),
#                           CurrencyRate(currency='jen (Japonia)', code='JPY', mid=0.027848),
#                           CurrencyRate(currency='korona czeska', code='CZK', mid=0.1779),
#                           CurrencyRate(currency='korona duńska', code='DKK', mid=0.5808),
#                           CurrencyRate(currency='korona islandzka', code='ISK', mid=0.028849),
#                           CurrencyRate(currency='korona norweska', code='NOK', mid=0.3694),
#                           CurrencyRate(currency='korona szwedzka', code='SEK', mid=0.3856),
#                           CurrencyRate(currency='lej rumuński', code='RON', mid=0.8717),
#                           CurrencyRate(currency='lew (Bułgaria)', code='BGN', mid=2.214),
#                           CurrencyRate(currency='lira turecka', code='TRY', mid=0.1386),
#                           CurrencyRate(currency='nowy izraelski szekel', code='ILS', mid=1.0868),
#                           CurrencyRate(currency='peso chilijskie', code='CLP', mid=0.004611),
#                           CurrencyRate(currency='peso filipińskie', code='PHP', mid=0.0725),
#                           CurrencyRate(currency='peso meksykańskie', code='MXN', mid=0.2304),
#                           CurrencyRate(currency='rand (Republika Południowej Afryki)', code='ZAR', mid=0.2127),
#                           CurrencyRate(currency='real (Brazylia)', code='BRL', mid=0.818),
#                           CurrencyRate(currency='ringgit (Malezja)', code='MYR', mid=0.8614),
#                           CurrencyRate(currency='rupia indonezyjska', code='IDR', mid=0.00025906),
#                           CurrencyRate(currency='rupia indyjska', code='INR', mid=0.048191),
#                           CurrencyRate(currency='won południowokoreański', code='KRW', mid=0.003068),
#                           CurrencyRate(currency='yuan renminbi (Chiny)', code='CNY', mid=0.5609),
#                           CurrencyRate(currency='SDR (MFW)', code='XDR', mid=5.3418)])
print(exchange_rate_table.rates[5])  # currency='dolar nowozelandzki' code='NZD' mid=2.4699
print(exchange_rate_table.rates[9])  # currency='dolar nowozelandzki' code='NZD' mid=2.4699
# currency='frank szwajcarski' code='CHF' mid=4.5913
