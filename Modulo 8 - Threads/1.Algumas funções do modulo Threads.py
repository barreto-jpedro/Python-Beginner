#1. Crie uma função proc1 que imprime a mensagem "Processo 1" e siga as instruções: 
from threading import Thread
import threading 

def imprime_mensagem(mensagem="Processo 1"):
    print(f"A mensagem é: {mensagem}")

#a) Inicialize essa função a partir de um objeto thread t1  
thread_1 = Thread(target=imprime_mensagem)
thread_1.start()


#b) Consulte se o objeto thread criado está ativo
if thread_1.is_alive():
    print("O objeto thread criado está ativo")
  
#c) Consulte o nome da thread ativa atualmente 
thread_atual = threading.current_thread()
print(thread_atual.getName)

#d) Consulte o identificador de thead do thread atual 
print(thread_atual.ident())

#e) Consulte a quantidade de threads ativas atualmente 
quantidade_de_threads_ativas = threading.active_count()
print(quantidade_de_threads_ativas) 

#f) Retorne uma lista com todos os threads ativos atualmente
todas_as_threads_ativas = threading.enumerate() 
print(todas_as_threads_ativas)
