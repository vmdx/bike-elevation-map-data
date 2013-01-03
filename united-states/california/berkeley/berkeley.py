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

city = 'Berkeley, CA'

regions = [
    # near campus (go bears)
    [
        # south -> north streets
        [
            'College Ave', 'Bowditch St', 'Regent St',
            'Hillegass Ave', 'Benvenue Ave', 'Etna St', 'Piedmont Ave', 'Gayley Road',
            'Telegraph Ave',
            'Dana St', 'Ellsworth St',
            'Fulton St', 'Oxford St', 'Walnut St', 'Shattuck Ave',
            'Spruce St', 'Arch St', 'Scenic Ave', 'Euclid Ave', 'Leroy Ave',
            'La Loma Ave',
            # west of shattuck
            'Milvia St', 'Bonita St', 'Martin Luther King Junior Way',
            'Grant St', 'Josephine St',
            'McKinley Ave', 'McGee Ave', 'California St', 'Sacramento St', 'Acton St',
            'Franklin St', 'Bonar St', 'Chestnut St',
            'Park St', 'Mabel St', 'Matthews St', 'Wallace St', 'Roosevelt Ave',
            'West St', 'Browning St',
            'Curtis St', 'San Pablo Ave',
            # west of san pab
            '10th St', '9th St', '8th St', '7th St', '6th St', '5th St', '4th St',
            '3rd St', '2nd St',
        ],
        # east -> west streets
        [
            'Ashby Ave', 'Russell St', 'Oregon St', 'Stuart St', 'Ward St',
            'Derby St', 'Carleton St', 'Parker St', 'Blake St', 'Dwight Way',
            'Haste St', 'Channing Way', 'Durant Ave', 'Bancroft Way',
            'Kittredge St', 'Allston Way', 'Center St', 'Addison St', 'University Ave',
            'Berkeley Way', 'Hearst Ave', 'Ridge Rd',
            'Lincoln St', 'Francisco St', 'Delaware St', 'Virginia St',
            'Hilgard Ave', 'Cedar St', 'Vine St', 'Rose St',
            'Jones St', 'Page St', 'Camelia St', 'Gilman St',
        ],
        # weird diagonals
        ['Hopkins St', 'Le Conte Ave'],
    ],
]

breaks = {

    ##################
    # west -> east streets
    # BREAKS ON WEST SIDE
    ##################
    #'1st St': set(['2nd Ave']),
    'Bancroft Way': set(['College Ave']),
    'Francisco St': set(['Franklin St']),
    'La Loma Ave': set(['Virginia St']),
    'Leroy Ave': set(['Virginia St']),
    'Lincoln St': set(['Chestnut St']),
    'Oregon St': set(['Mabel St']),
    'Rose St': set(['Scenic Ave']),


    ##############################
    # south -> north streets
    # BREAKS ON SOUTH SIDE
    ##############################
    #'1st St': set(['2nd Ave']),
}



# For curved roads, where we will need to call the google maps
# directions API, define which parts of which paths are curved.
# WEST -> EAST
# SOUTH -> NORTH
curved_roads = {
    'Curtis St': [('Hopkins St', 'Gilman St')],
    'La Loma Ave': [('Cedar St', 'Rose St')],
    'Le Conte Ave': [('Hearst Ave', 'Euclid Ave')],
    'Lincoln St': [('Acton St', 'Sacramento St')],
    'Ridge Rd': [('Scenic Ave', 'Euclid Ave')],
    'Rose St': [('Spruce St', 'Scenic Ave')],
    'Virginia St': [('Spruce St', 'Arch St')],
}

# These will be copied straight into the paths json object.
# All addresses in the paths will be looked up and given NEXT
# attributes.
custom_paths = {
    'UC Berkeley Gayley/Piedmont': {
        'path': [
            'Hearst Ave and La Loma Ave',
            'Gayley Rd and University Dr',
            'Gayley Rd and Stadium Rim Way',
            'Piedmont Ave and Optometry Lane',
            '2300 Piedmont Ave',
            'Piedmont Ave and Bancroft Way',
        ]
    },
    'Linking Piedmont to Bancroft correctly': {
        'path': [
            '2300 Piedmont Ave',
            'Bancroft Way and College Ave',
        ]
    },
}


# Define bike paths, bike routes, here!
# WEST -> EAST
# SOUTH -> NORTH
route_directives = [
    ('9th St', [('Carleton St', 'Dwight Way', 'route'), ('Dwight Way', 'Delaware St', 'path'), ('Delaware St', 'Gilman St', 'route')]),
    ('Bowditch St', [('Dwight Way', 'Bancroft Way', 'path')]),
    ('California St', [('Ashby Ave', 'Rose St', 'path')]),
    ('Channing Way', [('4th St', 'Martin Luther King Junior Way', 'route'), ('Martin Luther King Junior Way', 'College Ave', 'path')]),
    ('Hillegass Ave', [('Ashby Ave', 'Dwight Way', 'route')]),
    ('Milvia St', [('Russell St', 'Hopkins St', 'route')]),
    ('Russell St', [('San Pablo Ave', 'College Ave', 'path')]),
    ('Telegraph Ave', [('Ashby Ave', 'Dwight Way', 'path')]),
    ('Virginia St', [('5th St', 'Euclid Ave', 'route')]),
]

tbds = {
}


# Notes

