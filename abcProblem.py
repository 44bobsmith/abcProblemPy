def canMakeWord():
    blocksList = [['B','O',False],['X','K',False],['D','Q', False],['C','P',False],['N','A',False],['G','T',False],['R','E',False],['T','G',False],['Q','D',False],['F','S',False],['J','W',False],['H','U',False],['V','I',False],['A','N',False],['O','B',False],['E','R',False],['F','S',False],['L','Y',False],['P','C', False],['Z','M',False]];
    userWord = raw_input('What is your word to test please?')
    howManyTrue = 0
    for letter in userWord: #cycle thru each letter of the word

        for block in blocksList:
            print letter
            if block[2] == False:
                if block[0] == letter.upper() or block[1] == letter.upper(): #check index 0 and 1 in each block against the current letter of the word
                    block[2] = True
                    howManyTrue += 1
                    print block
                    print howManyTrue
                    break


    if howManyTrue < len(userWord):
        canMakeWordTest = False
    else:
        canMakeWordTest = True

    print 'can make word: ' + str(canMakeWordTest)


canMakeWord()
