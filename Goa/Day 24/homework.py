import re

# Example list of elements with their colors in HEX or RGB
elements = [
    {"name": "Element1", "color": "#FF5733"},  # HEX color
    {"name": "Element2", "color": (123, 104, 238)},  # RGB color
    {"name": "Element3", "color": "#7FFF00"}  # HEX color
]

def hex_to_rgb(hex_color):
    """Convert HEX color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def process_elements(elements):
    """Process elements based on their color."""
    for element in elements:
        color = element["color"]

        # Convert HEX to RGB if necessary
        if isinstance(color, str):
            color = hex_to_rgb(color)

        # Example operation: print the element's name if its R value is greater than 150
        if color[0] > 150:
            print(f"Element with high R value: {element['name']}")

# Process the elements
process_elements(elements)
