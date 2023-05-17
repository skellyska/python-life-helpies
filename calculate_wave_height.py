def calculate_wave_height(WVHT, SwH, SwP, SwD, WWH, WWP, WWD, APD):
    # Adjust the weights based on their relative importance
    wvht_weight = 0.3
    swh_weight = 0.2
    wwh_weight = 0.1
    steepness_weight = 0.1
    apd_weight = 0.1
    
    # Calculate the wave height
    wave_height = (WVHT * wvht_weight) + (SwH * swh_weight) + (WWH * wwh_weight) + (APD * apd_weight)
    
    return wave_height

def format_wave_height(wave_height):
    lower_range = int(wave_height)
    upper_range = lower_range + 1
    formatted_height = f"{lower_range}-{upper_range} feet"
    return formatted_height

def get_condition_rating(wind_direction):
    if wind_direction in ['N', 'NE', 'NW']:
        return "Poor"
    elif wind_direction in ['S', 'SE', 'SW']:
        return "Good"
    else:
        return "Fair"
    
# Example data (east SB data rn)
WVHT = 3.0  # feet
SwH = 3.0	# feet
SwP = 12.9  # seconds
SwD = 'W' # direction
WWH = 1.0 # feet
WWP = 4.0 # seconds
WWD = 'NW' # direction
APD = 6.7  # seconds

# Call the function to calculate wave height
wave_height = calculate_wave_height(WVHT, SwH, SwP, SwD, WWH, WWP, WWD, APD)

# Format and print the wave height
formatted_height = format_wave_height(wave_height)

# Get the condition rating based on wind direction
condition_rating = get_condition_rating(WWD)

print(f"Predicted wave height: {formatted_height}")
print(f"Condition rating: {condition_rating}")
