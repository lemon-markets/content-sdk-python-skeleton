import os

from dotenv import load_dotenv
from lemon import api

load_dotenv()

# create your client
client = api.create(
    trading_api_token=os.environ.get('TRADING_API_KEY'),
    market_data_api_token=os.environ.get('DATA_API_KEY'),
    env='paper'  # or 'money'
)
print(client)


def demo_data():
    # get venues
    response = client.market_data.venues.get()
    print(response.results)
    print('\n')


def demo_trading():
    # get account details
    response = client.trading.account.get()
    print(response.results)

    # activate buy order
    response = client.trading.orders.create(isin='US88160R1014', side='buy', quantity=1, venue='xmun')
    order_id = response.results.id
    print(response.results)
    response = client.trading.orders.activate(order_id=order_id)
    print(response)

    # cancel order
    response = client.trading.orders.create(isin='US88160R1014', side='buy', quantity=1, venue='xmun')
    order_id = response.results.id
    print(response.results)
    response = client.trading.orders.cancel(order_id=order_id)
    print(response)


if __name__ == '__main__':
    demo_data()
    demo_trading()
