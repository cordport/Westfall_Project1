import urllib3
import ftplib

def main():
    ftp = ftplib.FTP('drwestfall.net')
    ftp.login("ftp05", "student")
    print(ftp.getwelcome())
    ftp.retrbinary('RETR newFile', open('README', 'wb').write)
    #ftp.retrlines('LIST')
    ftp.quit()

main()




