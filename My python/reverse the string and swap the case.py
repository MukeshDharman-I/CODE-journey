#input is (AWsomE Is CODiNg)
#output should be(codInG iS awSOMe)
#reverse the string and swap its case
def reverse_words_order_and_swap_cases(s):
    swaped=s.swapcase()
    string=""
    splitting=swaped.split()#splits the words in string within list  
    reversed=splitting[::-1]
    for i in reversed:
        string+=i+" "
    print(string)  #answer is from this statement  
    wrd=" ".join(reversed)# this statement is just to know about join function
    print(wrd)#empty string(" ") in the above statement is to fill the spaces
word="AWsomE Is CODiNg"
reverse_words_order_and_swap_cases(word)
