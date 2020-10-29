# Install yfinance with the following command
# pip3 install yfinance

import yfinance as yf
zip_ax = yf.Ticker("Z1P.AX")
# msft = yf.Ticker("MSFT")


zip_info = zip_ax.info
zip_volume = zip_ax.history(period="max")
# .actions, .dividends, .splits
print("breakpoint here")


#
# zipdata = zip.history(period='12mo')
# zipdata.loc[:, 'Volume']
# zipvol = zipdata.loc[:,'Volume']
# zipvol.values

def main():
    # pull in ticker data
    # use that array of codes to create ticker objects
    # locate the volume from those objects
    # change this volume to numpy style
    tickerCodes = read tickerdata
    thresholdSD = 10    #threshold value for meaningful change in volume
    timePeriod = '12mo' #time period for volume history, make a user input (in months or according to yfinance documentation)
    relevantTickers = []
    relDisplay = []

    # tickerslength = len(tickercodes) - use this if this length is used more than once

    for (i < len(tickerCodes)):   # for loop for each individual ticker code, do everything in here and then add interesting to a final array
        tickerCode = tickerCodes[i]

        #pulling the data for the particular ticker (make this period a user input too)
        companyData = tickerCode.history(period=timePeriod)
        companyVol = companyData.loc[:, 'Volume']
        numpyCompanyVol = companyVol.values

        #defining 3 day data for assessment use
        company3DayData = tickerCode.history(period='3d')


        #call math assessment to determine mean, standard deviation and the current day's deviation from mean (change this to 3 day deviation?)
        [tickerMean, tickerSD] = dataMean(numpyCompanyVol)
        [tickerNumDiffSD] = currentDayDeviation(numpyCompanyVol, tickerMean, tickerSD)

        #adding ticker to array if sd is more than threshold (need to make the threshold a user input)
        #not the most efficient way, could do all the calculations and create display array in one go, but creates cleaner code that can be
        #broken down into modules, allow for modification or re-purposement for different uses if required in future
        if (tickerNumDiffSD > thresholdSD):
            #creating a list of relevant tickers
            relevantTickers.append(tickerCode)

            # do we need to do extra calculation for any fancy outputs we want here or in a seperate file?
                # e.g. finding past performance off a breakout, current analysis reccomendations
            #finding the % increase in volume activity (over 3 days?) vs mean
            volIncreasePercent = (numpyCompanyVol[-1]/tickerMean)*100 #change to 3 day volume?

            #finding the % increase in price over 3 days
            companyPrice3Day = company3DayData.loc[:, 'Price']
            numpyCompanyPrice3day = companyPrice3Day.values

            PriceIncreasePercent3Day = (numpyCompanyPrice3day[-1]/numpyCompanyPrice3day[0]) * 100


            #relDisplay = [Ticker SDfromMean VolumeIncrease% 3DayPriceMovement?]
            #need to figure out what else we want to include in the output - number of times/performance after it has done this in the past
            relDisplay.append(tickerCode,tickerNumDiffSD,volIncreasePercent,PriceIncreasePercent3Day,'/n')

        # if math shows relevancy, store ticker data to send to yfinance for display
        #creating the display array design
        #display array = name mean stddev stdsfrommean volume
        #arr = ticker vol






