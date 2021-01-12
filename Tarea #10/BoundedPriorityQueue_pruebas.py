from BoundedPriorityQueue import BoundedPriorityQueue

print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4, "descripcion":"maestre", "Personas":["Juan P","Diego H"]}
niños = {"prioridad":2, "descripcion":"niños", "Personas":["Santi H","Angel H"]}
mecanicos = {"prioridad":4, "descripcion":"mecanicos", "Personas":["Diana T","Maria Z"]}
mujeres = {"prioridad":3, "descripcion":"mujeres", "Personas":["Lupita M","Sara C"]}
ancianos = {"prioridad":2, "descripcion":"ancianos", "Personas":["Pedro O","Jacobo F"]}
niñas = {"prioridad":1, "descripcion":"niñas", "Personas":["Ana B","Miranda A"]}
hombre = {"prioridad":3, "descripcion":"hombre", "Personas":["Eduardo K","Victor D"]}
vigia = {"prioridad":4, "descripcion":"vigia", "Personas":["John C","Jaime M"]}
capitan = {"prioridad":5, "descripcion":"capitan", "Personas":["Elizabeth T","Bayek S"]}
timonel = {"prioridad":4, "descripcion":"timonel", "Personas":["Evelyn P","Kassandra E"]}


cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(ancianos['prioridad'], ancianos)
cpa.enqueue(niñas['prioridad'], niñas)
cpa.enqueue(hombre['prioridad'], hombre)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)

while not cpa.is_empty():
    cpa.to_string()
    sig = cpa.dequeue()
    print(f"Los que evacuaran el barco ahora seran los {sig}")
cpa.to_string()
print("Se han evacuado a todos los pasajeros")
