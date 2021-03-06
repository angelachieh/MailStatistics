# Mail Statistics
This small Python script retrieves all emails from a Label on gmail and
generates a statistic on the ocurrence of the words.
This script uses the Pattern web mining module found in:
http://www.clips.ua.ac.be/pages/pattern

##Installation instructions
- Clone this project
- Download Pattern module (direct link to version 1.4 -
  http://www.clips.ua.ac.be/media/pattern-1.4.zip)
- Copy pattern-1.4.zip to the project folder (inside MailStatistics)
- unzip pattern-1.4.zip

##Usage
- On terminal, run: "python mailStatistics.py"
- It will ask your gmail login, password
- When asked for Folder name, insert Label name from gmail

##Changelog
- 03.05.2011 [angela]
    - Use of email package instead of mimify (deprecated) to decode MIME headers
- 05.03.2011 [cheng]
    - Removed unused filters
    - Additional filterlist for words in subject
    - Filter tags in subjects
    - Encode subject words to UTF-8 to keep coherence
    - Auto convert folder name to lower case
- 04.03.2011 [angela]
    - Reply lines are now identified by the names and email addresses of the authors of the topic's previous messages (all reply formats)
    - Headers in MIME encoded-word format are decoded
    - Words are split by whitespaces, filtered and then split by punctuation signs
    - Filterlist updated to take into account more general email addresses
    - Changed some variables' names
- 01.03.2011 [cheng]
    - Cache temporarily disabled (temporary workaround for known issue 1)
- 01.03.2011 [angela]
    - Ignore quoted text in reply email (limited to two reply formats commonly found in Gmail with English language settings)
    - Split words separated by punctuation signs without spaces
    - Ignore subject of reply email
    - User can choose if search is case sensitive or insensitive
    - Added function: encode to utf8
- 27.02.2011 [helton]
    - Code cleanup
- 26.02.2011 [cheng]
    - getpass to hide password input on the screen
    - Increment output[i].txt when filename already exists
    - Added leading and trailing " to the punctuation signs to be stripped from the words
    - Filter List: list of expressions to be filtered from the results (regular expressions)
    - Initial filters: email address, date, URL
- 26.02.2011 [helton]
    - Added README
- 26.02.2011 [helton]
    - Ignores words with 3 or less characters
- 26.02.2011 [helton]
    - First release

##Known Issues
1. Cached emails are not updated with Gmail (workaround implemented)
2. Cannot read HTML content inside emails (emails with formatted text)