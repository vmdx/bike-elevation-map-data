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

city = 'Example, State'

regions = [
    # region 1
    [
        # bucket 1
        [
            'street 1',
        ],
        [
            'avenue 1'
        ],
    ],
]

breaks = {

    ##################
    # west -> east streets
    # BREAKS ON WEST SIDE
    ##################
    #'1st St': set(['2nd Ave']),


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
    #'1st St': [('3rd Ave', '6th Ave')],
}

# These will be copied straight into the paths json object.
# All addresses in the paths will be looked up and given NEXT
# attributes.
custom_paths = {
    #'The Panhandle / SF Bike Route 30': {
    #    'path': [
    #        'Baker St and Fell St',
    #        'San Francisco Bicycle Route 30 and Masonic Ave',
    #        'Kezar Dr and Stanyan St',
    #    ],
    #    'type': 'path' # OPTIONAL
    #},
}


# Define bike paths, bike routes, here!
# WEST -> EAST
# SOUTH -> NORTH
route_directives = [
    # sample route
    #('1st St', [('45th Ave', '30th Ave', 'route')]),
]



# Notes

