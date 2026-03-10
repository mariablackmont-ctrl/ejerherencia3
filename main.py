from clases.herencia1.taxi import Taxi
from clases.herencia1.autoparticular import AutoParticular


def main():
    
    coche = Taxi("123-GTO", "Versa", 1000, "123-a")
    print()
    print("*************")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()
    
    ap = AutoParticular("456", "María", "15", "volvo", "rojo", "abc")
    ap.subirAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajarAuto()
    print("Datos del usuario: ")
    print(ap)
        
if __name__ == "__main__":
    main()