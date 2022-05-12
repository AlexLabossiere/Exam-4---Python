#!/usr/bin/env python3

import pandas as pd
#need to import this first, or else code wont work at all
def main():   #last function will call back to here to start it all
    '''main functuon to open your file with lines of sequences'''
    my_file = open("sampledna.txt.txt", "r")   #opens files on python
    sequence = my_file.read().rstrip(';').splitlines()  # read file lines, split into lines/list, takes away ';'
    for item in sequence:
        panda_stuff(item)
        LC(item)
        #running each item in the list of sequences to panda function (this starts everything)
        msg = f'sequence is {item} and is {len(item)} characters long'  #fun informational message
        print(msg)  #printing message on commandline (tells you which sequences is what and at what length

def possible(k,sequence):
    '''Gives you possible kmers within a given sequence'''
    return min((len(sequence))-k+1,
               4**k)  #runs after panda calls for possible, gives possible kmers for given sequence
#takes minimum of length of the sequences in our list, an subtract them from given k and + 1


def observed_kmers(k,sequence):
    '''Gives you actual observed kmers within sequence'''
#need a listof kmers that can be observered
#extra examples of kmer and source of for loop found in README
    observed = []   #this is out list of obeservation, its empty right now, we want to make a list of observations
    kmers = len(sequence) - k + 1  #gives us the possible kmers for sequence
    for length in range(kmers):    #when uses kmer for start length of of sequence
        kmers = sequence[length:length + k]  #this cuts sequence into specific kmer, k value from panda loop
        if kmers not in observed:
            observed.append(kmers)  #places unique sequences within obsered list
    return(len(observed))  #returns length of said observervations made in list

def panda_stuff(sequence): #main function calls this function
    '''creates dataframe based off k, possible and observed kmers'''
#we want a list of all of our things (3) k numbers, observations, possibilties
#want a list that goes through size K that is limited by sequence
#this K is looped +1 until there is no more sequence
    data = []
    k = 1
    while k <= len(sequence):
        data.append([k,
                     observed_kmers(k,sequence),#we have out list K (which is growing per loop)
                     possible(k,sequence)]) #which calls for observed kmers and possible kmers, which starts the calcuations from the other functions
        k += 1
      # if k >= 9:
       #    break
#put this here as a limit, sequences can be very long, (one of outs is 55 length so take away the # to have a limit
    df = pd.DataFrame(data,
                      columns = ('k',
                                 'observed',
                                 'possible')) #makes dataframe from pandas, add columns for the numbers calculated

   #print(df) just did this to view output
    df.to_csv('./'+sequence+'.txt') #makes each of your panda tables to CSVs to be read

def LC(sequence):
    '''Finds Linguistic complexisty of given string'''
    sum_observed = 0  #instead of an empty list its a no value
    sum_possible = 0 # same for another value
    k = 1 #same trick as above using a loop of k values
    while k <= len(sequence):
        sum_observed += observed_kmers(k,sequence)  #this adds the numbers to the value listed above
        sum_possible += possible(k,sequence)
        k += 1
    msg = f' Language complexity of {sequence} is {(sum_observed/sum_possible)}'
    print(msg) #prints value of LC


if __name__=="__main__": #python reads line to line, this is the last line and will start the cascade
    main()
