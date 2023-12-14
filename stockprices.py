import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from time import sleep

symbols = input("Enter your stock symbols separated by a \", \": ").split(", ")
for symbol in symbols:
    # Interval required 5 minutes
    data = yf.download(tickers=symbol, period='5d', interval='5m')
    # Print data
    print(data)

    # declare figure
    fig = go.Figure()

    # Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))

    # Add titles

    fig.update_layout(
        title= symbol + ' live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    # Show
    fig.show()

# url = "https://finance.yahoo.com/quote/"
# current_url = ""
# stock_picks = []
# symbols = input("Enter your stock symbols separated by a \", \": ").split(", ")
#
# print(symbols)
# for symbol in symbols:
#     current_url = url + symbol + "/"
#     print(current_url)
#     request = requests.get(current_url)
#     soup = BeautifulSoup(request.text,"html.parser")
#     print(soup.prettify())
#     price = soup.find("fin-streamer",{"class": "Fz(36px)"}).text
#     print(symbol + "'s price is :$" + price)

def stock_price():
    url = ("https://finance.yahoo.com/quote/AC.TO/")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("fin-streamer",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
    return price
    # return soup
    # for price in stock_price:
    #     print(price.text)

# url = ("https://finance.yahoo.com/quote/AFRM/")
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# price = soup.find("fin-streamer",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
# print(price)

# price = stock_price()
# print("\nAFRM's price is " + str(price), end ="")
# while True:
#     new_price = stock_price()
#     if new_price != price:
#         price = stock_price()
#         print("\nAFRM's price is " + str(price), end="")
#     sleep(1)


# Print the job titles in this job posting website.
# url = "https://realpython.github.io/fake-jobs/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# results = soup.find(id="ResultsContainer")
# job_title = results.find_all("h2", class_="title is-5")
# for job in job_title:
#     print(job.text)
# print(soup)


