
# earth’s radius (mean radius = 6,371km)
EARTHS_MEAN_RADIUS = 6371  # kilometers

# Google Maps ... default Earth radius of 6,378,137 meters
GOOGLE_MAPS_DEFAULT_EARTH_RADIUS = 6378137  # meters

# circumference of the earth along the equator is 24,901.92 miles,
EARTHS_CIRCUMFERENCE_IN_MILES = 24901.92  # miles
EARTHS_CIRCUMFERENCE_IN_DEGREES = 360  # there are 360 degrees in a circle


def haversine_formula():
    # This JavaScript uses the Haversine Formula expressed in terms
    #  of a two-argument inverse tangent function
    #  to calculate the great circle distance between two points on the Earth.
    # This is the method recommended for calculating short distances
    #  by Bob Chamberlain (rgc@jpl.nasa.gov) of Caltech
    #  and NASA's Jet Propulsion Laboratory as described on the U.S. Census Bureau Web site.
    # dlon = lon2 - lon1
    # dlat = lat2 - lat1
    # a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
    # c = 2 * atan2( sqrt(a), sqrt(1-a) )
    # d = R * c (where R is the radius of the Earth)
    pass


def generate_list_of_latlon_coordinates_for_circles_to_cover_a_rectangle(lat_dd_nw,
                                                                         lon_dd_nw,
                                                                         lat_dd_se,
                                                                         lon_dd_se,
                                                                         circle_radius,
                                                                         radius_measure="miles"):
    if radius_measure == "miles":
        pass
    elif radius_measure == "kilometers":
        circle_radius = convert_kilometers_to_miles(circle_radius)
    else:
        raise ValueError

    pass


def convert_degrees_minutes_seconds_to_decimal_degrees(degrees, minutes, seconds):
    # Decimal Degrees = Degrees + (Minutes / 60) + (Seconds / 3600)
    # return decimal_degrees
    pass


def convert_decimal_degrees_to_degrees_minutes_seconds(decimal_degrees):
    # return (degrees, minutes, seconds)
    pass


def convert_decimal_degrees_to_miles(decimal_degrees):
    pass


def convert_degrees_of_latitude_to_miles(degrees_of_latitude):
    # ...convert latitude into miles...divide the amount of miles by the degrees in a circle
    # ...distance between 20 degrees north and -10 degrees south...30 degrees
    # Take the amount of degrees and multiply it by 69.2 miles
    # For our example of 30 miles, you have a distance of 2,076 miles.
    pass


def convert_kilometers_to_miles(kilometers):
    return kilometers * 1.6


def convert_miles_to_kilometers(miles):
    return miles * .6


def convert_miles_to_meters(miles):
    # Miles to Meters	mi to m	mi x 1609.344
    return miles * 1609.344


def convert_meters_to_feet(meters):
    return meters * .7


def convert_kilometers_to_meters(kilometers):
    pass


def convert_feet_to_miles(feet):
    # Feet to Miles	ft to mi	ft x .0001893940
    return feet * .0001893940


def convert_centimeters_to_millimeters(centimeters):
    return centimeters * 10


# Conversion	Abbrev.	Formula (rounded)
# Miles to Kilometers	mi to km	mi x 1.609344
# Kilometers to Miles	km to mi	km x .6213711922
