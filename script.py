# names of hurricanes


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def convert_damages_data(damages):
  """Convert damages data from string to float and return converted data as a list."""
  conversion = {"M": 1000000,
               "B": 1000000000}

  updated_damages = list()
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage.find('M') != -1:
      updated_damages.append(float(damage[0:damage.find('M')])*conversion["M"])
    if damage.find('B') != -1:
      updated_damages.append(float(damage[0:damage.find('B')])*conversion["B"])
  return updated_damages

updated_damages = convert_damages_data(damages)

print("Updated Damage List: \n")
print(updated_damages)

# write your construct hurricane dictionary function here:


def dict_create(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_count = len(names)
    hurricanes = {}
    for i in range(hurricane_count):
        hurricanes[names[i]] = {"Name": names[i],
                                   "Month": months[i],
                                   "Year": years[i],
                                   "Max Sustained Winds": max_sustained_winds[i],
                                   "Affected Areas": areas_affected[i],
                                   "Damages": updated_damages[i],
                                   "Deaths": deaths[i]}
        
    return hurricanes

hurricanes_name = dict_create(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

print('\n List of Hurricanes by name: \n', hurricanes_name)


# write your construct hurricane by year dictionary function here:

hurricanes = dict_create(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

def dict_create_year(hurricanes):
    hurricanes_by_year = {}
    for year in hurricanes:
      current_year = hurricanes[year]["Year"]
      current_cane = hurricanes[year]
      if current_year not in hurricanes_by_year:
        hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

hurricanes_year = dict_create_year(hurricanes)

print("\n Hurricanes Listed By Year: \n", hurricanes_year)
print("\n Hurricane by Year Example, 1961: \n", hurricanes_year[1961])
        


# write your count affected areas function here:

def count_areas(hurricanes):
  counted_hurricane_areas = {}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]["Affected Areas"]:
      if area not in counted_hurricane_areas:
        counted_hurricane_areas[area] = 1
      else:
        counted_hurricane_areas[area] += 1
  return counted_hurricane_areas

hurricane_affected_areas = count_areas(hurricanes)

print("\n Count of Affected Areas: \n", hurricane_affected_areas)



# write your find most affected area function here:

def most_affected_areas(counted_hurricane_areas):
  max_area = "Central America"
  max_area_count = 0

  for area in counted_hurricane_areas:
    if counted_hurricane_areas[area] > max_area_count:
      max_area = area
      max_area_count = counted_hurricane_areas[area]
  return max_area, max_area_count

most_affected_area = most_affected_areas(hurricane_affected_areas)

print("\n The most affected area is: \n", most_affected_area)



# write your greatest number of deaths function here:


def highest_deaths(hurricanes):
  highest_death_hurricane = ''
  highest_death_count = 0

  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] > highest_death_count:
      highest_death_hurricane = hurricane
      highest_death_count = hurricanes[hurricane]["Deaths"]
  return highest_death_hurricane, highest_death_count


print("\n The hurricane with highest mortality is: \n", highest_deaths(hurricanes))


# write your catgeorize by mortality function here:


def mortality_rating(hurricanes):
  mortality_scale = {0:0,
                     1: 100,
                     2: 500,
                     3: 1000,
                     4: 10000}

  hurricanes_by_mortality = {0: [],
                             1: [],
                             2: [],
                             3: [],
                             4: [],
                             5: []}
                           

  for hurricane in hurricanes:
    num_deaths = hurricanes[hurricane]["Deaths"]
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[hurricane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[hurricane])
    else:
      hurricanes_by_mortality[5].append(hurricanes[hurricane])
  return hurricanes_by_mortality

mortality_rating_fin = mortality_rating(hurricanes)

print(mortality_rating_fin[5])

# write your greatest damage function here:

def greatest_damage(hurricanes):
  greatest_damage_hurricane = ""
  greatest_damage_value = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Damages"] == "Damages not recorded":
      continue
    elif hurricanes[hurricane]["Damages"] > greatest_damage_value:
      greatest_damage_hurricane = hurricane
      greatest_damage_value = hurricanes[hurricane]["Damages"]
  return greatest_damage_hurricane, greatest_damage_value

most_damage_hurricane = greatest_damage(hurricanes)

print("\n The most damage hurricane is: \n", most_damage_hurricane)


# find highest damage inducing hurricane and its total cost

def categorize_by_damage(hurricanes):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  
  hurricanes_by_damage = {0: [],
                          1: [],
                          2: [],
                          3: [],
                          4: [],
                          5: []}
  
  for hurricane in hurricanes:
    total_damage = hurricanes[hurricane]["Damages"]
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[hurricane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[hurricane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[hurricane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[hurricane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[hurricane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[hurricane])
    
    return hurricanes_by_damage

hurricanes_by_damage = categorize_by_damage(hurricanes)

print(hurricanes_by_damage)
