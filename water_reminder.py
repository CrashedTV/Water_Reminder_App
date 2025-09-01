import time
import tkinter as tk
from tkinter import messagebox
import threading
import winsound
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, app_instance):
        self.app_instance = app_instance
        
    def on_modified(self, event):
        if event.src_path.endswith('water_reminder.py'):
            self.app_instance.restart_app()

class WaterReminder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("💧 Water Reminder")
        self.root.geometry("700x500")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        self.running = False
        self.alarm_running = False
        self.setup_file_watcher()
        
        # Modern UI
        title = tk.Label(self.root, text="💧 Water Reminder", 
                        font=("Segoe UI", 20, "bold"), 
                        fg="#3498db", bg="#2c3e50")
        title.pack(pady=20)
        
        # Interval frame
        interval_frame = tk.Frame(self.root, bg="#2c3e50")
        interval_frame.pack(pady=20)
        
        tk.Label(interval_frame, text="Reminder Interval", 
                font=("Segoe UI", 12), fg="#ecf0f1", bg="#2c3e50").pack()
        
        self.interval_var = tk.StringVar(value="30")
        interval_entry = tk.Entry(interval_frame, textvariable=self.interval_var, 
                                 font=("Segoe UI", 14), width=8, justify="center",
                                 bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1")
        interval_entry.pack(pady=5)
        
        tk.Label(interval_frame, text="minutes", 
                font=("Segoe UI", 10), fg="#bdc3c7", bg="#2c3e50").pack()
        
        # Buttons
        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        btn_frame.pack(pady=30)
        
        self.start_btn = tk.Button(btn_frame, text="▶ Start Reminders", 
                                  command=self.start_reminders,
                                  font=("Segoe UI", 12, "bold"),
                                  bg="#27ae60", fg="white", 
                                  width=15, height=2, border=0,
                                  activebackground="#2ecc71")
        self.start_btn.pack(pady=5)
        
        self.stop_btn = tk.Button(btn_frame, text="⏹ Stop Reminders", 
                                 command=self.stop_reminders, state="disabled",
                                 font=("Segoe UI", 12, "bold"),
                                 bg="#e74c3c", fg="white", 
                                 width=15, height=2, border=0,
                                 activebackground="#c0392b")
        self.stop_btn.pack(pady=5)
        
        # Status
        self.status_label = tk.Label(self.root, text="Ready to start", 
                                    font=("Segoe UI", 10), 
                                    fg="#95a5a6", bg="#2c3e50")
        self.status_label.pack(pady=10)
        
    def start_reminders(self):
        try:
            interval = int(self.interval_var.get()) * 60
            self.running = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.status_label.config(text=f"Reminders active - every {self.interval_var.get()} minutes", fg="#27ae60")
            
            self.reminder_thread = threading.Thread(target=self.reminder_loop, args=(interval,))
            self.reminder_thread.daemon = True
            self.reminder_thread.start()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def stop_reminders(self):
        self.running = False
        self.alarm_running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_label.config(text="Reminders stopped", fg="#e74c3c")
    
    def reminder_loop(self, interval):
        while self.running:
            time.sleep(interval)
            if self.running:
                self.show_alarm()
    
    def show_alarm(self):
        self.alarm_running = True
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title("💧 Water Time!")
        alarm_window.geometry("600x500")
        alarm_window.configure(bg="#e74c3c")
        alarm_window.attributes("-topmost", True)
        alarm_window.resizable(False, False)
        
        tk.Label(alarm_window, text="💧 DRINK WATER! 💧", 
                font=("Segoe UI", 16, "bold"), 
                fg="white", bg="#e74c3c").pack(pady=30)
        
        tk.Label(alarm_window, text="Time to stay hydrated!", 
                font=("Segoe UI", 12), 
                fg="white", bg="#e74c3c").pack(pady=10)
        
        stop_alarm_btn = tk.Button(alarm_window, text="✓ I Drank Water", 
                                  command=lambda: self.stop_alarm(alarm_window),
                                  font=("Segoe UI", 12, "bold"),
                                  bg="#27ae60", fg="white", 
                                  width=15, height=2)
        stop_alarm_btn.pack(pady=20)
        
        # Start continuous beeping
        self.beep_thread = threading.Thread(target=self.continuous_beep)
        self.beep_thread.daemon = True
        self.beep_thread.start()
    
    def continuous_beep(self):
        while self.alarm_running:
            winsound.Beep(800, 500)
            time.sleep(0.5)
    
    def stop_alarm(self, alarm_window):
        self.alarm_running = False
        alarm_window.destroy()
    
    def setup_file_watcher(self):
        try:
            self.event_handler = FileChangeHandler(self)
            self.observer = Observer()
            self.observer.schedule(self.event_handler, path='.', recursive=False)
            self.observer.start()
        except ImportError:
            pass
    
    def restart_app(self):
        self.root.after(1000, self._restart)
    
    def _restart(self):
        self.root.quit()
        os.execv(sys.executable, ['python'] + sys.argv)
    
    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            if hasattr(self, 'observer'):
                self.observer.stop()
                self.observer.join()

if __name__ == "__main__":
    app = WaterReminder()
    app.run()