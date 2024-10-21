import tkinter as tk


root = tk.Tk()
root.title("Grid Layout")
root.geometry("400x400")

####################################################################
# wenn man das Widget nachher noch erreichen will gibt man Ihm einen
# Namen bevor man es dem Parent-Widget hinzufügt
####################################################################

# Schritt 1: Dem Widget einen Namen geben
myButton = tk.Button(root, text="Row 0, Col 0")
# Schritt 2: Das Widget dem Parent-Widget hinzufügen
myButton.grid(row=0, column=0)

####################################################################################
# wenn das Widget nur einen dekorativen Zweck hat kann man es auch
# direkt beim erstellen hinzufügen. Also Schritt 1 + 2 zusammen
####################################################################################
tk.Button(root, text="Row 0, Col 2").grid(row=0, column=1)
tk.Button(root, text="Row 0, Col 3").grid(row=0, column=2)
tk.Button(root, text="Row 1, Col 1").grid(row=1, column=0)
tk.Button(root, text="Row 1, Col 2").grid(row=1, column=1)
tk.Button(root, text="Row 1, Col 3").grid(row=1, column=2)

####################################################################################
# Columnspan macht das das Widget mehr Platz in der Breite erhält
####################################################################################
tk.Button(root, text="columnspan=2", width=20).grid(row=2, column=0,columnspan=2)
tk.Button(root, text="columnspan=3", width=25).grid(row=3, column=0, columnspan=3)

####################################################################################
# padx und pady sorgen für Abstand
####################################################################################
paddingHorizontal = 5
paddingVertikal = 5

tk.Button(root, text="Row 0, Col 2").grid(row=4, column=0, padx=paddingHorizontal, pady=paddingVertikal)
tk.Button(root, text="Row 0, Col 2").grid(row=4, column=1, padx=paddingHorizontal, pady=paddingVertikal)
tk.Button(root, text="Row 0, Col 3").grid(row=4, column=2, padx=paddingHorizontal, pady=paddingVertikal)
tk.Button(root, text="Row 2, Col 1").grid(row=5, column=0, padx=paddingHorizontal, pady=paddingVertikal)
tk.Button(root, text="Row 2, Col 2").grid(row=5, column=1, padx=paddingHorizontal, pady=paddingVertikal)
tk.Button(root, text="Row 2, Col 3").grid(row=5, column=2, padx=paddingHorizontal, pady=paddingVertikal)



root.mainloop()