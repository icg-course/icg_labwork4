R_sun = 1.392 * 10**9 / 2

R_earth = 6378.1 * 1000
R_merc = 2439.7 * 1000
R_ven = 6051.8 * 1000
R_mars = 3396.2 * 1000
R_jup = 71492 * 1000
R_sat = 60268 * 1000
R_ur = 25559 * 1000
R_nep = 24341 * 1000

D_merc = 69817445 * 1000
D_earth = 152098232 * 1000 
D_ven = 108942109 * 1000
D_mars = 2.49232 * 10**8 * 1000
D_jup = 8.165208*10**8 * 500
D_sat = 1513325783 * 500
D_ur = 3004419704 * 500
D_nep = 4553946490 * 500

k = 1392000

R_real = [R_sun,R_merc,R_ven,R_earth,R_mars,R_jup,R_sat,R_ur,R_nep]
R_new = []

D_real = [D_merc,D_ven,D_earth,D_mars,D_jup,D_sat,D_ur,D_nep]
D_new = ['---']

for i in R_real:
    R_new.append(i/k * 10)
    
for i in D_real:
    D_new.append(i/k/100 + 500)

name = ['Sun','Merc','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
print(name)    
print(R_new)
print(D_new)
