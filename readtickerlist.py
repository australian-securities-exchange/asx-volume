import csv


def readTickersIntoArray():  # returns list of ASX tickers as an array
    tickerCodes = []  # initialising tickers array
    with open("ASX_TickerList.txt") as tickerFile:
        next(tickerFile)  # skips first line of file (heading)
        for line in csv.reader(tickerFile, dialect="excel-tab"):
            tickerCodes.append(line[0])  # only reads first column of file (tickers only)
    return tickerCodes


if __name__ == "__main__":
    bruh = readTickersIntoArray()
    print(bruh)  # testing and debugging
    print("breakpoint here")
