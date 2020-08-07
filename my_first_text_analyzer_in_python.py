exampleText = "\"Ornhgvshy vf orggre guna htyl.\nRkcyvpvg vf orggre guna vzcyvpvg.\nFvzcyr vf orggre guna pbzcyvpngrq.\nSyng vf orggre guna arfgrq.\nFcenfr fv orggre guna qrafr.\nErnqnovyvgl pbhagf.\nFcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.\nNygubhtu cenpgvpnyvgl orgnf chevgl.\nReebef fubhyq arire cnff fvyragyl.\nHayrff rkcyvpvgyl fvyraprq.\nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.\nGurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.\nNygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.\nAbj vf orggre guna arrire.\nNygubhtu arire vf bsgra orggre guna *evtug* abj.\nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\nVs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!\"\n"
print("Here's example text:\n\n" + exampleText)

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print("The number of the same character specified in the text is analyzed below.")
char_chosen = input("Choose a character:\n")
print("The number of " + char_chosen + " is: " + str(count_char(exampleText, char_chosen)))
print("\nHere's a list of percentages by character:\n")
for char in exampleText:
    perc = 100 * count_char(exampleText, char) / len(exampleText)
    print("{0} - {1}%".format(char, round(perc, 2)))
