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
#Deletes a directory from the server
#ftpObj is the current working ftp server object
#directoryName is the directory you want deleted
#RETURN is False if error occurs else true
#*********************
def delete_Dir(ftpObj, dirName):
    try:
        if dir_Exists(ftpObj, dirName): #if the directory exists
            ftpObj.rmd(dirName) #remove the directory
            print("Directory: ", dirName, " deletion successful ") #print successful deletion message
        else: #otherwise, the directory does not exist
            print("Directory: ", dirName, " does not exist") #print directory DNE message
            return False
    except ftplib.all_errors: #an error occurred
        print("Directory: ", dirName, " deletion failed") #print failed deletion message
        return False #return false indicates deletion did not occur
    return True


#*********************
#Checks if directory exists (in current location)
#ftpObj is the current working ftp server object
#dir is the directory you want to check for existence
#THIS ASSUMES YOU ARE IN THE CORRECT DIR
#RETURN is True if the directory exists, False if it does not
#*********************
def dir_Exists(ftpObj, dirName):
    fileList = [] #list object to store all files
    ftpObj.retrlines('LIST', fileList.append) #append to list
    
    for file in fileList: #for every file/directory in the list (current location)
        if file.split()[-1] == dirName and file.upper().startswith('D'): # If the name matches and is a directory
            return True #directory found, return True
    return False #otherwise, directory not found, return False


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