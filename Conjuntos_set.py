#Em Python, conjuntos (sets) são coleções não ordenadas de elementos únicos. 
# A estrutura de dados set permite operações matemáticas de conjuntos (união, interseção, diferença)
# e é otimizada para buscas rápidas e remoção de duplicatas.

#Um set é uma coleção de elementos imutáveis (como números, strings, tuplas) que não aceita duplicatas.
#É definido com chaves {} ou função set().

#Exemplos:

frutas= {"maça", "banana", "laranja"}
numeros = set([1,2,3,3])   #retorna {1,2,3}

#Adicionando elementos .add

frutas.add ("uva")

#Removendo elementos .remove

frutas.remove("banana")
frutas.discard ("pera") #não gera erro se não exisir

#União .union
A= {1,2,3}
B={3,4}
print(A| B) # {1,2,3,4}

#Interseção
print(A | B)  # {3}

#Verificar se elemento existe
frutas= "maça", "laranja", "ovos"
print("maça" in frutas) #true
print("banana" in frutas) #false

#Diferença
A= {1,2,3}
B={1,4,5}
print(A - B)  #2,3 (elementos que estão em A mas não em B)
print(B - A)  #4,5

#Diferença simetrica
print(A ^ B)  # {1, 2, 4, 5} (elementos que estão em A ou B, mas não nos dois)

#Em resumo: 
# Éuma estrutura de dados poderosa para trabalhar com coleções únicas e operações de conjuntos, oferecendo desempenho superior em verificações de pertencimento e manipulação de dados sem duplicata


#EM RESUMO:
# é uma estrutura de dados poderosa para trabalhar com coleções únicas e operações de conjuntos, oferecendo desempenho superior em verificações de pertencimento e manipulação de dados sem duplicata

