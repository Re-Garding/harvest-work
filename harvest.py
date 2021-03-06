############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("Mint")
    all_melon_types.append(musk)

    casa = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casa.add_pairing("Strawberries")
    casa.add_pairing("Mint")
    all_melon_types.append(casa)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("Prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("Ice Cream")
    all_melon_types.append(yw)

    #print(all_melon_types)
    return all_melon_types

#musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
#casa = MelonType("cas", 2003, "orange", False, False, "Casaba")
#cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
#yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # melon_list = list(melon_types)

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for foods in range(len(melon.pairings)):
            pair = melon.pairings[foods]
            print(f'- {pair}')


    


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    Melon_Type = {}

    for melon in melon_types:
        Melon_Type[melon.code] = melon.name

    return Melon_Type


print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
