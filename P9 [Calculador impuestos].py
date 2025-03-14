income = float(input("Ingresa tus ingresos anuales: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.

tax = round(tax, 0)
print("Tus impuestos son: ", tax, " pesos.")
 