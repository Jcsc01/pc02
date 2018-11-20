#Construya una aplicación que solicite 1 coordenada “x” y “y” y determine la distancia que hay
#entre el punto indicado y el punto 0, 0.
#Imprima la distancia y la coordenada ingresada al terminar la app.

x=int(input("Ingrese coordenada x: "))
y=int(input("Ingrese coordenada y: "))
z=((x*x)+(y*y))
distancia=0

for i in range(z):
    if(i*i==z):
        distancia=i

print("distancia: "+str(distancia)+", coordenadas: ("+str(x)+");("+str(y)+")")