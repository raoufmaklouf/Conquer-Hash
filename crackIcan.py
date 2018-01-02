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
                  crackIcan.py v2.0
                 
    by:raouf maklouf
    
    ********************************************                          
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
        path=[open('sources/wordlist/actor-givenname','r'),
          open('sources/wordlist/actor-surname','r'),
          open('sources/wordlist/sqlmap.txt','r'),
          open('/usr/share/wordlists/rockyou.txt','r'), 
          open('sources/wordlist/AFR_DBF.TXT','r'),
          open('sources/wordlist/alloub.txt','r'),
          open('sources/wordlist/Antworth','r'),
          open('sources/wordlist/ASSurnames','r'),
          open('sources/wordlist/av_hips_executables.txt','r'),
          open('sources/wordlist/chinese','r'),
          open('sources/wordlist/cis-surname','r'),
          open('sources/wordlist/common-passwords.txt','r'),
          open('sources/wordlist/Congress','r'),
          open('sources/wordlist/crl-names','r'),
          open('sources/wordlist/dangerzone_a.txt','r'),
          open('sources/wordlist/dangerzone_b.txt','r'),
          open('sources/wordlist/default_pass_for_services_unhash.txt','r'),
          open('sources/wordlist/dic-0294.txt','r'),
          open('sources/wordlist/directory-list-1.0.txt','r'),
          open('sources/wordlist/directory-list-lowercase-2.3-medium.txt','r'),
          open('sources/wordlist/Dosref','r'),
          open('sources/wordlist/etc-hosts','r'),
          open('sources/wordlist/Family-Names','r'),
          open('sources/wordlist/female-names','r'),
          open('sources/wordlist/Given-Names','r'),
          open('sources/wordlist/givennames-ol','r'),
          open('sources/wordlist/Jargon','r'),
          open('sources/wordlist/kjbible','r'),
          open('sources/wordlist/language-list','r'),
          open('sources/wordlist/male-names','r'),
          open('sources/wordlist/malicious_urls.txt','r'),
          open('sources/wordlist/megabeast.txt','r'),
          open('sources/wordlist/movie-characters','r'),
          open('sources/wordlist/names.txt','r'),
          open('sources/wordlist/NAMES.txt','r'),
          open('sources/wordlist/norm.txt','r'),
          open('sources/wordlist/oracle_default_hashes.txt','r'),
          open('sources/wordlist/other-names','r'),
          open('sources/wordlist/oz','r'),
          open('sources/wordlist/routers_userpass.txt','r'),
          open('sources/wordlist/sid.txt','r'),
          open('sources/wordlist/Unabr.dict','r'),
          open('sources/wordlist/unix_users.txt','r'),
          open('sources/wordlist/vxworks_common_20.txt','r'),
          open('sources/wordlist/vxworks_collide_20.txt','r')]
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
  ------------
  if you first run the tool you have to run setup.sh first
  ------------
  usege :sudo chmod +x setup.sh 
  usege :sudo ./setup.sh
  ------------
  usage :python3 crackIcan.py <hash>
  exampel : python3 crackIcan.py 098f6bcd4621d373cade4e832627b4f6
  ------------
             ''')
    print(crack.logo)
    print(help)
    sys.exit()
crack.hash_=inp1

def custom_wordlist():
    print('')
    print('\033[7;49;93m make sure that you do not change the target name when you create the wordlist \033[0m')
    print('')
    global target
    target=input('the target name:') 
    os.system('uxterm ./creatwordlist.sh') 
    
                
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
print('''\033[7;49;93m if you know the target and  collected some personal information
you create a custom wordlist \033[0m''')
print('')    
choice=str(input('\033[7;49;92m try custom wordlist(y/n): \033[0m'))
if choice=='y':
    custom_wordlist()
    wlist=('sources/{}.txt'.format(target))
    wlist=open(wlist,'r')
    crack.s_list=wlist
    __main__1()
    crack.self_wordlist_crack()
    __main__2()
    crack.self_wordlist_crack()
    __main__3()    
    crack.self_wordlist_crack()
    os.system('rm sources/{}.txt'.format(target))
else:
    pass
print('')
print('''\033[7;49;93m this may last for a very long time it depends on the
speed of your processor but make sure that the Hash if it is of latin 
letters and special characters and the number of characters of 
6-32 characters will be cracking \033[0m''')
print('')
choice1=input('\033[7;49;92m you want try random crack (y/n): \033[0m')
if choice1 == 'y':
    __main__1()
    crack.random_crack()
    __main__2()
    crack.random_crack()
    __main__3()
    crack.random_crack()
else:
    sys.exit()
