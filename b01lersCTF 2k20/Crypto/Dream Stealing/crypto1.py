#!/usr/bin/python

n = 98570307780590287344989641660271563150943084591122129236101184963953890610515286342182643236514124325672053304374355281945455993001454145469449640602102808287018619896494144221889411960418829067000944408910977857246549239617540588105788633268030690222998939690024329717050066864773464183557939988832150357227
e = 65537
p = 9695477612097814143634685975895486365012211256067236988184151482923787800058653259439240377630508988251817608592320391742708529901158658812320088090921919
c = 75665489286663825011389014693118717144564492910496517817351278852753259053052732535663285501814281678158913989615919776491777945945627147232073116295758400365665526264438202825171012874266519752207522580833300789271016065464767771248100896706714555420620455039240658817899104768781122292162714745754316687483
q = n//p

from Crypto.Util.number import inverse

phi = ( p - 1 )*( q - 1 )

d = inverse(e, phi)

m = pow(c, d, n)
m = hex(m)[2:-1]
m += 'd'
flag =''

i = 0
while(i<len(m)):
	print(m[i:i+2])
	flag += chr(int(m[i:i+2],16))
	i += 2

print(flag)