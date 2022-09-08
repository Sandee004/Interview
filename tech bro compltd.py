bad_things=["kidnapping", "stealing"]
boss_levels=["Java", "C++", "C", "C+", "Machine Learning"]


def yes():
    print("Splendid. What languages do you work with? (Separate with a comma)")
    stack= input()
    
    if stack in boss_levels:
        print("Boss!! Teach me na")

    print("On a scale of 1-100, how passionate are you about tech?")
    passion_range= input()

    if int(passion_range) > 69:
        print("Wow.....You really love it. That's cool")
        print("What's your favourite thing about it?")
        fav= input()
        print("Alright")
        
    elif int(passion_range) >39:
        print("Hmm.....would you have rather chosen a different carrer path? What would you choose?")
        career_path= input()
        
        if career_path=="no":
            print("Alright then")
        else:
            print("Sounds good. It's a nice alternative")
    else:
        print("Ouch. What would you rather do?")
        alternative= input()
        print("Well......i guess that's okay as well.")



print("Hello, I'm Pydroid.")
name= input("What's your name? ")
print()


print("Alright " + name + ". Are you into tech too? (yes or no)")
choose_path= input()

if choose_path== "yes":
    yes()
    
            
else:
    print("What do you do then?")
    job= input()
    if job in bad_things:
        print("That's messed up bro")
    else:
        print("That's great.")


print("Nice to meet you " + name + ". Pydroid wishes you the best")