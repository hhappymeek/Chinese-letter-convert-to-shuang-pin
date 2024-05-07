from pypinyin import pinyin, lazy_pinyin, Style
from colorama import init,Fore
import pyperclip
import os
def transfer(input_text):
    output_text = pinyin(input_text, style=Style.TONE3, neutral_tone_with_five=True)
    pinyinsentence = [] 
    pinyinsentence_sp = []
    initials = ['zh','ch','sh','q','w','r','t','y','p','s','d','f','g',
                'h','j','k','l','z','x','c','b','n','m',]
    initials_sp = ['v','i','u','q','w','r','t','y','p','s','d','f','g',
                'h','j','k','l','z','x','c','b','n','m',]
    finals = ['iang','iong','ang','eng','ing','ong','ung','iao','ian','uan','ua','ai','ei','ui','ao','ou','uo','iu','ie','ue','an','en','in','on','un','e','u','i','o','a','v']
    finals_sp = ['d','s','h','g',';','s','d','c','m','r','w','l','z','v','k','b','o','q','x','t','j','f','n','s','p','e','u','i','o','a','y']
    for i in output_text:
        temp = i[0].removeprefix("['")
        temp = temp.removeprefix("']")
        pinyinsentence.append(temp)
    for subtext in pinyinsentence:  
        for initial in initials:        
            if subtext.find(initial) == 0:    
                pinyinsentence_sp.append(initials_sp[initials.index(initial)]) 
                break
            if initial == initials[-1]:
                pinyinsentence_sp.append('o')
        for final in finals:                
            if subtext.find(final) != -1:
                pinyinsentence_sp.append(finals_sp[finals.index(final)])
                break
        if subtext[-1] == '5':
            pinyinsentence_sp.append('0')
        else:
            pinyinsentence_sp.append(subtext[-1])
    return_str = ''
    for character in pinyinsentence_sp:
        return_str = return_str + character
    return return_str
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True
init(autoreset=True)
instruction='0为轻声。1,2,3,4分别对应四个声调\n使用"stop"或"quit"或"exit"退出程序'
print(Fore.YELLOW + instruction,'\n')
print(Fore.CYAN + '输入一行全中文的句段')
while 1==1:
    try:
        text=input()
        if text!='quit' and text!='stop' and text!='exit':
            if is_all_chinese(text):
                transfered=transfer(text)
                pyperclip.copy(transfered)
                print(Fore.YELLOW + transfered)
            elif text=='pd':
                print('你怎么知道我的名字')      
            else:
                print(Fore.RED + '句段不全为中文')
        else:
            break
    except:
        print(Fore.RED + '中文句段无法识别')
        continue


