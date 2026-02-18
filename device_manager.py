import sounddevice as sd

def get_audio_devices():
    print("--- LISTADO DE DISPOSITIVOS DE AUDIO ---")
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        # QA Check: Buscamos dispositivos con entradas para el meeting 
        # y salidas para nuestro micro virtual
        tipo = "ENTRADA" if dev['max_input_channels'] > 0 else "SALIDA"
        print(f"ID: {i} | {dev['name']} | {tipo} | Canales: {dev['max_input_channels']}/{dev['max_output_channels']}")
    return devices

if __name__ == "__main__":
    get_audio_devices()