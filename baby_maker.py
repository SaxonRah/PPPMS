# Generate CSV of people to test PPPMS - Python Picture Polaroid Management System
# Run this python file to generate a babies.csv file.

import random
import csv
from faker import Faker

fake = Faker()


def make_baby():
    __username = fake.word()
    __result = fake.boolean()
    __tier = 'Big Brain' if __result else "Galaxy Brain"
    __amount = 5 if __result else 15

    """
    Maybe make this data below more coherent. Data values should be consistent in relation to other data values.
    For example: Tier calculations above simulates real data but incorrectly for the rest.
    The code below is ignorant to the values it generates. It can make an inactive account with active dates, 
    invalid amounts, wrong access_expiration dates, ect.
    
    Not sure if it's worth it because, filtering patrons should be easy by just looking at tier, patron status,
    patronage_since_date, ect. to confirm a polaroid should be sent. So making better test data might not be so useful.
    """
    name = fake.name_female() if fake.boolean() else fake.name_male()
    email = fake.safe_email()
    twitter = __username
    discord = __username
    patron_status = "Active" if fake.boolean() else "Inactive"
    follows_you = 'No' if fake.boolean() else "Yes"
    lifetime_amount = random.randint(1, 3) * __amount
    pledge_amount = __amount
    charge_frequency = 'Monthly' if fake.boolean() else "Yearly"
    tier = __tier
    address = fake.street_address()
    street = fake.street_name()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    country = fake.country()
    phone = fake.phone_number()
    patronage_since_date = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
    last_charge_date = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
    last_charge_status = "UNKNOWN"
    additional_details = "NONE"
    user_id = __username
    last_updated = "UNKNOWN"
    currency = "USD"
    max_posts = random.randint(0, 1023)
    access_expiration = fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=None)
    next_charge_date = fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=None)

    baby = [name, email, twitter, discord, patron_status,
            follows_you, lifetime_amount, pledge_amount, charge_frequency,
            tier, address, street, city, state, zipcode, country, phone,
            patronage_since_date, last_charge_date, last_charge_status, additional_details,
            user_id, last_updated, currency, max_posts, access_expiration, next_charge_date
            ]
    return baby


def breed(patrons=1024):
    header = ['Name', 'Email', 'Twitter', 'Discord', 'Patron Status',
              'Follows You', 'Lifetime Amount', 'Pledge Amount', 'Charge Frequency',
              'Tier', 'Addressee', 'Street', 'City', 'State', 'Zip', 'Country', 'Phone',
              'Patronage Since Date', 'Last Charge Date', 'Last Charge Status', 'Additional Details',
              'User ID', 'Last Updated', 'Currency', 'Max Posts', 'Access Expiration', 'Next Charge Date'
              ]
    data = []

    for x in range(patrons):
        print("Patron #", x)
        single_baby = make_baby()
        print(single_baby)
        data.append(single_baby)

    with open('./babies.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


if __name__ == "__main__":
    breed(512)
