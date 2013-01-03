"""
This is a data file for thebikemap.com.

This Python file defines variables documented below.

* city
    A string for what city this file defines.

* regions
    A list of regions. Each region consists of a list of buckets.
    A bucket is a list of non intersecting streets.

* breaks
    Breaks are defined as intersections where there should be
    no path connecting that intersection with the next one.

    Breaks must be defined from west -> east, or south -> north.

    For example: there is a break on 2nd Ave at Lincoln Way, since
    you can't get to 2nd Ave @ Fulton (the next intersection)
    without taking a turn. Lincoln is the south intersection, hence,
    south -> north.

* custom_paths
    Custom paths are nonstandard paths that cannot be defined by simple
    street intersections. For example - the Panhandle bike route in SF.

* curved_roads
    Curved roads define roads that curve in the city. By default, the
    map will attempt to draw a straight line between intersections. This
    does not work on curved roads.

* route_directives
    This defines portions of roads that are designated as bike routes, or
    routes with bike paths.
"""

city = 'San Francisco, CA'

regions = [
    # NOPA
    [
        [
            'Geary Blvd', "O'Farrell St", "Turk St", "Turk Blvd",
            'Ellis St', 'Eddy St',
            'Golden Gate Ave', 'McAllister St', 'Fulton St',
            'Grove St', 'Hayes St', 'Fell St', 'Oak St',
            'Page St', 'Haight St', 'Waller St',
        ],
        [
            'Van Ness Ave', 'Franklin St', 'Gough St',
            'Octavia Blvd', 'Octavia St', 'Laguna St', 'Buchanan St',
            'Webster St', 'Fillmore St', 'Steiner St', 'Pierce St', 'Scott St',
            # Div -> Masonic
            'Divisadero St', "Broderick St", 'Baker St', 'Lyon St', 'Central Ave', 'Masonic Ave',
            # Masonic -> Stanyan
            'Ashbury St', 'Clayton St', 'Belvedere St', 'Parker Ave', 'Cole St', 'Shrader St', 'Stanyan St', 'Arguello Blvd',
        ],
    ],
    # Richmond/Sunset
    [
        # west -> east streets
        [
            'Lake St', 'California St', 'Clement St', 'Geary Blvd',
            'Anza St', 'Balboa St', 'Cabrillo St', 'Fulton St',
            'Lincoln Way', 'Frederick St', 'Hugo St',
            'Irving St', 'Judah St',
            'Kirkham St', 'Lawton St', 'Moraga St',
            'Noriega St', 'Ortega St', 'Pacheco St',
            'Quintara St', 'Rivera St', 'Santiago St',
            'Taraval St', 'Ulloa St', 'Vicente St',
        ],

        # south -> north streets
        [
            # the aves ( no 13th )
            '2nd Ave', '3rd Ave', '4th Ave', '5th Ave', '6th Ave', '7th Ave', '8th Ave', '9th Ave', '10th Ave', '11th Ave', '12th Ave', '14th Ave', '15th Ave', '16th Ave', '17th Ave', '18th Ave', '19th Ave', '20th Ave', '21st Ave', '22nd Ave', '23rd Ave', '24th Ave', '25th Ave', '26th Ave', '27th Ave', '28th Ave', '29th Ave', '30th Ave', '31st Ave', '32nd Ave', '33rd Ave', '34th Ave', '35th Ave', '36th Ave', '37th Ave', '38th Ave', '39th Ave', '40th Ave', '41st Ave', '42nd Ave', '43rd Ave', '44th Ave', '45th Ave', '46th Ave', '47th Ave', '48th Ave',
            # other streets
            'Arguello Blvd', 'Sunset Blvd', 'Funston Ave', 'Park Presidio Blvd', 'Willard St',
            'La Playa St', 'Great Highway',
        ],
    ],

    # Marina / Pac Hgts / Fillmore / Nob Hill / North Beach / TL
    [
        # west -> east streets
        [
            'Oak St', 'Fell St', 'Hayes St', 'Grove St',
            'McAllister St', 'Golden Gate Ave', 'Turk St',
            'Eddy St', 'Ellis St', "O'Farrell St", 'Geary St',
            'Post St', 'Sutter St', 'Bush St', 'Pine St',
            'California St', 'Sacramento St', 'Clay St',
            'Washington St', 'Jackson St', 'Pacific Ave',
            'Broadway St', 'Vallejo St', 'Green St',
            'Union St', 'Filbert St', 'Greenwich St',
            'Lombard St', 'Chestnut St', 'Francisco St',
            'Bay St', 'North Point St', 'Beach St', 'Marina Blvd',
            'Jefferson St',
        ],

        # south -> north streets
        [
            'Masonic Ave', 'Presidio Ave',
            'Lyon St', 'Baker St', 'Broderick St', 'Divisadero St',
            'Scott St', 'Pierce St', 'Steiner St', 'Fillmore St',
            'Webster St', 'Buchanan St', 'Laguna St', 'Octavia Blvd', 'Octavia St',
            'Gough St', 'Franklin St', 'Van Ness Ave',
            'Polk St', 'Larkin St', 'Hyde St', 'Leavenworth St',
            'Jones St', 'Taylor St', 'Mason St',
            'Powell St', 'Stockton St', 'Grant Ave',
            'Kearny St', 'Montgomery St', 'Sansome St',
            'Battery St', 'Front St', 'Davis St', 'Drumm St',
            # there are some tiny north south streets above market...
            '7th St', 'Cyril Magnin St'
        ],
        # weirdo diagonal streets
        [
            'Columbus Ave', 'The Embarcadero', 'Market St'
        ]
    ],

    # Holly Park Circle
    [
        [
            'Holly Park Cir'
        ],
        [
            'Highland Ave', 'Park St', 'Murray St',
            'Appleton Ave', 'Elsie St', 'Bocana St',
        ]
    ],

    # Laurel Heights
    [
        # west -> east streets
        [
            'Pacific Ave', 'Jackson St', 'Washington St',
            'Clay St', 'Sacramento St', 'California St',
            'Mayfair Dr', 'Euclid Ave', 'Geary Blvd',
            'Anza St', 'Terra Vista Ave', 'Edward St',
            'Anza Vista Ave', 'McAllister St', 'Golden Gate Ave',
        ],

        [
            'Arguello Blvd', 'Cherry St', 'Maple St', 'Spruce St',
            'Locust St', 'Laurel St', 'Walnut St', 'Presidio Ave',
            'Palm Ave', 'Jordan Ave', 'Commonwealth Ave', 'Parker Ave',
            'Collins St', 'Stanyan St',
            'Wood St', 'Beaumont Ave', 'Willard N',
            'Baker St', "St Joseph's Ave"
        ],

    ],

    # I need to bike home from Crocker Amazon, fuuu
    [
        # west->east streets
        [
            'Geneva Ave', 'Amazon Ave', 'Italy Ave', 'France Ave',
            'Russia Ave', 'Persia Ave', 'Brazil Ave', 'Excelsior Ave',
            'Avalon Ave', 'Silver Ave', 'Maynard St', 'Ney St',
            'Trumbull St', 'Alemany Blvd', 'Bosworth St', 'Crescent Ave',
            'Richland Ave', 'Park St', 'Highland Ave', 'Appleton Ave',
            'Randall St', '30th St', 'Day St',
            '29th St', '28th St', '27th St', '26th St', '25th St', '24th St',
            '23rd St', '22nd St', '21st St', '20th St', '19th St', '18th St',
            '17th St', '16th St',
        ],

        # mission st, lol
        [
            'Mission St', 'Dolores St'
        ],
    ],

    # Ashbury Heights / Duboce Triangle / Frederick Knob

    [
        # west->east streets
        [
            'Beulah St', 'Frederick St', 'Carl St', 'Parnassus Ave',
            'Grattan St', 'Alma St', 'Rivoli St',
            'Duboce Ave', 'Hermann St', 'Germania St', 'Henry St',
            '14th St', '15th St', '16th St', '17th St'
        ],

        # north->south streets
        [
            '4th Ave', '3rd Ave', 'Hillway Ave', 'Willard St', 'Arguello Blvd',
            'Stanyan St', 'Shrader St', 'Cole St', 'Belvedere St', 'Clayton St',
            'Downey St', 'Ashbury St', 'Delmar St', 'Masonic Ave',
            'Divisadero St', 'Castro St', 'Scott St', 'Noe St', 'Steiner St',
            'Sanchez St', 'Fillmore St', 'Church St', 'Webster St', 'Buchanan St',
            'Laguna St'
        ],
        ['Market St'],
    ],

    # SOMA
    [
        # northwest->southeast streets
        [
            'Steuart St', 'Spear St',
            'Main St', 'Beale St', 'Fremont St',
            '1st St', '2nd St', 'New Montgomery St', '3rd St',
            '4th St', '5th St', '6th St', '7th St', '8th St',
            '9th St', '10th St', '11th St', '12th St'
        ],

        # northeast->southwest streets
        [
            'Market St', 'Mission St', 'Howard St',
            'Folsom St', 'Harrison St', 'Bryant St', 'Brannan St',
            'Townsend St', 'King St'
        ],

        ['Van Ness Ave', 'The Embarcadero'],

    ],

    # The Mission
    [
        # west->east streets
        [
            'Duboce Ave', 'Division St', '14th St', 'Alameda St',
            '15th St', '16th St', '17th St', '18th St', 'Mariposa St',
            '19th St', '20th St', '21st St', '22nd St', '23rd St', '24th St',
            '25th St', '26th St', 'Cesar Chavez St', '27th St', '28th St',
            'Clipper St', 'Elizabeth St', '29th St', 'Day St', '30th St',
            # weird noe streets
            'Jersey St', 'Duncan St', 'Alvarado St',
        ],

        # north->south streets
        [
            'Douglass St', 'Diamond St', 'Collingwood St', 'Castro St',
            'Noe St', 'Sanchez St', 'Church St', 'Dolores St', 'Guerrero St',
            'Valencia St', 'Mission St', 'Capp St', 'Van Ness Ave', 'Shotwell St',
            'Folsom St', 'Harrison St', 'Alabama St', 'Florida St', 'Bryant St',
            'York St', 'Hampshire St', 'Potrero Ave', 'Utah St', 'Vermont St',
            'Kansas St', 'Rhode Island St', 'De Haro St', 'Carolina St',
            'Arkansas St', 'Connecticut St', 'Missouri St', 'Mississippi St',
            'Pennsylvania Ave', 'Indiana St', 'Minnesota St', 'Tennessee St',
            '3rd St', 'Illinois St', 'Chattanooga St',
            # more small streets
            'Bartlett St', 'Fair Oaks St', 'Wisconsin St', 'Texas St',
        ],

    ],

]

breaks = {

    ##################
    # west -> east streets
    # BREAKS ON WEST SIDE
    ##################
    '19th St': set(['Church St']),
    '22nd St': set(['Potrero Ave', 'Missouri St']),
    '26th St': set(['Connecticut St']),
    'Anza St': set(['32nd Ave']),
    'Bay St': set(['Scott St']),
    'Beach St': set(['Buchanan St']),
    'Clay St': set(['Laguna St']),
    'Ellis St': set(['Webster St']),
    'Francisco St': set(['Polk St', 'Hyde St', 'Leavenworth St', 'Scott St']),
    'Golden Gate Ave': set(['Stanyan St']),
    'Grove St': set(['Scott St']),
    'Jefferson St': set(['Scott St', 'Webster St']),
    'Mason St': set(['Marina Blvd']),
    'McAllister St': set(['Parker Ave']),
    'North Point St': set(['Scott St', 'Laguna St']),
    "O'Farrell St": set(['Pierce St', 'Webster St']),
    'Pacheco St': set(['28th Ave', '41st Ave']),
    'Rivera St': set(['24th Ave']),
    'Quintara St': set(['39th Ave']),
    'Vallejo St': set(['Leavenworth St', 'Jones St', 'Taylor St']),
    'Waller St': set(['Central Ave']),
    'Washington St': set(['Scott St']),


    ##############################
    # south -> north streets
    # BREAKS ON SOUTH SIDE
    ##############################
    'Ashbury St': set(['Oak St']),
    'Buchanan St': set(['Eddy St', 'Chestnut St']),
    'Castro St': set(['Duncan St']),
    'Central Ave': set(['Oak St']),
    'Clayton St': set(['Oak St']),
    'Cole St': set(['Oak St']),
    'Connecticut St': set(['25th St']),
    'Hampshire St': set(['17th St']),
    'Larkin St': set(['Chestnut St']),
    'Lyon St': set(['Turk Blvd', 'Oak St', 'Bay St']),
    'Mississippi St': set(['Cesar Chavez St', '25th St']),
    'Missouri St': set(['Cesar Chavez St']),
    'Octavia St': set(['Sacramento St', 'Golden Gate Ave', 'Post St']),
    'Pierce St': set(['Clay St', 'Hayes St']),
    'Shrader St': set(['Oak St']),
    'Texas St': set(['25th St']),
    'Utah St': set(['23rd St']),
    'Vermont St': set(['23rd St']),
    'Webster St': set(['Chestnut St']),
    'York St': set(['Mariposa St']),


    # The Aves (and arguello/funston, lol)
    'Arguello Blvd': set(['Frederick St']),
    '2nd Ave': set(['Lincoln Way']),
    '3rd Ave': set(['Lincoln Way']),
    '4th Ave': set(['Kirkham St', 'Lincoln Way']),
    '5th Ave': set(['Lincoln Way']),
    '6th Ave': set(['Lincoln Way']),
    '7th Ave': set(['Lincoln Way']),
    '8th Ave': set(['Lincoln Way']),
    '9th Ave': set(['Lincoln Way']),
    '10th Ave': set(['Lincoln Way']),
    '11th Ave': set(['Lincoln Way']),
    '12th Ave': set(['Lincoln Way']),
    'Funston Ave': set(['Lincoln Way']),
    '14th Ave': set(['Lincoln Way']),
    '15th Ave': set(['Lincoln Way', 'Lawton St']),
    '16th Ave': set(['Lincoln Way', 'Lawton St']),
    '17th Ave': set(['Lincoln Way']),
    '18th Ave': set(['Lincoln Way']),
    '19th Ave': set(['Lincoln Way']),
    '20th Ave': set(['Lincoln Way']),
    '21st Ave': set(['Lincoln Way']),
    '22nd Ave': set(['Lincoln Way']),
    '23rd Ave': set(['Lincoln Way', 'Taraval St', 'Santiago St']),
    '24th Ave': set(['Lincoln Way']),
    '25th Ave': set(['Lincoln Way', 'Quintara St']),
    '26th Ave': set(['Lincoln Way', 'Quintara St']),
    '27th Ave': set(['Lincoln Way', 'Quintara St']),
    '28th Ave': set(['Lincoln Way']),
    '29th Ave': set(['Lincoln Way']),
    '30th Ave': set(['Lincoln Way']),
    '31st Ave': set(['Lincoln Way', 'Balboa St']),
    '32nd Ave': set(['Lincoln Way']),
    '33rd Ave': set(['Lincoln Way']),
    '34th Ave': set(['Lincoln Way']),
    '35th Ave': set(['Lincoln Way']),
    '36th Ave': set(['Lincoln Way']),
    '37th Ave': set(['Lincoln Way']),
    '38th Ave': set(['Lincoln Way', 'Rivera St']),
    '39th Ave': set(['Lincoln Way', 'Quintara St']),
    '40th Ave': set(['Lincoln Way', 'Quintara St']),
    '41st Ave': set(['Lincoln Way']),
    '42nd Ave': set(['Lincoln Way']),
    '43rd Ave': set(['Lincoln Way']),
    '44th Ave': set(['Lincoln Way']),
    '45th Ave': set(['Lincoln Way']),
    '46th Ave': set(['Lincoln Way']),
    '47th Ave': set(['Lincoln Way']),
    '48th Ave': set(['Lincoln Way']),
    'La Playa St': set(['Lincoln Way']),
}



# For curved roads, where we will need to call the google maps
# directions API, define which parts of which paths are curved.
# WEST -> EAST
# SOUTH -> NORTH
curved_roads = {
    'Lawton St': [('16th Ave', 'Funston Ave')],
    '15th Ave': [('Noriega St', 'Lawton St')],
    'Clayton St': [('Market St', '17th St')],
    'Market St': [('Clayton St', 'Castro St')],
    'Marina Blvd': [('Fillmore St', 'Webster St')],
}

# These will be copied straight into the paths json object.
# All addresses in the paths will be looked up and given NEXT
# attributes.
custom_paths = {
    'The Panhandle / SF Bike Route 30': {
        'path': [
            'Baker St and Fell St',
            'San Francisco Bicycle Route 30 and Masonic Ave',
            'Kezar Dr and Stanyan St',
            'Kezar Dr and John F Kennedy Dr',
            'John F Kennedy Dr and Conservatory Dr East',
            'John F Kennedy Dr and Nancy Pelosi Dr',
            'John F Kennedy Dr and Conservatory Dr West',
            '360 John F Kennedy Dr',
            'John F Kennedy Dr and 8th Ave',
            'John F Kennedy Dr and Hagiwara Tea Garden Dr',
            '802 10th Ave',
            'John F Kennedy Dr and Stow Lake Dr',
            'John F Kennedy Drive and Transverse Dr',
            '750 John F Kennedy Dr',
        ],
        'type': 'path',
    },
    'SF Bike Route 30 / JFK Dr to Ocean Beach': {
        'path': [
            '750 John F Kennedy Dr',
            'John F Kennedy Drive and 30th Ave',
            'John F Kennedy Drive and 36th Ave',
            'John F Kennedy Drive and Chain of Lakes Dr East',
            'John F Kennedy Drive and Chain of Lakes Dr West',
            'John F Kennedy Drive and South Fork Dr',
            'John F Kennedy Drive and 47th Ave',
            'John F Kennedy Drive and Great Highway',
        ],
        'type': 'route'
    },
    'Kezar Drive Panhandle to Sunset': {
        'path': [
            'Kezar Dr and John F Kennedy Dr',
            '700 Kezar Dr',
            'Kezar Dr and Lincoln Way',
        ],
        'type': 'path',
    },
    '20th Ave Sunset to Richmond': {
        'path': [
            '20th Ave and Lincoln Way',
            '700 Martin Luther King Junior Dr',
            'Transverse Dr and San Francisco Bicycle Route 34',
            'John F Kennedy Drive and Transverse Dr',
            '399 Transverse Dr',
            '22nd Ave and Fulton St',
        ],
        'type': 'route',
    },
    'SF Bike Route 34 / MLK and Middle Drives': {
        'path': [
            'Transverse Dr and San Francisco Bicycle Route 34',
            'Middle Drive West and Overlook Drive',
            'Middle Drive West and Metson Rd',
            'Middle Drive West and Martin Luther King Junior Dr',
            'Martin Luther King Junior Dr and Chain of Lakes Dr East',
            'Martin Luther King Junior Dr and South Fork Dr',
            'La Playa St and Lincoln Way',
        ],
        'type': 'route',
    },
    'MLK to JFK on South Fork Dr': {
        'path': [
            'Martin Luther King Junior Dr and South Fork Dr',
            'John F Kennedy Drive and South Fork Dr',
        ],
        'type': 'route',
    },
    '8th Ave into GGP': {
        'path': [
            'Fulton St and 8th Ave',
            'John F Kennedy Dr and 8th Ave',
        ],
        'type': 'route',
    },
    'Sunset Blvd into GGP': {
        'path': [
            'Sunset Blvd and Irving St',
            '3600 Lincoln Way',
            '1276 Martin Luther King Junior Dr',
        ],
        'type': 'route',
    },

    # Connectors for streets that change names.
    'Lincoln Way to Frederick St': {
        'path': [
            '2nd Ave and Lincoln Way',
            'Arguello Blvd and Frederick St',
        ],
    },
    'Hyde/Grove to 8th/Mission': {
        'path': [
            'Hyde St and Grove St',
            '8th St and Mission St',
        ],
        'type': 'path'
    },
    'Judah St to Parnassus Ave': {
        'path': [
            '5th Ave and Judah St',
            '4th Ave and Parnassus Ave',
        ],
    },
}


# Define bike paths, bike routes, here!
# WEST -> EAST
# SOUTH -> NORTH
route_directives = [
    # 4 francisco
    ('Francisco St', [('Octavia St', 'Polk St', 'path')]),
    # 5 embarc
    ('The Embarcadero', [('King St', 'Kearny St', 'path')]),
    # 6 greenwich, green
    ('Greenwich St', [('Lyon St', 'Octavia St', 'route')]),
    ('Green St', [('Octavia St', 'Polk St', 'route')]),
    # 10 clement, 30th, lake, sacramento, clay, webster, broadway
    ('Clement St', [('45th Ave', '30th Ave', 'route')]),
    ('30th Ave', [('Clement St', 'Lake St', 'route')]),
    ('Lake St', [('30th Ave', '28th Ave', 'route'), ('28th Ave', 'Arguello Blvd', 'path')]),
    ('Sacramento St', [('Arguello Blvd', 'Cherry St', 'route')]),
    ('Cherry St', [('Sacramento St', 'Clay St', 'route')]),
    ('Clay St', [('Cherry St', 'Webster St', 'route')]),
    ('Webster St', [('Clay St', 'Broadway St', 'route')]),
    ('Broadway St', [('Webster St', 'The Embarcadero', 'route')]),
    # 11 columbus
    ('Columbus Ave', [('North Point St', 'Montgomery St', 'route')]),
    # 11 2nd
    ('2nd St', [('Market St', 'King St', 'route')]),
    # 16 sutter
    ('Sutter St', [('Steiner St', 'Sansome St', 'route')]),
    # 16 post
    ('Post St', [('Presidio Ave', 'Steiner St', 'path'), ('Steiner St', 'Montgomery St', 'route')]),
    # 19 5th
    ('5th St', [('Market St', 'Townsend St', 'route')]),
    # 20 cabrillo
    ('Cabrillo St', [('La Playa St', 'Arguello Blvd', 'path')]),
    # 20 turk
    ('Turk Blvd', [('Arguello Blvd', 'Masonic Ave', 'path')]),
    # 20 mcallister
    ('McAllister St', [('Masonic Ave', '7th St', 'route')]),
    # 23 7th
    ('7th St', [('McAllister St', 'Market St', 'route'), ('Market St', 'Townsend St', 'path')]),
    # 23 8th
    ('8th St', [('Mission St', 'Townsend St', 'path')]),
    # 25 Polk
    ('Polk St', [('Market St', 'Post St', 'path'), ('Post St', 'Union St', 'route'), ('Union St', 'Beach St', 'path')]),
    # 25 Potrero
    ('Potrero Ave', [('25th St', '17th St', 'path')]),
    # 30 14th
    ('14th St', [('Sanchez St', 'Church St', 'route'), ('Church St', 'Folsom St', 'path'), ('Folsom St', 'Harrison St', 'route')]),
    # 30 Market
    ('Market St', [('Castro St', 'Hayes St', 'path'), ('Hayes St', 'Steuart St', 'route')]),
    # 30 Wiggle
    ('Hayes St', [('Broderick St', 'Scott St', 'route')]),
    ('Fell St', [('Baker St', 'Scott St', 'path')]),
    ('Scott St', [('Haight St', 'Fell St', 'path')]),
    ('Haight St', [('Scott St', 'Pierce St', 'route')]),
    ('Pierce St', [('Waller St', 'Haight St', 'route')]),
    ('Waller St', [('Pierce St', 'Steiner St', 'route')]),
    ('Steiner St', [('Duboce Ave', 'Waller St', 'route')]),
    ('Duboce Ave', [('Steiner St', 'Webster St', 'route'), ('Webster St', 'Market St', 'path')]),
    # 30 SOMA
    ('Folsom St', [('14th St', 'The Embarcadero', 'path')]),
    ('Howard St', [('11th St', 'Fremont St', 'path'), ('Fremont St', 'The Embarcadero', 'route')]),
    # 32 Page
    ('Page St', [('Stanyan St', 'Franklin St', 'route')]),
    # 33 Harrison
    ('Harrison St', [('Cesar Chavez St', '26th St', 'path'), ('26th St', '23rd St', 'route'), ('23rd St', '11th St', 'path')]),
    # 40 17th
    ('17th St', [('Douglass St', 'Kansas St', 'route')]),
    # 40 Kirkham
    ('Kirkham St', [('Great Highway', '6th Ave', 'route')]),
    # 44 Jersey / Chattanooga / 22nd
    ('Jersey St', [('Diamond St', 'Chattanooga St', 'route')]),
    ('Chattanooga St', [('Jersey St', '22nd St', 'route')]),
    ('22nd St', [('Chattanooga St', 'Potrero Ave', 'route')]),
    # 45 Steiner
    ('Steiner St', [('Fulton St', 'Greenwich St', 'route')]),
    # 45 Valencia
    ('Valencia St', [('Cesar Chavez St', 'Duboce Ave', 'path')]),
    # 47 Sanchez
    ('Sanchez St', [('17th St', '14th St', 'route')]),
    # 60 Vicente
    ('Vicente St', [('Great Highway', '14th Ave', 'route')]),
    # 60 Cesar Chavez
    ('Cesar Chavez St', [('Sanchez St', 'Mississippi St', 'route'), ('Mississippi St', '3rd St', 'path'), ('3rd St', 'Illinois St', 'route')]),
    # 65 Arguello
    ('Arguello Blvd', [('Fulton St', 'Jackson St', 'path')]),
    # 69 15th Ave
    ('15th Ave', [('Cabrillo St', 'Lake St', 'route')]),
    # 75 20th Ave
    ('20th Ave', [('Vicente St', 'Lincoln Way', 'route')]),
    # 75 23rd Ave
    ('23rd Ave', [('Lincoln Way', 'Lake St', 'route')]),
    # 85 34th Ave
    ('34th Ave', [('Vicente St', 'Irving St', 'route'), ('Cabrillo St', 'Clement St', 'route')]),
    ('Irving St', [('Sunset Blvd', '34th Ave', 'route')]),
    # 95 great highway
    ('Great Highway', [('Vicente St', 'Fulton St', 'path'), ('Fulton St', 'Balboa St', 'route')]),
    # 106 octavia
    ('Octavia St', [('Green St', 'Bay St', 'route')]),
    # 330 8th Ave
    ('8th Ave', [('Fulton St', 'Lake St', 'route')]),
]

tbds = {
}

# Notes
# 8th and Market doesn't show up correctly via Google Maps API.
