IPS_VALIDOS = ['200.135.80.9', "192.168.1.1", "8.35.67.74", "1.2.3.4"]
IPS_INVALIDOS = ["257.32.4.5", "85.345.1.2", "9.8.234.5", "192.168.0.256"]

arquivo = open('IP_addresses.txt', 'r')
novo_arquivo =  open('Verified_IPs.txt','w')

IPS_CHECADOS_E_VALIDOS = []
IPS_CHECADOS_E_INVALIDOS = []


for ip in arquivo:   
    ip = ip.replace('\n','')    
    if ip in IPS_VALIDOS:
        IPS_CHECADOS_E_VALIDOS.append(ip)         
    elif ip in IPS_INVALIDOS:
        IPS_CHECADOS_E_INVALIDOS.append(ip)
        

STRING_IPS_CHECADOS_E_VALIDOS = '[Endereços Validos:]\n'
STRING_IPS_CHECADOS_E_INVALIDOS = '[Endereços invalidos:]\n'

for ip in IPS_CHECADOS_E_VALIDOS:
    STRING_IPS_CHECADOS_E_VALIDOS += (str(ip)+'\n')

for ip in IPS_CHECADOS_E_INVALIDOS:
    STRING_IPS_CHECADOS_E_INVALIDOS += (str(ip)+'\n')    

novo_arquivo.write(STRING_IPS_CHECADOS_E_VALIDOS+'\n'+STRING_IPS_CHECADOS_E_INVALIDOS)
    