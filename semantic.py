# This is the code that I adapted from Hyperion examples to further test the difference as the task required. 

import spacy

nlp = spacy.load('en_core_web_md')

#The Hyperion Task Book code adapted to include milk as one of the tokens so as to see if it produces an interesting result. 
tokens = nlp('cat apple monkey banana milk ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


nlp = spacy.load('en_core_web_sm')
nlp1 = spacy.load('en_core_web_md')

complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]



print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))


print("-------------Complaints similarity---------------")

for token in complaints:
    token = nlp1(token)
    for token_ in complaints:
        token_ = nlp1(token_)
        print(token.similarity(token_))


print('''\nThoughts: 
    I noticed that scores from 0-1 when using en_core_web_sm are generally lower than when using en_core_web_md. I also notied that using 
    en_core_web_sm for a similarity check produces a warning form the developers.

    Concerning the monkey and banana example, its interesting that the score is higher, so considers that there is a similariy, whereas the score 
    is lower for Cat and Banana. Its interesting because the things in themselves are not the same type, for instance both Monkeys and Cats are mammals. 
    That suggests that spacy doesn't just match by type of object / entity but also some sort of frequency of known association. However, to say that a 
    Monkey and a Banana are similar is bad description, so presumably it is better to suggest that Monkey and Banana have a high degree of association. 
    I conducted a further test by adding milk to the tokens, and sure enought Moneky and Milk had a relatively low similiarity, campared to Bananas for instance.
    And Cats and Mile had a slightly higher similarity than cat and banana. 

    I also noticed that using en_core_web_sm for similarity tests of strings produces a UserWarning "[W007] The model you are using has no word vectors loaded." 
    Which is a shame because actually sm produces quite an accurate result.  ''')

# Code ends