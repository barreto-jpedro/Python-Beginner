# 9. Dada uma lista encadeada de caracteres formada por uma sequência alternada de 
# letras e dígitos, construa um método que retorne uma lista na qual as letras são 
# mantidas na sequência original e os dígitos são colocados na ordem inversa. Exemplos: 
# A 1 E 5 T 7 W 8 G → A E T W G 8 7 5 1 
# 3 C 9 H 4 Q 6 → C H Q 6 4 9 3 
# Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos 
# dígitos. Sugestões: 
# a) usar uma fila e uma pilha; 
# b) supor um método ehDigito() que retorna um valor booleano, como por exemplo,  
# verdadeiro caso um caractere seja um dígito

def list_organizer(any_list):    
    my_number_list = []
    my_character_list = []

    for value in any_list:
        cast = str(value)
        if cast.isdigit():
            my_number_list.append(value)
        
        elif cast.isalpha():
            my_character_list.append(value)

    my_number_list = sorted(my_number_list)[::-1]
    organized_list = my_character_list + my_number_list
    return organized_list
        
my_first_test_list = ["A",1,"E",5,"T",7,"W",8,"G"]
my_second_test_list = ["A",1,"E",5,"T",7,"W",8,"G"]

print(f"1ª lista desorganizada: {my_first_test_list}")
print(f"1ª lista ORGANIZADA: {list_organizer(my_first_test_list)}\n")

print(f"2ª lista desorganizada: {my_second_test_list}")
print(f"2ª lista ORGANIZADA: {list_organizer(my_second_test_list)}")
