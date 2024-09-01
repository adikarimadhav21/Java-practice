"""
Write a Python program to find the most frequent character in a string
"""

def most_freq():
    st="nnnaabbbbm"
    count_ch={}
    for ch in st:
        count_ch[ch]=count_ch.get(ch,0)+1
    print(count_ch.get)
    return max(count_ch,key=count_ch.get)


print(most_freq())

"""
Write a Python program to remove all duplicates from a string and return the result.
"""

def remove_dup():
    st="vvvbbhio"
    print("".join(sorted(set(st),key=st.index)))

remove_dup()

"""
Write a Python program to capitalize the first letter of each word in a sentence.
"""
def cap_wrd():
    sentence="hello how are you"
    words=sentence.split()
    new_sentence=" ".join( word.capitalize() for word in words)
    print(new_sentence)
cap_wrd()

"""
Write a Python program to find the longest word in a sentence.

"""
def longest():
    sentence="hello how are you peoples"
    words= sentence.split()
    lon=max(words,key=lambda x:len(x))
    print(lon)
longest()

"""
Write a Python program to find the second most frequent character in a string.
"""
def second_most():
    word="bbbbcccttyyyyy"
    count_ch={}
    for chr in word:
        count_ch[chr]=count_ch.get(chr,0)+1
    sort_count= sorted(count_ch.items(),key=lambda x:x[1],reverse=True)

    print(sort_count[1][0]) if len(sort_count)>=2 else print("not valid")
second_most()

"""
Write a Python program to check if a string contains only unique characters.

"""

def check_uniq():
    strn="aabnvj"
    print("yes") if len(set(strn))==len(strn) else print("no")
check_uniq()

