from zad1 import *
from zad2 import wyodrebnij_hashtagi
from zad3 import wyodrebnij_emotikony

# zad1a
print(usun_liczby('Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'))

# zad1b
print(usun_znaczniki_html('<div><h2>Header</h2> <p>article<b> strong text</b> <a href="">link</a> </p></div> '))

# zad1c
print(usun_interpunkcje('''Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. 
Mauris egestas erat quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, 
tortor nisl facilisis leo, at tristique augue risus eu risus. '''))

# zad2
print(wyodrebnij_hashtagi('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. 
Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta
lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus.'''))

# zad3
print(wyodrebnij_emotikony('''To jest tekst :) zawierajacy emotikony :-) :> i smutne też ;< :( :-('''))
