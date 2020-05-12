

# this will replace the spaces in a string with '%20'

def URL():
    
    string = input('what is the URL?  ')
    
    # remove spaces after input
    string = string.strip(' ')
    
    # replace spaces 
    string = string.replace(" ", "%20")

    print(string)

URL()