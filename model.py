#
# textmodel.py
#
# TextModel project!
#
# Name(s): Grace Williams
#

import math
import string 
from porter import create_stem
class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        # 
        # The text in the model, all in a single string--the original
        # and "cleaned" versions.
        #
        self.text = ''            # No text present yet
        self.cleanedtext = ''     # Nor any cleaned text yet
                                  # ..(cleaned == only letters, all lowercase)

        #
        # Create dictionaries for each characteristic
        #
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths
        
        # Create another dictionary of your own
        #
        self.numvowels = {}     # For counting vowels

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = f'Words:\n{str(self.words)}\n\n'
        s += f'Word lengths:\n{str(self.wordlengths)}\n\n'
        s += f'Stems:\n{str(self.stems)}\n\n'
        s += f'Sentence lengths:\n{str(self.sentencelengths)}\n\n'
        s += f'Number of vowels:\n{str(self.numvowels)}\n\n'
        s += '+'*55 + '\n'
        s += f'Text[:42]    {self.text[:42]}\n'
        s += f'Cleaned[:42] {self.cleanedtext[:42]}\n'
        s += '+'*55 + '\n\n'
        return s

    # We provide two text-adding methods (functions) here:
    def addRawText(self, text):
        """addRawText accepts self (the object itself)
                      and text, a string of raw text to add.
           Nothing is returned from this method, but
           the text _is_ added.
        """
        self.text += text 
        self.cleanedtext += self.cleanString(self.text) 

    # The second one adds text from a file:
    def addFileText(self, filename):
        """addFileText accepts a filename.
            
           Nothing is returned from this method, but
           the file is opened and its text _is_ added.

           If the file is not present, it will crash!
        """
        f = open(filename, 'r', encoding='latin1')
                               # The above may need utf-8 or utf-16, depending
        text = f.read()        # Read all of the contents into text 
        f.close()              # Close the file
        self.addRawText(text)  # Uses the previous method!

    # Include other functions here.
    # In particular, you'll need functions that add to the model.

    def makeSentenceLengths(self):
        """Creates the dictionary of sentence lengths
               should use self.text, because it needs the punctuation!
        """
        s = str(self.text)
        LoW = s.split()
        count = 0 

        for x in LoW:
            count += 1
            if x[-1] == '.' or x[-1] == '?' or x[-1] == '!':
                if count in self.sentencelengths:
                    self.sentencelengths[count] += 1
                else: 
                    self.sentencelengths[count] = 1 
                count = 0 


    def cleanString(self, s):
        """Returns the string s, but
           with only ASCII characters, only lowercase, and no punctuation.
           See the description and hints in the problem!
        """
        s = s.encode("ascii", "ignore")
        s = s.decode()
        
        result = s.lower()    # Not implemented fully: this just lower-cases     
                   
        for c in result: 
            if c in string.punctuation:
                result = result.replace(c, '')
        return result
    
    def makeWordLengths(self):
        """Creates the dictionary of word length features.
               Uses self.cleanedtext
        """
        s = self.cleanedtext 
        LoW = s.split() 
        
        for x in LoW:
            count = len(x)
            if count in self.wordlengths:
                self.wordlengths[count] += 1
            else: 
                self.wordlengths[count] = 1 
            count = 0 
    
    def makeWords(self):
        """Creates the dictionary of words.
               Uses self.cleanedtext
        """
        s = self.cleanedtext
        LoW = s.split() 

        for x in LoW:
            if x in self.words:
                self.words[x] += 1 
            else: 
                self.words[x] = 1 
    
    def makeStems(self):
        """Creates the dictionary of stems of words.
               Uses self.cleanedtext
        """
        s = self.cleanedtext
        LoW = s.split()

        for x in LoW:
            z = create_stem(x)
            if z in self.stems:
                self.stems[z] += 1 
            else: 
                self.stems[z] = 1 
    
    def makeNumberofVowels(self):
        """Creates the dictionary of vowels from words.
               Uses self.cleanedtext
        """
        s = self.cleanedtext
        v = 'aeiou'
        
        for c in v:
            self.numvowels[c] = 0
        for x in s:
            if x in v:
                self.numvowels[x] += 1
    
    def normalizeDictionary(self,d):
        """accepts any single one of the model dictionaries d 
            Returns a normalized dictionary.
        """
        nd = {}
        sum = 0
        for x in d:
           sum += d[x] 

        if sum == 0:
            for z in d:
                nd[z] = 0
            return nd
        
        for y in d:
            nd[y] = d[y]/sum
            
        return nd  
    
    def smallestValue(self, nd1, nd2):
        """accepts any two model dictionaries nd1 and nd2
            Returns the smallest positive non-zero value.
        """
        c = 0
        for w in nd1:
            c = nd1[w]
            break 
        for x in nd1:
            if nd1[x] < c:
                c = nd1[x]

        for y in nd2:
            if nd2[y] < c:
                c = nd2[y]
        
        return c
    
    def compareDictionaries(self, d, nd1, nd2):
        """computes the log-probability that the dictionary d is from 
            the distribution of data in the normalized dictionary nd1 
            and the log-probability that dictionary d arose from the distribution 
            of data in normalized dictionary nd2
            Returns both log-probability values.
        """
        epsilon = 0.5*self.smallestValue(nd1, nd2) 
        total1 = 0
        total2 = 0
        for k in d:
            if k in nd1:
                total1 += d[k]*math.log(nd1[k])
            
            else: 
                total1 += d[k]*math.log(epsilon)


            if k in nd2:
                total2 += d[k]*math.log(nd2[k])
            
            else: 
               total2 += d[k]*math.log(epsilon)

        return [total1, total2]
    
    def createAllDictionaries(self):
        """Create out all five of self's
           dictionaries in full.
        """
        self.makeSentenceLengths()
        self.makeWords()
        self.makeStems()
        self.makeWordLengths()
        self.makeNumberofVowels()
    
    def compareTextWithTwoModels(self, model1, model2):
        """prints the comparitve results of the log probabilities
            for all five dictionaries.
        """
        nd1 = self.normalizeDictionary(model1.words)
        nd2 = self.normalizeDictionary(model2.words)
        LogProbs1 = self.compareDictionaries(self.words, nd1, nd2)
        print("Words:\nModel 1 has the log probability", LogProbs1[0], 
              "\nModel 2 has the log probability", LogProbs1[-1], "\n")

        nd1 = self.normalizeDictionary(model1.wordlengths)
        nd2 = self.normalizeDictionary(model2.wordlengths)
        LogProbs2 = self.compareDictionaries(self.wordlengths, nd1, nd2)
        print("Word lengths:\nModel 1 has the log probability", LogProbs2[0], 
              "\nModel 2 has the log probability", LogProbs2[-1], "\n")

        nd1 = self.normalizeDictionary(model1.stems)
        nd2 = self.normalizeDictionary(model2.stems)
        LogProbs3 = self.compareDictionaries(self.stems, nd1, nd2)
        print("Stems:\nModel 1 has the log probability", LogProbs3[0], 
              "\nModel 2 has the log probability", LogProbs3[-1], "\n")

        nd1 = self.normalizeDictionary(model1.sentencelengths)
        nd2 = self.normalizeDictionary(model2.sentencelengths)
        LogProbs4 = self.compareDictionaries(self.sentencelengths, nd1, nd2)
        print("Sentence lengths:\nModel 1 has the log probability", LogProbs4[0], 
              "\nModel 2 has the log probability", LogProbs4[-1], "\n")


        nd1 = self.normalizeDictionary(model1.numvowels)
        nd2 = self.normalizeDictionary(model2.numvowels)
        LogProbs5 = self.compareDictionaries(self.numvowels, nd1, nd2)
        print("Number of Vowels:\nModel 1 has the log probability", LogProbs5[0], 
              "\nModel 2 has the log probability", LogProbs5[-1], "\n")
        
        Model1sum = (LogProbs1[0] + LogProbs2[0] + LogProbs3[0] + LogProbs4[0] + LogProbs5[0])
        Model2sum = (LogProbs1[-1] + LogProbs2[-1] + LogProbs3[-1] + LogProbs4[-1] + LogProbs5[-1])
        print("The sum of weighted probabilities for Model 1 is", Model1sum, 
              "\nThe sum of weighted probabilities for Model 2 is", Model2sum)
        if Model1sum > Model2sum:
            print("\nModel 1 is the better match!")
        else: 
            print("Model 2 is the better match!")
        




      







                

            



                
            




            



# And let's test things out here...
TMintro = TextModel()

# Add a call that puts information into the model
TMintro.addRawText("""This is a small sentence. This isn't a small
sentence, because this sentence contains more than 10 words and a
number! This isn't a question, is it?""")

# Put the above triple-quoted string into a file named test.txt, then run this:
TMintro.addFileText("test.txt")   # "comment in" this line, once the file is created

# Print it out
print("TMintro is", TMintro)


# Add more calls - and more models - here:
test_text = """This is a small sentence. This isn't a small
sentence, because this sentence contains more than 10 words and a
number! This isn't a question, is it?"""
TM = TextModel()
TM.addFileText("test.txt")
assert TM.text == test_text

# Create all of the dictionaries
TM.makeSentenceLengths()
TM.makeWordLengths()
TM.makeWords()
TM.makeStems()
TM.makeNumberofVowels()

# Let's see all of the dictionaries!
print("The text model has these dictionaries:")
print(TM)





# 3 Example Test Files:
print(" +++++++++++ Model1 +++++++++++ ")
TM1 = TextModel()
TM1.addFileText("train1.txt")
TM1.createAllDictionaries()  # provided in hw description
print(TM1)

print(" +++++++++++ Model2 +++++++++++ ")
TM2 = TextModel()
TM2.addFileText("train2.txt")
TM2.createAllDictionaries()  # provided in hw description
print(TM2)


print(" +++++++++++ Unknown1 text +++++++++++ ")
TM_Unk1 = TextModel()
TM_Unk1.addFileText("unknown1.txt")
TM_Unk1.createAllDictionaries()  # provided in hw description
print(TM_Unk1)

print(" +++++++++++ Unknown2 text +++++++++++ ")
TM_Unk2 = TextModel()
TM_Unk2.addFileText("unknown2.txt")
TM_Unk2.createAllDictionaries()  # provided in hw description
print(TM_Unk2)