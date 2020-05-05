# 60 arcsec = 1 parsec = 3,26156 Light Years

semi_major_axis = 1.29
angular_dist_arcsec = 0.011664
LIGHT_YEARS_IN_PARSEC = 3.26156

distance_parsec = semi_major_axis / angular_dist_arcsec
print(distance_parsec)
apprx_distance_in_light_years = distance_parsec * LIGHT_YEARS_IN_PARSEC
print(apprx_distance_in_light_years)
