import urllib3
import Connection_Class

def main():
    ftp = connect("drwestfall.net")
    login(ftp, "ftp05", "student")
    print(ftp.getwelcome())
    download_BIN(ftp, "newFile")
    disconnect(ftp)





#MAKE SURE THIS IS THE END OF THE DOCUMENT. DO NOT MOVE OR ADD AFTER THIS POINT*********************************************************************
main()