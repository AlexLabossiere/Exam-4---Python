from exam4code import *

def possible():
    assert possible(9,'ATTTAGGTT') == 1

def observed_kmers():
    assert possible(9,'ATTTAGGTT') == 1

#does not work, do not know why, followed the tutorials exactly like it was shown and no forums give simple reasons as
#to why this does not work
#functions will work individually if fed a given parameter
# but python cannot find file, despite said file being in the SAME folder
# error that pops up is -->> ModuleNotFoundError: No module named 'exam4code'
#stackoverflow seems to have any and every explaination except for mine but i dont know how to get python to see
#the functions within the script
