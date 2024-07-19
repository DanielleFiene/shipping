# define a weight variable
weight = 41.5

#Ground shipping
if weight <= 2:
  price_ground = weight * 1.5 + 20
elif weight <= 6:
  price_ground = weight * 3 + 20
elif weight <= 10:
  price_ground = weight * 4 + 20
else:
  price_ground = weight * 4.75 + 20

#define a variable for premium ground shipping
price_premium_ground_shipping = 125

# Drone shipping
if weight <= 2:
  price_drone = weight * 4.5
elif weight <= 6:
  price_drone = weight * 9
elif weight <= 10:
  price_drone = weight * 12
else:
  price_drone = weight * 14.25

print(price_ground)
print(price_drone)
print(price_premium_ground_shipping)

