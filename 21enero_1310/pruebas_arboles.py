from arboles import BinarySearchtree

abb=BinarySearchtree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)
abb.insert(25)
abb.transversal("preorden")
abb.transversal("posorden")
res=abb.search(35)
print(f"el resultado es{res}")
abb.remove(25)
abb.transversal("preorden")
