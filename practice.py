import time

def main():
    print("This is a game of survival. Your choices will decided wether you live or die.")
    time.sleep(2)
    print("You wake up on a beach and you are stranded on a deserted island. All you can remember is the feeling of waves crashing on your face.")
    time.sleep(2)
    print("Scared, hungry, thirsty, and cold you start to think about what to do to survive")
    time.sleep(2)
    choice = input("You can only do one thing before it's too dark. Do you first: 1. stay where you are and wait to be rescued, 2. go hunt for food, or 3. look for clean water")
    if choice == 1:
        print("You go through the night with no food, water, shelter, fire and you get a few hours of sleep")
        time.sleep(2)
        a = input("Do you: 1. stay where you are and wait to be rescued, 2. go hunt for food and look for clean water")
        if a == 1:
            print("You look at horizon as you take your final breaths waiting for help.")
            time.sleep(2)
            print("Finally, your body shuts down. You are dead.")
            time.sleep(2)
        elif a == 2:
            print("You find river with water and some coconuts.")
            time.sleep(2)
            print("You head back to the beach and you see a large python.")
            time.sleep(2)
            b = input("Do you: 1. Fight the python or 2. Run to the beach")
            if b == 1:
                time.sleep(2)
                print("The python bit you before you made a move. You died from poison")
            elif b == 2:
                time.sleep(2)
                print("You didn't run fast enough. The python bit you before you could make a move. You died of poison")
            else:
                time.sleep(2)
                print("That is not an option, restart.")
        else:
            time.sleep(2)
            print("That is not an option, restart.")
    elif choice == 2:
        time.sleep(2)
        print("You find a deer next to a river.")
        time.sleep(2)
        c = input("Do you: 1. Sneak up on the deer, 2. Run at the deer, or 3. go back to the beach")
        if c == 1:
            time.sleep(2)
            print("You hide in a bush and finally jump at the deer.")
            time.sleep(2)
            print("Sadly the deer got away and you're forced to go back to the beach.")
            time.sleep(2)
            print("On the way back you see a bear growling at you.")
            time.sleep(2)
            d = input("Do you: 1. Fight the bear or 2. Run to the beach")
            if d == 1:
                time.sleep(2)
                print("The bear tore you apart before you could land a punch. You are dead")
            elif d == 2:
                time.sleep(2)
                print("Running for your life you lose track of where you are and you see a village with people. You are saved! You Win!")
            elif d == 3:
                time.sleep(2)
                print("You walk back the beach and it's morning. Without food, water, and sleep your body starts to shut down.")
            else:
                time.sleep(2)
                print("That is not an option, restart.")
        elif c == 2:
            time.sleep(2)
            print("You scare the deer off and then you look up at the sky. Coconuts on the trees catches your eye.")
            time.sleep(2)
            print("You bring as many coconuts to the beach and you look at the river.")
            time.sleep(2)
            e = input("Do you: 1. Drink the water straight out of the river or do you 2. Wait to boil the water when you make the fire tomorrow.")
            if e == 1:
                time.sleep(2)
                print("You drink and drink and drink. Feeling better you walk back to the beach.")
                time.sleep(2)
                print("Suddenly, you feel a pain in your stomach. The water wasnt clean. You died.")
            elif e == 2:
                time.sleep(2)
                print("you sleep through the night thirsty but the next day you make a fire and drink your clean boiled water.")
                time.sleep(2)
                f = input("Do you: 1. explore a cave or 2. wait to be rescued?")
                if f == 1:
                    time.sleep(2)
                    print("You walk in the cave in search of something that is interesting.")
                    time.sleep(2)
                    print("You see a treasure chest and instantly go for it.")
                    time.sleep(2)
                    print("Suddenly the room starts shaking and bolders start falling from the ceiling.")
                    time.sleep(2)
                    print("One of the bolders hit you in the head and you are dead")
                elif f == 2:
                    time.sleep(2)
                    print("You wait for any sign of human life to appear")
                    time.sleep(2)
                    print("You wait and wait and wait but nothing appears.")
                    time.sleep(2)
                    g = input("You see a ship out in the distance. Do you: 1. Try to run and swim toward it or 2. Or stay on the beach and hope they notice the smoak from your fire?")
                    if g == 1:
                        time.sleep(2)
                        print("You run into the ocean and you trip on a rock")
                        time.sleep(2)
                        print("The ocean waves were to strong for you and you drowned. You are dead.")
                    elif g == 2:
                        time.sleep(2)
                        print("The boat turns in your direction. They saw your smoak. You survived! You win!")
                    else:
                        print("That is not an option, restart.")
                else:
                    print("That is not an option, restart.")
            else:
                print("That is not an option, restart.")
        elif c == 3:
            time.sleep(2)
            print("You run back to the beach but now you don't have any food or water. Your body shuts down and you died.")
        else:
            print("That is not an option, restart.")
    elif choice == 3:
        time.sleep(2)
        print("You find a river with clear water.")
        time.sleep(2)
        e = input("Do you: 1. Drink the water straight out of the river or do you 2. Wait to boil the water when you make the fire tomorrow.")
        if e == 1:
            time.sleep(2)
            print("You drink and drink and drink. Feeling better, you walk back to the beach.")
            time.sleep(2)
            print("Suddenly, you feel a pain in your stomach. The water wasnt clean. You died.")
        elif e == 2:
            time.sleep(2)
            print("you sleep through the night thirsty but the next day you make a fire and drink your clean boiled water.")
            time.sleep(2)
            h = input("Do you now 1. Go hunt for food or 2. Build a shelter?")
            if h == 1:
                time.sleep(2)
                print("You wander around the island and you stumble upon a bear.")
                time.sleep(2)
                i = input("Do you 1. Fight the bear or 2. run away from the bear.")
                if i == 1:
                    time.sleep(2)
                    print("The bear slashes you in the face and you bleed out to death")
                elif i == 2:
                    time.sleep(2)
                    print("You start to build a shelter, but super hungry you finish it halfway.")
                    time.sleep(2)
                    print("Luckily there was a ship that caught on the smoak of the fire.")
                    time.sleep(2)
                    print("You are saved you win!")
                else:
                    print("That is not an option, restart.")
            elif h == 2:
                time.sleep(2)
                print("You start to build a shelter, but super hungry you finish it halfway.")
                time.sleep(2)
                print("Luckily there was a ship that caught on the smoak of the fire.")
                time.sleep(2)
                print("You are saved you win!")
            else:
                print("That is not an option, restart.")
main()