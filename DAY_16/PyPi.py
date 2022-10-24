## Display table from Pypi

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Chamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "r"

print(table)





