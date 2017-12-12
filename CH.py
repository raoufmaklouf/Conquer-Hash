import hashlib
import sys
import os
import itertools

class hash_crack:
    htype=[]
    hash_=[]
    s_list=[]
    logo=''' 
    
\033[1;49;33m                              ___                \033[0m  
\033[1;49;33m         @__      < - - - - -()_ \      ***       \033[0m  
\033[1;49;33m        (o o)             !!   | |     (o o)       \033[0m 
\033[1;49;33m    ooO--(_)--Ooo------------------ooO--(_)--Ooo----\033[0m
                  Conquer-Hash v1.0
                 
    by:raouf maklouf
    
          \033[1;49;92m      ___           ___          \033[0m
          \033[1;49;92m     /\__\         /\  \         \033[0m    
          \033[1;49;92m    /:/  /         \:\  \        \033[0m    
          \033[1;49;92m   /:/  /           \:\  \       \033[0m    
          \033[1;49;92m  /:/  /  ___   ___ /::\  \      \033[0m    
          \033[1;49;92m /:/__/  /\__\ /\  /:/\:\__\     \033[0m    
          \033[1;49;92m \:\  \ /:/  / \:\/:/  \/__/     \033[0m    
          \033[1;49;92m  \:\  /:/  /   \::/__/          \033[0m    
          \033[1;49;92m   \:\/:/  /     \:\  \          \033[0m    
          \033[1;49;92m    \::/  /       \:\__\         \033[0m    
          \033[1;49;92m     \/__/         \/__/         \033[0m
    ******************hapy-hacking******************                          
         '''    
    
    def random_crack(self):
        char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=\!@#$%^&*()_+|{}"/?>.,<'
        n=range(6,32)
        for t in n:
            try:
                for s in itertools.product(char, repeat=t):
                    password =''.join(s)
                    password.rstrip('')
                    try:
                        bhash=self.hash_
                        x=password.encode('utf-8')
                        h=hashlib.new(self.htype)
                        h.update(x)
                        x=h.hexdigest()
                        if x==bhash:
                                os.system('clear')
                                print(self.logo)
                                print ('hash:\033[31;142m {} \033[0m'.format(self.hash_))
                                print('type: \033[45m {} \033[0m'.format(self.htype),'Result: \033[7;49;92m {} \033[0m '.format(x))
                                sys.exit()
                        else:
                            pass
                    except UnicodeDecodeError:
                        pass
            except UnicodeDecodeError:
                pass
        
                
    def self_wordlist_crack(self):
        try:
            for x in self.s_list:
                try:
                    x=x.rstrip('\n')
                    x=x.rstrip(' ')
                    y=x.encode('utf-8')
                    h=hashlib.new(self.htype)
                    h.update(y)
                    y=h.hexdigest()
                    if y == self.hash_:
                        os.system('clear')
                        print(self.logo)
                        print ('hash:\033[31;142m {} \033[0m'.format(self.hash_))
                        print('type: \033[45m {} \033[0m'.format(self.htype),'Result: \033[7;49;92m {} \033[0m '.format(x))
                        sys.exit()
                    else:
                        pass
                except UnicodeDecodeError:
                    pass
        except UnicodeDecodeError:
            pass
        
    
    def outocrack(self):
        path=[open('/usr/share/wordlists/rockyou.txt','r'),
          open('/usr/share/wordlists/sqlmap.txt','r'),
          open('/usr/share/wordlists/dirb/big.txt','r'),
          open('/usr/share/wordlists/dirb/euskera.txt','r'),
          open('/usr/share/wordlists/dirb/catala.txt','r'),
          open('/usr/share/wordlists/dirb/common.txt','r')]
        for lis in path:
            print('crack is running ... hash type:{} wordlist:{}'.format(self.htype,lis))
            try:
                for x in lis:
                    try:
                        x=x.rstrip('\n')
                        x=x.rstrip(' ')
                        y=x.encode('utf-8')
                        h=hashlib.new(self.htype)
                        h.update(y)
                        y=h.hexdigest()
                        if y == self.hash_:
                            os.system('clear')
                            print(self.logo)
                            print ('hash:\033[31;142m {} \033[0m'.format(self.hash_))
                            print('type: \033[45m {} \033[0m'.format(self.htype),'Result: \033[7;49;92m {} \033[0m '.format(x))
                            sys.exit()
                        else:
                            pass
                    except UnicodeDecodeError:
                        pass
            except UnicodeDecodeError:
                pass
            
crack=hash_crack()            
try:
    inp1= sys.argv[1]
except IndexError:
    help=(''' 
  usage :python3 CH.py <hash>
  exampel: python3 CH.py 098f6bcd4621d373cade4e832627b4f6
             ''')
    print(crack.logo)
    print(help)
    sys.exit()
crack.hash_=inp1
                
def __main__1():
    if len(crack.hash_) == 32:
        crack.htype=('md5')
    elif len(crack.hash_) == 128:
        crack.htype=('sha512')
    elif len(crack.hash_) ==72:
        crack.htype=('md5-sha1')
    elif len(crack.hash_) ==64:
        crack.htype=('sha256')
    elif len(crack.hash_) ==56:
        crack.htype=('sha224')
    elif len(crack.hash_) ==96:
        crack.htype=('sha384')
    elif len(crack.hash_) ==40:
        crack.htype=('sha1')
    else:
        print('hash is not right')
        sys.exit()
    
    
def __main__2(): 
    if len(crack.hash_)==32:
        crack.htype=('md4')
    elif len(crack.hash_)==40:
        crack.htype=('ripemd160')
    elif len(crack.hash_)==64:
        crack.htype=('blake2s256')
    elif len(crack.hash_)==128:
        crack.htype=('whirlpool')
    else:
        pass
        sys.exit()
   
def __main__3():

    if len(crack.hash_)==128:
        crack.htype=('blake2b512')
    else:
        pass
   
if __name__ == "__main__":
    __main__1()
    crack.outocrack()
    __main__2()
    crack.outocrack()
    __main__3()
    crack.outocrack()

print('')    
choice=str(input('try other wordlist(y/n):'))
if choice=='y':
    wlist=input('wordlist:')
    wlist=open(wlist,'r')
    crack.s_list=wlist
    __main__1()
    crack.self_wordlist_crack()
    __main__2()
    crack.self_wordlist_crack()
    __main__3    
    crack.self_wordlist_crack()    
else:
    pass
print('''this may last for a very long time it depends on the
speed of your processor but make sure that the Hash if it is of latin 
letters and special characters and the number of characters of 
6-32 characters will be cracking''')
choice1=input('you want try random crack (y/n):')
if choice1 == 'y':
    __main__1()
    crack.random_crack()
    __main__2()
    crack.random_crack()
    __main__3()
    crack.random_crack()
else:
    sys.exit()