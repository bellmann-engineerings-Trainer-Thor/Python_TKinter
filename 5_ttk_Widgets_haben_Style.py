import tkinter as tk
from tkinter import ttk

def on_readonly_toggle():
    if readonly_var.get():
        entry.state(['readonly'])
    else:
        entry.state(['!readonly'])

root = tk.Tk()
root.title("Styled Frame Beispiel")

style = ttk.Style()
style.configure(
    "Custom.TEntry",
    background="white",              # Hintergrundfarbe des Eingabefeldes
    foreground="black",              # Textfarbe im Eingabefeld
    font=("Arial", 12),              # Schriftart und -größe des Textes
    borderwidth=2,                   # Breite des Rahmens
    relief="sunken",                 # Stil des Rahmens (sunken, raised, etc.)
    padding=5,                       # Innenabstand
    insertwidth=3,                   # Breite des Cursors
    insertcolor="blue",              # Farbe des Cursors
    selectbackground="lightblue",    # Hintergrundfarbe des markierten Textes
    selectforeground="black",        # Textfarbe des markierten Textes
    fieldbackground="lightyellow",   # Hintergrundfarbe des Eingabefeldes, wenn fokussiert
    highlightcolor="red",            # Farbe des Hervorhebungsrahmens, wenn fokussiert
    highlightthickness=2,            # Breite des Hervorhebungsrahmens
    highlightbackground="grey",      # Hintergrundfarbe des Hervorhebungsrahmens, wenn nicht fokussiert
    readonlybackground="lightgrey",  # Hintergrundfarbe, wenn schreibgeschützt
)

# Dynamische Anpassung von Stilen abhängig vom Zustand
style.map(
    "Custom.TEntry",
    foreground=[("disabled", "grey"), ("readonly", "darkgrey")],  # Textfarbe abhängig vom Zustand
    background=[("disabled", "lightgrey")],  # Hintergrundfarbe bei deaktiviertem Zustand
    highlightcolor=[("focus", "green"), ("!focus", "red")],  # Rahmenfarbe abhängig vom Fokus
)

# Entry-Widget erstellen und den Stil anwenden
entry = ttk.Entry(root, style="Custom.TEntry")
entry.pack(padx=20, pady=20, fill="x")

# Toggle für Schreibschutz
readonly_var = tk.BooleanVar(value=False)
readonly_check = ttk.Checkbutton(root, text="Schreibschutz", variable=readonly_var, command=on_readonly_toggle)
readonly_check.pack(pady=10)

# Beispieltext für Demonstration
entry.insert(0, "Dies ist ein Beispieltext")


# Mainloop starten
root.mainloop()
