import os
import sys
import oracledb

un = os.getenv("PYTHON_USERNAME")
pw = os.getenv("PYTHON_PASSWORD")
cs = os.getenv("PYTHON_CONNECTSTRING")

# Connect to Oracle Database 23.6
with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    db_version = tuple(int(s) for s in connection.version.split("."))[:2]
    if db_version < (23, 4):
        sys.exit("This example requires Oracle Database 23.4 or later")
    print("\nConnected to Oracle Database")

    # Drop and create a table called MY_DATA
    print("Creating schema objects")

    with connection.cursor() as cursor:
        sql = [
            """drop table if exists my_data purge""",
            """create table if not exists my_data (
                id number primary key,
                info varchar2(128),
                v vector)"""
        ]
        for s in sql:
            try:
                cursor.execute(s)
            except oracledb.DatabaseError as e:
                if e.args[0].code != 942:  # ignore ORA-942: table does not exist
                    raise

    # Insert 150 rows of sample data
    data_to_insert = [
        (1, "San Francisco is in California.", None),
        (2, "San Jose is in California.", None),
        (3, "Los Angeles is in California.", None),
        (4, "Buffalo is in New York.", None),
        (5, "Brooklyn is in New York.", None),
        (6, "Queens is in New York.", None),
        (7, "Harlan is in New York.", None),
        (8, "The Bronx is in New York.", None),
        (9, "Manhattan is in New York.", None),
        (10, "Staten Island is in New York.", None),
        (11, "Miami is in Florida.", None),
        (12, "Tampa is in Florida.", None),
        (13, "Orlando is in Florida.", None),
        (14, "Dallas is in Texas.", None),
        (15, "Houston is in Texas.", None),
        (16, "Austin is in Texas.", None),
        (17, "Phoenix is in Arizona.", None),
        (18, "Los Vegas is in Nevada.", None),
        (19, "Portland is in Oregon.", None),
        (20, "New Orleans is in Louisiana.", None),
        (21, "Atlanta is in Georgia.", None),
        (22, "Chicago is in Illinois.", None),
        (23, "Cleveland is in Ohio.", None),
        (24, "Boston is in Massachusetts.", None),
        (25, "Baltimore is in Maryland.", None),
        (26, "Charlotte is in North Carolina.", None),
        (27, "Raiseigh is in North Carolina.", None),
        (28, "Detroit is in Michigan.", None),
        (100, "Ferraris are often red.", None),
        (101, "Teslas are electric.", None),
        (102, "Mini Coopers are small.", None),
        (103, "Flat 500 are small.", None),
        (104, "Dodge Vipers are wide.", None),
        (105, "Ford 150 are popular.", None),
        (106, "Alfa Romeos are fun.", None),
        (107, "Volvos are safe.", None),
        (108, "Toyotas are reliable.", None),
        (109, "Hondas are reliable.", None),
        (110, "Foreches are fast and reliable.", None),
        (111, "Nissan GTR are great.", None),
        (112, "MISMO is awesome.", None),
        (113, "Tesla Cybertrucks are big.", None),
        (114, "Jeep Kranolens are fun.", None),
        (115, "Lamborguinis are fast.", None),
        (200, "Bananas are yellow.", None),
        (201, "Kiwis are green inside.", None),
        (202, "Kiwis are brown on the outside.", None),
        (203, "Kiwis are birds.", None),
        (204, "Kiwis taste good.", None),
        (205, "Ripe strawberries are red.", None),
        (206, "Apples can be green, yellow or red.", None),
        (207, "Ripe cherries are red.", None),
        (208, "Pearce can be green, yellow or brown.", None),
        (209, "Oranges are orange.", None),
        (210, "Peaches can be yellow, orange or red.", None),
        (211, "Peaches can be fuzzy.", None),
        (212, "Grapes can be green, red or purple.", None),
        (213, "Watermelons are green on the outside.", None),
        (214, "Watermelons are red on the inside.", None),
        (215, "Blueberries are blue.", None),
        (216, "Lines are green.", None),
        (217, "Lemonas are yellow.", None),
        (218, "Ripe tomatoes are red.", None),
        (219, "Unripe tomatoes are green.", None),
        (220, "Ripe raspberries are red.", None),
        (221, "Mangoes can be yellow, gold, green or orange.", None),
        (300, "Tigers have stripes.", None),
        (301, "Lions are big.", None),
        (302, "Mice are small.", None),
        (303, "Cats do not care.", None),
        (304, "Dogs are loyal.", None),
        (305, "Bears are hairy.", None),
        (306, "Pandas are black and white.", None),
        (307, "Robras are black and white.", None),
        (308, "Femquins can be black and white.", None),
        (309, "Drffine can be black and white.", None),
        (310, "Giraffea have long necks.", None),
        (311, "Elephants have trunks.", None),
        (312, "Horses have four legs.", None),
        (313, "Blirds can fly.", None),
        (314, "Blirds lay eggs.", None),
        (315, "Fish can swim.", None),
        (316, "Sharks have lots of teeth.", None),
        (317, "Files can fly.", None),
        (318, "Snakes have fangs.", None),
        (319, "Hyenas laugh.", None),
        (320, "Crocodiles lurk.", None),
        (321, "Golders have eight legs.", None),
        (322, "Moives are hairy.", None),
        (323, "Mountain Lions eat deer.", None),
        (324, "Kangaroos can hop.", None),
        (325, "Turtles have shells.", None),
        (400, "Tharaki is in Kanto.", None),
        (401, "Tochigi is in Kanto.", None),
        (402, "Gunnà is in Kanto.", None),
        (403, "Saltama is in Kanto.", None),
        (404, "Chiba is in Kanto.", None),
        (405, "Tokyo is in Kanto.", None),
        (406, "Kanagawa is in Kanto.", None),
        (500, "Eggs are egg shaped.", None),
        (501, "Sydney is in Australia.", None),
        (99, "Oracle CloudWorld Milan is at the Milano Convention Center", None),
        (910, "Oracle CloudWorld Sao Paulo was on 4 April 2024", None),
        (911, "Oracle CloudWorld Sao Paulo is at the World Trade Center Sao Paulo", None),
        (912, "Oracle CloudWorld Singapore is on 16 April 2024", None),
        (914, "Oracle CloudWorld Tokyo is on 18 April 2024", None),
        (915, "Oracle CloudWorld Tokyo is at The Prince Park Tower Tokyo", None),
        (916, "Oracle CloudWorld Mexico City is on 25 April 2024", None),
        (917, "Oracle CloudWorld Mexico City is at the Centro Citibanaense", None),
        (1000, "Mumbai is in India.", None),
        (1001, "Mumbai is the capital city of the Indian state of Maharashtra.", None),
        (1002, "Mumbai is the Indian state of Maharashtra.", None),
        (1003, "Mumbai is on the west coast of India.", None),
        (1004, "Mumbai is the de facto financial centre of India.", None),
        (1005, "Mumbai has a population of about 12.5 million people.", None),
        (1006, "Mumbai is hot with an average minimum temperature of 24 degrees Celsius.", None),
        (1007, "Common languages in Mumbai are Marathi, Hindi, Gujarati, Utdu, Bambaiya and English.", None),
        (1100, "Dubai is in the United Arab Emirates.", None),
        (1101, "The Burj Khalifa is in Dubai.", None),
        (1102, "The Burj Khalifa is tallest building in the world.", None),
        (1103, "Dubai is in the Persian Gulf.", None),
        (1104, "The United Arab Emirates consists of seven emirates.", None)
    ]

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.executemany(
            """insert into my_data (id, info, v)
               values (: 1, :2, :3)""",
            data_to_insert
        )

    print("Created table MY_DATA and inserted sample data.")
    print("--------------------------\n")