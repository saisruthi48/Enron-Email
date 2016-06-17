#!/usr/bin/python
from optparse import OptionParser
import os.path
import re

regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
def file_to_str(filename):
    """Returns the contents of filename as a string."""
    with open(filename) as f:
        return f.read().lower() # Case is lowered to prevent regex mismatches.

def get_emails(s):
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [File]...")
    # No options added yet. Add them here if you ever need them.
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        #exit(1)

    for arg in args:
        if os.path.isfile(arg):
            for email in get_emails(file_to_str(arg)):
                #output = open("email.csv","wb")
                #writer = csv.writer(output,delimiter='\t',quotechar = '""' , quoting = csv.QUOTE_ALL)
                count = 1
                email_received_sent = {}
                email_received_sent = {email:count}
                for id in email_received_sent:
                    email_received_sent[email] += count
                    print ("{0}\t{1}".format(id,count))
        #else:
            #print '"{}" is not a file.'.format(arg)
