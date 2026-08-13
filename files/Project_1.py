# CLASS: 
class Menu:
  def __init__(self, name,items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}.' 

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items   
    # pull totals from purchased_items
    total = 0
    for i in self.purchased_items:
      item_price = self.items[i]
    # calculate and store sum into var 
      total = total + item_price
    # return var
    return total

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f'{self.address}'

  # CLASS: 
class Menu:
  def __init__(self, name,items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}.' 

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items   
    # pull totals from purchased_items
    total = 0
    for i in self.purchased_items:
      item_price = self.items[i]
    # calculate and store sum into var 
      total = total + item_price
    # return var
    return total

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f'{self.address}'

  def available_menus(self, time):
    def convert_time(t):
        t = t.lower().strip()
        period = t[-2:]
        hour = int(t[:-2])
        if period == "pm" and hour != 12:
            hour += 12
        elif period == "am" and hour == 12:
            hour = 0
        return hour

    hour = convert_time(time)
    available_menus = []

    for menu in self.menus:
        start = convert_time(menu.start_time)
        end = convert_time(menu.end_time)
        if start <= hour <= end:
            available_menus.append(menu.name)
    return available_menus

  # -------Task 19+--------
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return f'{self.name}'

# ---------------------------------------
# MENUS:
brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, '11am', '4pm')

early_bird = Menu('Early-Bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, '3pm', '6pm')

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, '5pm', '11pm')

kids = Menu('Kid', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, '11am', '9pm')

arepas_menu = Menu('Take a\' Arepa', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, '10am', '8pm')

# ---------------------------------------
# ORDERS:
# print(brunch)
brunch_order1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
# print(f'Your total today is: ${brunch_order1:.2f}')

# print(early_bird)
early_order1 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
# print(f'Your total today is: ${early_order1:.2f}')

# ---------------------------------------
# FRANCHISES
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# print(flagship_store)
# print(new_installment)

noon = flagship_store.available_menus('12pm')
# print(noon)
five_pm = new_installment.available_menus('5pm')
# print(five_pm)

# ---------------------------------------
# BUSINESSES
basta_fazoolin = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

take_a_arepa = Business('Take a\' Arepa', [arepas_place])

print(basta_fazoolin)
print(take_a_arepa)
