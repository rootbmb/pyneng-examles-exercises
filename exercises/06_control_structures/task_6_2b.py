# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



while True:
    ip: str = input("Введите ip адресс: ")

    octets = ip.split(".")
    valid_ip = len(octets) == 4 and ip.count('.') == 3

    for i in octets:
        valid_ip = i.isdigit() and int(i) in range(256) and valid_ip

        
    if valid_ip:
            if int(ip.split('.')[0]) in range(1, 224):
                    print('unicast')
            elif int(ip.split('.')[0]) in range(224, 240):
                    print('multicast')
            elif ip == '255.255.255.255':
                    print('local broadcast')
            elif ip == '0.0.0.0':
                    print('unassigned')
            else:
                    print('unused')    
            break    
    else:
        print('Неправильный IP-адрес')