import urllib3
import ftplib

def main():
    ftp = connect("drwestfall.net")
    login(ftp, "ftp05", "student")
    print(ftp.getwelcome())
    download_BIN(ftp, "newFile")
    disconnect(ftp)

#*********************
#connects a new ftp obj to the given url
#url is a valid string containing the file servers url
#If error returns None
#return is the new ftp obj initialized to the url
#*********************
def connect(url):
    try:
        ftp = ftplib.FTP(url)
    except ftplib.all_errors:
        #What should be returned if we have an error? we can't just return the ftp obj... maybe None?
        return None
    return ftp


#*********************
#logs into the file server using the provided userName and password
#ftpObj is the current working ftp server object
#userName is a str containing the user name
#password is the password
#RETURN is False if error occurs else true
#*********************
def login(ftpObj, userName, Password):
    try:
        ftpObj.login(userName, Password)
    except ftplib.all_errors:
        return False
    return True


#*********************
#Downloads binary version of file (for use with non text based files)
#(i.e. JPG GIF PDF) SHOULD NOT BE USED FOR TXT or DOCX
#ftpObj is the current working ftp server object
#fileName is the file you want downloaded
#THIS ASSUMES YOU ARE IN THE CORRECT DIR
#RETURN is False if error occurs else true
#*********************
def download_BIN(ftpObj, fileName):
    try:                            #we need some way to monitor the progress... any ideas? compaire the file size? is there a built in method?
        ftpObj.retrbinary('RETR '.join(fileName), open(fileName, 'wb').write)
    except ftplib.all_errors:
        return False                #we should change this to actuall tell the error
    return True


#*********************
#Disconnects from the ftp server, steralizes ftpObj
#Should be called whenever switching servers or closing the program
#ftpObj is a active ftp connection object
#if there is an error return False
#if successful, sets ftpObj to None and returns true
#*********************
def disconnect(ftpObj):
    try:
        ftpObj.close()
    except ftplib.all_errors:
        return False
    ftpObj = None
    return True






#MAKE SURE THIS IS THE END OF THE DOCUMENT. DO NOT MOVE OR ADD AFTER THIS POINT*********************************************************************
main()
#testing if visual studio works