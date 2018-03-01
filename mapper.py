
import sys
import re

def read_input(file):
    for line in file:
        # here we need to remove all the special characters from the file
        #for the purpose of which I am using a regular expression
        line = re.sub('[^A-Za-z0-9]+', ' ', line)
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        # we need to check whether the line contains only 1 word or more
        #if the line contains only single word, treat it as pair
        if len(words)==1:
            a = words
            for word in a:
                print '%s%s%d' % (word,separator, 1)
        else:
            #if the line contains more than 1 words
            a = zip(words, words[1:])
            for word in a:
                print '%s %s%s%d' % (word[0],word[1],separator, 1)
        
if __name__ == "__main__":
    main()
