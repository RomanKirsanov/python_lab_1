#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decode_message():
    """Декодирование секретного сообщения"""
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    decoded_p = []
    # Расшифровка
    word1 = secret_message[0][3]  
    word2 = secret_message[1][9:13]  
    word3 = secret_message[2][5:15:2]  
    word4 = secret_message[3][7:13][::-1]  
    word5 = secret_message[4][16:21][::-1]  

    decoded_p = [word1, word2, word3, word4, word5]
    decoded_parts = ' '.join(decoded_p)
    print(decoded_parts)
    return decoded_parts