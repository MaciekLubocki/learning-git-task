
shopping = {
"warzywniak":["marchewka", "rukola", "cebula","bakłażan","ziemniaki"], 
"mięsny":["łopatka","mielone","kurczak","boczek"], 
"piekarnia":["bułki","chleb","bagietka"]} 


product_sum = sum(map(len,shopping.values()))


for store, product in shopping.items():
    print('W Sklepie', store.capitalize(), 'kupuje:', (', '.join(product)).title())
print('Ilość produktów do kupienia:', product_sum)



print('')
print('Specjalne pozdrowienia dla Najlepszego Mentora! Dziękuję za pomoc w nauce.')