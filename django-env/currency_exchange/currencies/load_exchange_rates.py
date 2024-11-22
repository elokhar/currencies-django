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
        exchange_rate = rates.loc[rates.index[0], ('Adj Close', ticker)]
        if curr.reverse_rate == True:
            currency_pair = "USD" + curr.code
        else:
            currency_pair = curr.code + "USD"

        rate_query_result = models.ExchangeRate.objects.filter(currency_pair=currency_pair)
        
        if rate_query_result:
            rate = rate_query_result[0]
        else:
            rate = models.ExchangeRate(currency_pair=currency_pair)
        rate.exchange_rate = exchange_rate
        rate.save()
    # print(models.ExchangeRate.objects.all().values())