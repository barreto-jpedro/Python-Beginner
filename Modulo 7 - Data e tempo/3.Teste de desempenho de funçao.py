# 3. Adapte o programa acima para calcular o tempo de processamento do script. Utilize 
# time.time() e perf_counter() para apresentar a variação do tempo 
import time

def printar_Hello_World():
    for i in range(0,5):
        print('Hello World!')
        time.sleep(3)

antes = time.time()
printar_Hello_World()
depois = time.time()

tempo_gasto = depois - antes
print(f'Tempo gasto calculado com a funçao time.time(): {tempo_gasto} seg.')

antes = time.perf_counter()
printar_Hello_World()
depois = time.perf_counter()

print(f'Tempo gasto calculado com a funçao time.perf_count(): {tempo_gasto} seg.')