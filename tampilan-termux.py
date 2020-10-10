#coding=utf-8
import os,sys,time



#=======================================#•
      #                                #•
     #            apa??               #•
    #        mau scriptnya ?         #•
   # ya bikin lahhh ..awowkoakaok:v #•
  #   sabrek yutub gw ea aswhuuuu  #•
 #                                #•
#=======================================#•

os.system("clear")
time.sleep(1)
print ""
print ""
print "    [ WAIT ] "
print ""
print ""
time.sleep(2)

def er():
    time.sleep(1)
    print ""
    print " [ KESALAHAN ]"
    print ""
    time.sleep(2)
    main()
logo = """

    █▀▄─▄▀▄ █▄─█ ▄▀▀─ ▄▀▀ ▄▀▄ ▀█▀
    █▀█─█▀█ █─▀█ █─▀▌──▀▄ █▀█ ─█─
    ▀▀─ ▀─▀ ▀──▀ ▀▀▀─ ▀▀─ ▀─▀ ─▀─
•═╦═══════════════( Din-zUgex95 )═══•
  ║ [1] Membuat Script
  ║ [2] Edit Script
  ║ [3] Jalankan Script
  ║ [4] Hapus Script
  ║ [5] Exit
  '"""
def main():
    os.system("clear")
    print (logo)
    pilih = raw_input("   •>>> ")
    if pilih in ["2"]:
       edit_script()
    if pilih in ["4"]:
       hapus()
    if pilih in ["5"]:
       time.sleep(1)
       print ""
       print " [ Exit ]"
       print ""
       exit()
    else:
       er()

def edit_script():
    time.sleep(1)
    print ""
    ed = raw_input(" [ Enter Untuk Edit Script ]")
    print ""
    time.sleep(2)
    os.system("nano tampilan-termux.py")
    main()

def hapus():
    time.sleep(1)
    print ""
    print " [ Tidak Dapat Dihapus ]"
    print ""
    time.sleep(2)
    main()


main()
