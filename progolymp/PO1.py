kvikt = 2*int(input("Kuvert ? "))
avikt = 2*int(input("Affisch ? ")) 
bvikt = int(input("Blad ? "))

print(kvikt*229*324/1e6 + avikt*297*420/1e6 + bvikt*210*297/1e6)