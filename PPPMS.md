# PPPMS - Python Picture Polaroid Management System
Software to manage a signed polaroid from a host - every 3 months
7(?) Hosts and 835 patrons as of writing. Minimum of 7 and maximum of 5,845 polaroids possible.
# Hosts
Will, Kevin, Nigel, Bernard, Alan, Jabril, Peter, ???

# Patron CSV
Below is everything from a single line on the Patreon CSV file. It contains everything we need, I think.
# __Patreon_CSV_Structure__Members_000000.csv File
Name,Email,Twitter,Discord,Patron Status,Follows You,Lifetime Amount,Pledge Amount,Charge Frequency,Tier,Addressee,
Street,City,State,Zip,Country,Phone,Patronage Since Date,Last Charge Date,Last Charge Status,Additional Details,
User ID,Last Updated,Currency,Max Posts,Access Expiration,Next Charge Date,

# Polaroid to Patron Distribution
Every 3 months a filtered address list with the correct number of polaroids should be produced.
Code will scan the csv from the Patreon site and update the shipping list every 3 months.
Code gives the number of photos needed for each host for every 3 month interval.

## Every 3 Months - Random?
Each of the 7 Hosts take like one hundred photos and photos get mailed randomly.
Shippers can randomly pull a photo from a box for each patron address.

## Every 3 Months - All Hosts Pool?
Each of the 7 Hosts take like one hundred photos every 3 months, photos get mailed in round robin fashion to patrons.
Each address is assigned a host and the host is rotated out every 3 months until no hosts are left.

## Every 3 Months - Rotating Featured Host?
One Host will have to take and sign like 700 photos.
All patrons get the same Host polaroid featured that 3 month interval.

# Questions
Can a patron receive multiple sets of polaroids, if subscribed long enough? --- I'd Assume so.

# Code Structure
Dead simple. Python 3.9 probably supports other versions. Needs faker, csv, random, libraries so far.
baby_maker.py, babies.csv and test_babies.py is used to generate and test dummy data.
The rest of code is for whatever.
