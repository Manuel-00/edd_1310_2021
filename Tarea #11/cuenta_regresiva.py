def cuenta_regresiva(num):
    if num >= 0:
        print(f"Quedan {num} segundos para empezar")
        cuenta_regresiva(num-1)
    else:
        print("Comenzamos")

def main():
    cuenta_regresiva(10)

main()
