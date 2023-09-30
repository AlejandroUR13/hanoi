def hanoi(n, origen, medio, destino):
    if n == 1:
        print(f'Mover disco 1 desde torre {origen} a torre {destino}')
        return
    hanoi(n-1, origen, destino, medio)
    print(f'Mover disco {n} desde torre {origen} a torre {destino}')
    hanoi(n-1, medio, origen, destino)

def main():
    try:
        n = int(input("¿Con que cantidad de discos desea jugar?\n"))
        if n <= 0:
            print("El número de discos debe ser mayor que cero.")
            return
        hanoi(n, 'A', 'B', 'C')
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()
