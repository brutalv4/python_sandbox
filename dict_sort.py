def main():
    stocks = {
        'GOOG': 434,
        'AAPL': 325,
        'FB': 54,
        'AMZN': 632,
        'F': 32,
        'MSFT': 549
    }

    print(min(stocks.items(), key=lambda t: t[1]))


if __name__ == '__main__':
    main()
