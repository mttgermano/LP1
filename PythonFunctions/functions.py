###### UFCG FUNC FACILIDADES PYTHON
###### Matheus Germano
### feito em: 31/08/22
#
### útlima verificação de código: 24/11/22   
#
### notas da verificação: 
# Função f_in foi concertada; Função f_sort  e f_sorted foram atualizadas (menos linhas). 
# Outras funções de sort foram adicionadas: Bubble sort e selection sort. 
# Todas funções funcionam e foram checadas.

###v2  = outra versão do código
###NOT = Not Original

#split
def f_split(frase):
    listafinal = []
    aux = ''
    for i in frase:
        if i == ' ':
            listafinal.append(aux)
            aux =''
        else:
            aux = aux + i

    #ultima palavra nn tem espaço depois
    if aux:
        listafinal.append(aux)
    return listafinal


#replace
    #requer a função f_split
def f_replace(existente,requisitado,frase):     #nao pode ser uma lista
    if isinstance(frase,str):
        palavras = f_split(frase)
        for i in range(len(palavras)):
            if palavras[i] == existente:
                palavras[i] = requisitado
            
        final = ''
        for i in range(len(palavras)):
            final = final + palavras[i] + " "
        return final
    else:                                       #espera-se que: se nao for uma string, seja uma lista
        for i in range(len(frase)):
            if frase[i] == existente:
                frase[i] = requisitado
        return frase


#count
def f_count(elemento_buscado,referencia):
    contador = 0
    for i in referencia:
        if elemento_buscado == i:
            contador += 1
    return contador

print(f_count('o', 'ooo'))


#index
def f_index(element1,element2):
    for i in range(len(element2)):
        if element1 == element2[i]:
            return i


#map
                #nao acho que vou usar muito + nao sei como fazer

#try/except
                #minima ideia como fazer isso na mao, acho que nao tem como 


#quicksort   #NTO
def f_sort(lista):       
    # base
    if len(lista) < 2:
        return lista

    # recursão
    else:
        pivot = lista[0]
        menores = [i for i in lista[1:] if i <= pivot]
        maiores = [i for i in lista[1:] if i > pivot]
        return f_sort(menores) + [pivot] + f_sort(maiores)


#bubble sort
def f_bubble(lista):  
    for i in range(1,len(lista)):
        for i in range(1,len(lista)):
            if lista[i] < lista[i-1]:
                #swap
                lista[i],lista[i-1] = lista[i-1],lista[i]
    return lista


#selection sort
def f_selection(lista):  
    indice_troca = 0
    while indice_troca != len(lista):
        # acha o menor
        menor = indice_troca
        for i in range(1+indice_troca,len(lista)):
            if lista[i] < lista[menor]:
                menor = i

        # swap
        lista[indice_troca],lista[menor] = lista[menor],lista[indice_troca]
        indice_troca +=1
    return lista


#mergesort

#sorted
def f_sorted(lista):
    anterior = lista[0]
    check = True
    for i in range(len(lista)):
        if i != 0:
            anterior = lista[i-1]

        if lista[i] < anterior:
            check = False
            break
    return check


#extend
def f_extend(list1,list2):
    for i in list2:
        list1.append(i)
    return list1


#in
def f_in(element1,sequence):        #sequence pode ser tanto str quanto lista
    for i in sequence:       
        if i == element1:         
            return True
        
    return False


#min
def f_min(*element):
    if isinstance(element[0],list) == True:         #menor elemento de uma lista
        menor = element[0][0]
        for i in element[0]:
            if i < menor:
                menor = i
        return menor
    else:                                           #menor elemento geral
        menor = element[0]
        for i in element:
            if i < menor:
                menor = i
        return menor
    

#max
def f_min(*element):
    if isinstance(element[0],list) == True:         #menor elemento de uma lista
        maior = element[0][0]
        for i in element[0]:
            if i > maior:
                maior = i
        return maior
    else:                                           #menor elemento geral
        maior = element[0]                         
        for i in element:
            if i > maior:
                maior = i
        return maior


#join
def f_join(element1,lista):                 
    frase = ''
    for i in lista:
        frase = frase + element1 + i
    return frase


#insert
def f_insert(index,element1,lista):
    listafinal = []
    for i in range(len(lista)):
        if i == index:
            listafinal.append(element1)
        listafinal.append(lista[i])
    return listafinal


#remove
def f_remove(element1,lista):
    listafinal = []
    for i in lista:
        if i == element1:
            pass
        else:
            listafinal.append(i)
    return listafinal


#reverse
def f_reverse(lista):    #assumindo que esse elemento é uma lista, pois str não suport assignment
    tamanho = len(lista) / 2
    if tamanho % 2 != 0:
        tamanho += 0.5
        tamanho = int(tamanho)

    for i in range(tamanho):
        aux = lista[i]
        lista[i] = lista[len(lista) - 1 - i]
        lista[len(lista) - 1 - i] = aux
    return lista


#v2 NTO             #artifícios do range
#listafinal = []
#for i in range(len(lista) -1, -1, -1):
#   listafinal.append(lista[i])
#return listafinal


#clear
def f_clear(lista):
    return []   #NTO #genial 


#copy
def f_copy(lista):
    listafinal = []
    for i in lista:
        listafinal.append(i)
    return listafinal

#v2 #NTO    #mesmo tempo de execução, menor  código
#listafinal = [] + lista
#return listafinal


#slices
def f_slices(lista,*ranger):
    listafinal = []
    steps = 0
    if len(ranger) == 3:
        steps = ranger[2]
    temp = steps
    for i in range(len(lista)):       
        if i == ranger[0]:
            break
        if len(ranger) >= 2:    #1arg: corta até lá || 2arg: começa a cortar daqui || 3 arg: steps
            if i < ranger[1]:
                pass
            else:
                if len(ranger) == 3:
                    if temp == steps:
                        listafinal.append(lista[i])
                        temp = 0
                    temp += 1     
        else:
            listafinal.append(lista[i])
    return listafinal


#split
    #essa foi genial
def f_split(element1):
    listafinal = []
    aux = ''
    for i in element1:
        if i == ' ':
            listafinal.append(aux)
            aux =''
        else:
            aux = aux + i

    #ultima palavra nn tem espaço depois
    if aux:
        listafinal.append(aux)
    return listafinal


#del
def f_del(index,lista):
    listafinal = []
    for i in range(len(lista)):
        if i == index:
            pass
        else:
            listafinal.append(lista[i])
    return listafinal


#sum
def f_sum(*element,):   
    somatorio = 0 
    if isinstance(element[0],list):     #se for uma lista
        for i in element[0]:
            somatorio += i
        return somatorio

    for i in element:                   #se for int ou float
        somatorio += i
    return somatorio
