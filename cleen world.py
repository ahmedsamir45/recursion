#x = 'wwooorrrlldd'
#print(x[1:])
def cleanword(word):
    if len(word) ==1 :
        return word

    if word[0]== word[1]:
        print(f"print from condition {word}")
        return cleanword(word[1:])
        

    return word[0]+cleanword(word[1:])

print(cleanword("wwwoooorrrldd"))
