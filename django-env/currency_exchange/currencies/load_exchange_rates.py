from . import models
import yfinance

def create_ticker(curr):
    if curr.reverse_rate == True:
        ticker = curr.code + '=X'
    else:
        ticker = curr.code + 'USD=X'
    return ticker

def load_exchange_rates():
    currs = models.Currency.objects.all()

    tickers_list = []
    for curr in currs:
        ticker = create_ticker(curr)
        tickers_list.append(ticker)

    rates = yfinance.download(tickers_list, period='1d')

    row_label = rates.index[0]        
    for curr in currs:
        ticker = create_ticker(curr)
        curr.exchange_rate = rates.loc[rates.index[0], ('Adj Close', ticker)]
        curr.save()
    # print(models.Currency.objects.all().values())