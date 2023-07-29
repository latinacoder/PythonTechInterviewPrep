#build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

weight = 41.5


#Ground Shipping
cost_ground = ""

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >2 and weight <=6:
  cost_ground = weight * 3 + 20
elif weight >6 and weight <=10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Cost Ground Shipping: $", cost_ground)

#premium
premium_shipping = 125.00
print("Cost Premium Shipping: $", premium_shipping)

#drone shipping

drone_shipping = ""

if weight <= 2:
  drone_shipping = weight * 4.5
elif weight >2 and weight <=6:
  drone_shipping = weight * 9
elif weight >6 and weight <=10:
  drone_shipping = weight * 12
else:
  drone_shipping = weight * 14.25
print("Cost Drone Shipping: $", drone_shipping)

