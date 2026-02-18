import customtkinter as ctk
import sounddevice as sd
import speech_recognition as sr
import threading
from deep_translator import GoogleTranslator

class QAAssistantUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- CONFIGURACIÓN DE VENTANA ---
        self.title("QA Meeting Helper - Pro")
        self.geometry("460x780")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.95)
        ctk.set_appearance_mode("dark")

        # --- SECCIÓN DE AUDIO ---
        self.audio_frame = ctk.CTkFrame(self)
        self.audio_frame.pack(pady=10, padx=10, fill="x")

        self.label_audio = ctk.CTkLabel(self.audio_frame, text="CONFIGURACIÓN DE AUDIO", font=("Arial", 12, "bold"))
        self.label_audio.pack(pady=5)

        self.devices = sd.query_devices()
        input_names = [f"{d['name']}" for d in self.devices if d['max_input_channels'] > 0]
        output_names = [f"{d['name']}" for d in self.devices if d['max_output_channels'] > 0]

        self.combo_input = ctk.CTkComboBox(self.audio_frame, values=input_names, width=350)
        self.combo_input.set("Seleccionar Entrada (Meeting/Mic)")
        self.combo_input.pack(pady=5)

        self.combo_output = ctk.CTkComboBox(self.audio_frame, values=output_names, width=350)
        self.combo_output.set("Seleccionar Salida Virtual (Cable)")
        self.combo_output.pack(pady=5)

        # --- ÁREA DE TRANSCRIPCIÓN ---
        self.transcript_area = ctk.CTkTextbox(self, width=430, height=300, font=("Consolas", 12))
        self.transcript_area.pack(pady=5, padx=10)
        self.transcript_area.insert("0.0", ">>> SISTEMA LISTO.\n")

        # --- SECCIÓN DE RESPUESTA POR VOZ ---
        self.response_frame = ctk.CTkFrame(self)
        self.response_frame.pack(pady=10, padx=10, fill="x")

        self.btn_mic = ctk.CTkButton(self.response_frame, text="🎤 INICIAR DICTADO (ES)", 
                                     fg_color="#a16207", hover_color="#854d0e", height=60,
                                     command=self.toggle_mic)
        self.btn_mic.pack(pady=10, padx=20, fill="x")

        self.btn_start = ctk.CTkButton(self, text="INICIAR ESCUCHA DEL MEETING", 
                                       fg_color="green", hover_color="#2e7d32",
                                       command=self.toggle_engine)
        self.btn_start.pack(pady=20)

        # Variables de control
        self.is_recording = False
        self.is_listening = False
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 2.0 
        self.translator = GoogleTranslator(source='es', target='en')
        
        # Guardaremos el objeto de audio aquí para procesarlo al detener
        self.stop_listening_fn = None 

    def get_selected_mic_index(self):
        selection = self.combo_input.get()
        for i, d in enumerate(self.devices):
            if d['name'] == selection:
                return i
        return None

    def validate_selection(self):
        if "Seleccionar" in self.combo_input.get():
            self.log_message("[ADVERTENCIA] Selecciona un micrófono en el listado superior.")
            return False
        return True

    def toggle_engine(self):
        if not self.is_listening:
            if not self.validate_selection(): return
            self.is_listening = True
            self.btn_start.configure(text="DETENER ESCUCHA", fg_color="#FF0000")
            self.log_message(f"[INFO] Escuchando meeting en: {self.combo_input.get()}")
        else:
            self.is_listening = False
            self.btn_start.configure(text="INICIAR ESCUCHA DEL MEETING", fg_color="green")
            self.log_message("[INFO] Escucha detenida.")

    def toggle_mic(self):
        """Maneja el toggle asegurando que al detener se procese lo capturado"""
        if not self.is_recording:
            if not self.validate_selection(): return
            
            self.is_recording = True
            self.btn_mic.configure(text="🛑 DETENER Y PROCESAR", fg_color="#FF0000")
            self.log_message(f"[INFO] Dictando... presiona el botón rojo para traducir ahora.")
            
            # Iniciamos hilo de escucha
            threading.Thread(target=self.capture_voice_thread, daemon=True).start()
        else:
            # IMPORTANTE: No ponemos is_recording = False aquí directamente. 
            # Dejamos que el hilo termine de recoger el audio actual.
            self.btn_mic.configure(text="⏳ PROCESANDO...", state="disabled")
            self.is_recording = False 

    def capture_voice_thread(self):
        target_idx = self.get_selected_mic_index()
        
        with sr.Microphone(device_index=target_idx) as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Escuchamos. Si el usuario pulsa el botón, el motor detectará el fin de la frase
                # o el timeout y procederá a la siguiente línea de código.
                audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=15)
                
                # Procesamos SIEMPRE, incluso si is_recording cambió a False justo ahora
                self.log_message("[SISTEMA] Traduciendo audio capturado...")
                
                text_es = self.recognizer.recognize_google(audio, language="es-ES")
                self.log_message(f"[YO - ES]: {text_es}")
                
                text_en = self.translator.translate(text_es)
                self.log_message(f"[TRADUCCIÓN - EN]: {text_en}")
                
            except sr.UnknownValueError:
                self.log_message("[SISTEMA] No se detectó voz clara.")
            except Exception as e:
                self.log_message(f"[ERROR] Error en el procesamiento: {str(e)}")
            finally:
                # Al final de todo, restauramos la UI
                self.after(0, self.reset_mic_ui)

    def reset_mic_ui(self):
        self.is_recording = False
        self.btn_mic.configure(text="🎤 INICIAR DICTADO (ES)", fg_color="#a16207", state="normal")
        self.log_message("[INFO] Dictado y procesamiento finalizados.")

    def log_message(self, message):
        self.transcript_area.insert("end", f"\n{message}")
        self.transcript_area.see("end")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = QAAssistantUI()
    app.run()