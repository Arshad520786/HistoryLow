# HistoryLow

This is a simple web scraping program to help me check if the merchandises that I'm interested in on momoshop are at history low price.

This program reads from a csv formatted file first to aquire previous histroy low prices.

Then it will start web scraping throught selenium and chrome web driver.

Then it finds the current pricing from the html we got.

For each current pricing we replace the old ones that is higher than the current pricing. It this process it will also inform if the pricing is at history low.

In the final step, this program writes the information of the new history low prices back to the csv file.

![image](https://user-images.githubusercontent.com/39294716/202990201-7179ad1a-fb10-49d1-a4f7-247920134d65.png)
