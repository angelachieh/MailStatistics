from pattern.web import Mail, GMAIL, SUBJECT
import operator
import getpass
import re
import os.path


def mostUsedWordsInFolder(mail, folder):
    if folder not in mail.folders:
        print("ERROR: Folder doesn't exist!")
        return

    print 'Reading ' + str(mail.folders[folder].count) + ' emails from ' + folder

    # Create word count database. A dict where key=word value = word count
    database = {}

    for i in range(mail.folders[folder].count):
        print 'Reading mail ' + str(i+1) + ' of ' + str(mail.folders[folder].count)
        message = mail.folders[folder].read(i, attachments=False, cached=True)
        
        # Email subject 
        words = message.subject.split()
        countWords(database, words)

        # Email body
        words = message.body.split()
        countWords(database, words)

    printDatabase(sorted(database.iteritems(), key=operator.itemgetter(1), reverse=True))
        

def countWords(database, words):

    # List of regular expressions to be filtered from the results
    filterlist = [ r".*\@.*\.com.*" , r"[0-9]*\/[0-9][0-9]?\/[0-9]*", r"https?\:\/\/.*" , r"^\=\?.*" ]

    for word in words:
        # Remove punctuation signs (. , !)
        word = word.lstrip('(>"*')
        word = word.rstrip('.!;,?)"*:')

        # Filter according to expressions in "filterlist"
        inFilter = False
        for regexp in filterlist:
            if re.search(regexp, word):
               inFilter = True
               continue

        if inFilter:
            continue

        # Word can become empty after strip
        # Also ignores words with 3 or less characters
        if word != "" and len(word) > 3:            
            if word in database:
                database[word] += 1
            else:
                database[word] = 1


def printDatabase(database):

    # Increment output[i].txt until a non-existent filename is found
    j = 0
    while True:
        filename = 'output' + str(j) + '.txt'
        if os.path.exists(filename):
            j += 1
        else:
            break

    fileOutput = open(filename, 'w')

    for key, value in database:
         fileOutput.write(key.encode('utf-8') + ' -> ' + str(value) + '\n')

    fileOutput.close()


def main():
    username = raw_input('Enter Gmail username: ')
    password = getpass.getpass('Enter Gmail password: ')
    folder = raw_input('Enter Folder name: ')
    gmail = Mail(username, password, service=GMAIL)
    mostUsedWordsInFolder(gmail, folder)


if __name__ == "__main__":
    main()


