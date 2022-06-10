import streamlit as sl
from forex_python.converter import CurrencyRates
sl.header('Rattle currency converter')
sl.write('Rattle currency converter used to convert currencies and know their price in real-time')
currency1=sl.selectbox('Select the currency to know the value',('USD','INR','CAD','EUR','JPY','AUD','GBP','CHF','DZD','ALL','AOA','ARS','AMD','NZD'))
currency2=sl.selectbox('Display value in:',('INR','USD','CAD','EUR','JPY','AUD','GBP','CHF','DZD','ALL','AOA','ARS','AMD','NZD'))

amount=sl.number_input('Amount:')
if sl.button('Convert'):
    c=CurrencyRates()
    sl.header(c.convert(currency1,currency2,amount))