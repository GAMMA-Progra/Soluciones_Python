#problema naves
def _main() -> None:
# recibir los primeros 2 datos n cantidad de naves y s espacio para moverse
  n=int(input())
  s=int(input())
# por cada n una iteracion
  for i in range (n):
  #m cantidad de mvimientos
  #pi posiocion inicial
    m=int(input())
    pi=int(input())
    sum=0
    #for para ir recibiendo lo numeros y que se sumen para luego usar modulo
    for j in range (m):
        tem=int(input())
        sum=sum+tem

# posicion final es la suma tem modulo s
    pf=(pi+sum)%s
# para la distancia minima necesitamos la mitad 
    d=(s-1)//2
    if pf<d:
      dmin=pf+1
    elif pf==d:
      dmin=d
    else:
      dmin=(s-1)-pf
# hostilidad = suma algebraica pas posicion inicial
    hn=sum+pi
    
    print(pf," ",dmin," ",hn)

if __name__ == '__main__':
  _main()