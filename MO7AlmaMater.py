# Write a program that reads a file containing the first two lines of the Penn State Alma Mater's first verse. Read each line, then complete the rest of the verse by adding the final two lines (Making sure that they are on separate lines). Then send it to the output file AlmaMaterOut.txt. The input file is AlmaMater.txt, which contains:
#
# For the glory of old State,
#
# For her founders strong and great,
#
#
# then the program produces the output file
#
# Follow this pseudo-code:
#
# MAIN FUNCTION
#     Call read_file() and store the returned value in 'verse'
#     Pass 'verse' to write_file()
#
# FUNCTION read_file()
#     Set 'filename' to "AlmaMater.txt"
#     Initialize an empty list 'verse_list'
#     Open 'filename' for reading as 'inf'
#     Initialize 'count' to 0
#     FOR each line in 'inf':
#         Append the line to 'verse_list'
#         Increment 'count' by 1
#     Call alma_mater_complete_verse() with 'verse_list'
#     Close 'inf'
#     RETURN 'verse_list'
#
# FUNCTION alma_mater_complete_verse(verse)
#     Append "\nFor the future that we wait," to 'verse'
#     Append "\nRaise the song, Raise the song." to 'verse'
#     RETURN 'verse'
#
# FUNCTION write_file(verse)
#     Open "AlmaMaterOut.txt" for writing as 'outf'
#     FOR each index 'i' from 0 to length of 'verse':
#         Write the element at 'verse[i]' to 'outf'
#     Close 'outf'
#
# CALL main()

def write_file(verse):
    """
    Receives a list with all lines in the verse and writes them into an output file
    :param verse: list with a complete verse
    """
    #open file for writing
    outFile = open("AlmaMaterOut.txt", "w")
    #write content of the list into the file
    for line in verse:
        outFile.write(line)
    outFile.close()

def alma_mater_complete_verse(verse):
    """
    receives list, and add two lines
    :param verse: list with first two lines
    """
    verse.append("\nFor the future that we wait,")
    verse.append("\nRaise the song, Raise the song.")

def read_file():
    """
    reads an input file, completes the verse, and return a list with all the content
    :return: list with a complete verse
    """
    #open file for reading
    inputFile = open("AlmaMaterin.txt", "r")

    #create an empty list
    verse_list = []

    #read content of the file into the list
    for line in inputFile:
        verse_list.append(line)

    #alternative of line 53-54:
    #verse_list = inputFile.readlines()

    #complete verse by calling the function
    alma_mater_complete_verse(verse_list)

    #close the file
    inputFile.close()

    #return list
    return verse_list

def main():
    verse = read_file()
    write_file(verse)
main()