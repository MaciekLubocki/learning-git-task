
shopping = {
"warzywniak":["marchewka", "rukola", "cebula","bakłażan","ziemniaki"], 
"mięsny":["łopatka","mielone","kurczak","boczek"], 
"piekarnia":["bułki","chleb","bagietka"]} 



print('cos tam')

product_sum = sum(map(len,shopping.values()))

print('cos tam')


for store, product in shopping.items():
    print('W Sklepie', store.capitalize(), 'kupuje:', (', '.join(product)).title())
print('Ilość produktów do kupienia:', product_sum)

