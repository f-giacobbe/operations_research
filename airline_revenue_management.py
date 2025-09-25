# Airline Revenue Management -> maximizing revenue by deciding how many business and economy class seats to sell



from gurobipy import Model, GRB

# Creating the model
model = Model("AirlineRM")

# Defining variables
x1 = model.addVar(name = "x1", lb = 0)
x2 = model.addVar(name = "x2", lb = 0)

business_fare = 637
economy_fare = 254

total_seats = 176

business_demand = 90
economy_demand = 150

# Defining our objective function (revenue - to maximize)
model.setObjective(business_fare*x1 + economy_fare*x2, GRB.MAXIMIZE)

# Subject to the following constraints:
model.addConstr(x1 + x2 <= total_seats, name = "capacity_constr")
model.addConstr(x1 <= business_demand, name = "demand_constr1")
model.addConstr(x2 <= economy_demand, name = "demand_constr2")

# Let's optimize
model.optimize()

print(f"""
Optimization result:
	business seats to sell: {x1.x}
	economy seats to sell: {x2.x}
	
	with a total revenue of: {model.objVal} euros.
""")