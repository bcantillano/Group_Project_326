from MobileCrawler import asinGet, pageGet, priceGet, nameGet, imageGet

# Extract product's ASIN from url
asin = asinGet()

# Get HTML code
soup = pageGet(asin)

# Get price
priceGet(soup)

# Get product's name
nameGet(soup)

# Get product's image
imageGet(soup)

# Write data to CSV

# Plot data from CSV and find max, min, avg

# *** WRITE GUI CODE HERE ***

