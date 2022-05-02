import collections
documentos = ['doc1', 'doc3', 'doc4', 'doc5']
print('Origin:', documentos)
docs = collections.deque(documentos)
print('Deque:', docs)
print('Longitud:', len(docs))  # mostrar número de elementos deque
print('Elemento de más a la izquierda:', docs[0])
print('Elemento de más a la derecha:', docs[-1])
docs.remove('doc3')  # borrar el elemento indicado
print('remove(doc3):', docs)
docs.append('doc6')  # añadir un elemento por la derecha
print(docs)  # deque(['doc1', 'doc4', 'doc5', 'doc6'])
listadocs = list(docs)  # Obtener lista con todos