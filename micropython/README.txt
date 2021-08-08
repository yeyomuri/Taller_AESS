Configuración.

1. Borre la memoria flash:
    esptool.py --chip esp32 erase_flash
    
2. Escriba el firmware en la esp32:
    esptool.py --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20210601-unstable-v1.15-171-gc5d2095e5.bin
    
3. Cargue su programa con la siguiente instruccion
    ampy --port COM4 -b 115200 put main.py



Firmware = https://micropython.org/download/esp32/

Nota: Escriba las instrucciones en la dirección correspondiente (donde está su programa).