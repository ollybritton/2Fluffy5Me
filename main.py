#coding=utf-8
import time, os, sys, random
from datetime import datetime

class Random:
    def __init__(self):
        pass

    def integer(self, a, b):
        return random.randint(a, b)

    def choice(self, xs):
        return random.choice(xs)

    def name(self):
        names = ["Bubbles", "Bundles", "Bunny", "Buttercup", "Button", "Chipmunk", "Cinnamon", "Cuddles", "Daisy", "Dimples", "Hiccup", "Huggie", "Jellybean", "Jiggles ", "Jujube ", "Kitkat", "Lollipop ", "Marshmallow ", "Munchkin", "Nibbles", "Nugget", "Panda", "Peaches ", "Pickles", "Pixie ", "Pocket", "Schmoopy ", "Skittles ", "Snickers ", "Snowball", "Snuggles ", "Squiggle ", "Taffy", "Teacup", "Tipsy", "Twinkles", "Velvet", "Waffles", "Wiggles", "Winky", "Bambi", "Barbie", "Blossom", "Bluebell", "Calypso", "Cookie", "Cuddles", "Cupcake", "Daisy", "Electra", "Giggles", "Ginger", "Goldilocks", "Gumdrop", "Honeybee", "Jasmine", "Juliette", "Juniper", "Ladybug", "Lakshmi", "Misty", "Nutmeg", "Olympia", "Princess", "Ruby", "Tiara", "Tinkerbell", "Trixie", "Twinkle", "Venus", "Amigo", "Banjo", "Cosmo", "Crocket", "Donatello", "Electro", "Elvis", "Euripides", "Figaro", "Fonzie", "Galileo", "Geronimo", "Hendrix", "Hercules", "Hobbes", "Houdini", "Lancelot", "Mars", "Moses", "Ozzy", "Pharaoh", "Picasso", "Prince", "Rembrandt", "Romeo", "Rumi", "Simba", "Tarzan", "Wizard", "Zorro"]

        return self.choice(names)

    def mood(self):
        return 5 + self.integer(-2, 2)

    def health(self):
        return 9 + self.integer(-1, 1)

    def personality(self):
        activities = ["Pet", "Groom", "Clean", "Walk", "Go to the Park", "Dress Up", "Brush", "Listen to Music", "Take a Catnap", "Bird Watch", "Travel", "Zen Out", "Go Camping", "High-Five", "Watch TV", "Go to Work", "Chill Out"]

        likes = []
        hates = []

        for i in range(6):
            a = self.choice(activities)
            likes.append(a)

            del activities[activities.index(a)]


        for i in range(6):
            a = self.choice(activities)
            hates.append(a)

            del activities[activities.index(a)]

        passive = activities

        return {
            "likes": likes,
            "hates": hates,
            "passive": passive
        }

def clear():
    os.system("clear")

def sleep(amount):
    time.sleep(amount)

class Creature:
    def __init__(self, name, mood, health, personality):
        self.name = name
        self.mood = mood
        self.health = health

        self.personality = personality
        self.likes = personality["likes"]
        self.hates = personality["hates"]
        self.passive = personality["passive"]


    def evaluate(self, activity):
        if activity in self.likes:
            self.mood += Random.integer(1, 2)

        elif activity in self.hates:
            self.mood -= Random.integer(1, 2)

    def hp(self):
        return "♥"*self.health

    def mood_counter(self):
        return "✓"*self.mood + "✖"*(10 - self.mood)


class Util:
    def hp(self, amount):
        return "♥"*amount

    def health(self, amount):
        if amount < 0:
            phrases = ["You have killed your cat. It is dead. If it were alive now, I bet it would have choice words for you, young man. You should feel bad.", "...I'm not sure how to break it to you... but you've killed your cat.", "Your cat is now deader that the relationship you had with it."]

            print(Random.choice(phrases) + " (Press enter to accept fate and end game)", end = "")
            input()

            sys.exit()


        elif amount == 1:
            phrases = ["Your cat is on the brink of death.", "Your cat is very close to dying.", "Your cat sits on the edge of life and death. One final push could could knock it either way."]

        elif amount == 2:
            pass

        elif amount == 3:
            pass

        elif amount == 4:
            pass

        elif amount == 5:
            pass

        elif amount == 6:
            pass

        elif amount == 7:
            pass

        elif amount == 8:
            pass

        elif amount == 9:
            pass

        elif amount == 10:
            pass

        elif amount > 10:
            pass


def intro():
    while True:
        clear()
        print("██████╗ ███████╗██╗     ██╗   ██╗███████╗███████╗██╗   ██╗███████╗███╗   ███╗███████╗\n╚════██╗██╔════╝██║     ██║   ██║██╔════╝██╔════╝╚██╗ ██╔╝██╔════╝████╗ ████║██╔════╝\n █████╔╝█████╗  ██║     ██║   ██║█████╗  █████╗   ╚████╔╝ ███████╗██╔████╔██║█████╗  \n██╔═══╝ ██╔══╝  ██║     ██║   ██║██╔══╝  ██╔══╝    ╚██╔╝  ╚════██║██║╚██╔╝██║██╔══╝  \n███████╗██║     ███████╗╚██████╔╝██║     ██║        ██║   ███████║██║ ╚═╝ ██║███████╗\n╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝        ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝")
        print("Hello and Welcom to 2Fluffy5Me, a cat simulator for lonely people! (Press <ENTER> to continue) ", end = "")
        input()

        print("(Full Disclaimer: I don't have a cat, and have no idea what it's like)")
        print("--------\n")

        print("Anyway, shall we start? [Y]es, [n]o, [m]eow: ", end = "")
        start_bool = input().lower()

        if start_bool == "yes" or start_bool == "y" or start_bool == "":
            print("Puuuurrrrrfect! Let's get going! (Press <ENTER> to continue) ", end = "")
            input()
            break

        elif start_bool == "meow" or start_bool == "m":
            print("Claw-some! I see you're getting into the persona! Let's get ready to rumble! (Press <ENTER> to continue) ", end = "")
            input()
            break

        elif start_bool == "no" or start_bool == "n":
            print("Uhhhh wut? You start again and give me the CORRECT answer. (Press <ENTER> to continue) ", end = "")
            input()


def main():
    clear()

    r = Random()
    cat =  Creature(r.name(), r.mood(), r.health(), r.personality())

    inital_like = r.choice(cat.likes)
    inital_hate = r.choice(cat.hates)
    initial_passive = r.choice(cat.passive)

    known_likes = [inital_like]
    known_hates = [inital_hate]
    known_passive = [initial_passive]

    times = []

    print("Ok! Your cat has been generated! (Press <ENTER> to continue) ", end = "")
    input()

    print("Meet {}, your lovely cat!".format(cat.name) + " (Press <ENTER> to continue) ", end = "")
    input()

    print("Here's a breakdown:")
    print("Health: {}".format(cat.hp()))
    print("Mood: {}".format(cat.mood_counter()))

    print("")

    print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
    print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
    print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))
    print("(Press enter to continue) ", end = "")
    input()

    print("")

    print("Ok! Have fun you two! (Press enter to continue) ", end = "")
    input()

    while cat.health > 0:
        clear()

        if cat.health > 10:
            cat.health = 10

        if cat.mood > 10:
            cat.mood = 10

        try:
            # Has the program been left for more than a minute?
            if (times[-2] - times[-1]).total_seconds() > 60:
                cat.health -= 1

        except:
            pass

        if cat.mood == 2:
            # Cats with mood 2 or lower self harm every turn.
            cat.health -= 1

        elif cat.mood == 1:
            cat.health -= 2

        elif cat.mood <= 0:
            print("Cat: Meow meow meow!")
            print("Cat (Translated): I'm tired of your sh*t! I'm f**king leaving! Bye b*tch!")
            print("(Press enter to accept your rejection) ", end = "")
            input()

            sys.exit()


        print("Your cat:")
        print("Health: {}".format(cat.hp()))
        print("Mood: {}".format(cat.mood_counter()))

        print("")

        print("Discovered personality:")
        print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
        print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
        print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))

        print("")
        print("----------")
        print("")
        print("Actions:")
        print("[F]eed: Feed your cat, both to keep it's mood up and not kill it.")
        print("[P]erform Activity: Perform an activity with your cat.")
        print("[H]elp/Guide: Read the help or guide on the game.")

        print("")

        action = input("What would you like to do? ").lower()
        print("")

        if action == "feed" or action == "f":
            phrases = ["Yum! That sure was delicous!", "Mhmmmm...", "That was puuuurrrrrfect!", "That was meownificient!"]
            print("Cat: Meow meow... meow.")
            print("Cat (Translated): {}".format(r.choice(phrases)))
            times.append(datetime.utcnow())

            print("\n(Press enter to continue)", end = "")
            input()

        elif action == "perform" or action == "activity" or action == "p" or action == "a":
            activities = ["Pet", "Groom", "Walk", "Go to the Park", "Dress Up", "Brush", "Listen to Music", "Take a Catnap", "Bird Watch", "Travel", "Zen Out", "Go Camping", "High-Five", "Watch TV", "Go to Work", "Chill Out"]

            print("Ok, these are the activities you can go on!")
            print("[1] Pet: Pet the cat.")
            print("[2] Groom: Groom the cat.")
            print("[3] Walk: Walk the cat.")
            print("[4] Go to the Park: Go to the park with your park.")
            print("[5] Dress Up: Dress up the cat.")
            print("[6] Brush: Brush the cat.")
            print("[7] Listen to Music: Listen to music with your cat.")
            print("[8] Take a Catnap: Take a nap with your cat.")
            print("[9] Bird Watch: Go birdwatching?")
            print("[10] Travel: Travel with the cat.")
            print("[11] Zen: Pet the cat.")
            print("[12] Go Camping: Go camping with the cat.")
            print("[13] High-Five: High-Five the cat.")
            print("[14] Watch TV: Watch TV with the cat.")
            print("[15] Go to Work: Go to Work with the cat.")
            print("[16] Chill Out: Chill out with the cat.")

            print("")
            print("You know that these are the things your cat likes:")
            print("Likes: {}".format( ", ".join( list( map( lambda x: "to " + x, known_likes ) ) ) ))
            print("Hates: {}".format( ", ".join( list( map( lambda x: "to " + x, known_hates ) ) ) ))
            print("Doesn't Mind: {}".format( ", ".join( list( map( lambda x: "to " + x, known_passive ) ) ) ))

            print("However, if you experiment, you get a FIRST TIME MOOD BONUS! YEEEEAAAAA!")

            print("")

            activity_number = int(input("What activity would you like to perform (type the number)? ").lower())

            clear()

            if activity_number == 1:
                # Pet
                curr = activities[activity_number - 1]

                print("You have chosen: Petting")
                print("(Press enter to continue) ", end = "")
                input()
                print("")

                luck = r.integer(0, 10)
                modifier = 0

                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 2

                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)

                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= r.integer(1, 2)

                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= 2

                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)

                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 3)

                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 2)

                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]

                    print(r.choice(phrases).format(cat.name))

                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]

                    print(r.choice(phrases).format(cat.name))

                print("(Press enter to continue) ", end = "")
                input()
                print("")


                luck = luck + modifier

                if luck <= 0:
                    print("In a freak petting accident, you manage to crush {}'s spine. It is not a nice look, and with a short breath and one final 'meow' before falling unconscious, you feel a sense of a not anger, but disapointment flood through you.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After an emergency trip to the vet, your cat hates your guts. Badly. It destests you.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 3
                    cat.mood -= 4

                    continue


                elif luck == 1:
                    print("Instead of petting, you manage to slip and firmly press down on the cat's body, causing its legs to collapase, forcing it the ground. You get the sense it will be alright, but it hurt more emotionally.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After a while, it begins to recover. It isn't that hurt, but it probably hates you now.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 2
                    cat.mood -= 3

                    continue



                elif luck in [2, 3]:
                    print("You pet a little too hard, and accidentally firmly slap it. {} quickly jumps away.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After some time has passed, you get the idea that things weren't what they once were.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 1
                    cat.mood -= 2

                    continue


                elif luck in [4, 5]:
                    print("The petting is OK, but a little hard at times. It doesn't mind it.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 0
                    cat.mood -= 0

                    continue


                elif luck in [6, 7]:
                    print("The petting was pretty good, and you both enjoyed the experince.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 0
                    cat.mood += 1

                    continue



                elif luck == 8:
                    print("That was some awesome petting. You especially rembered the part where you petted it very well. As well as being happier, the cat seems pyhsically and mentally healed.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 1
                    cat.mood += 2

                    continue


                elif luck == 9:
                    print("That was some PRO level petting. You shared an intimate moment together, and feel as if your previous relationship has now flowered into something wonderous and beautiful.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 2
                    cat.mood += 3

                    continue


                elif luck >= 10:
                    print("Before you even start petting, you know this is gonna be reaally, reaaallllyyy good petting. You feel energised, rivatalised, almost as if God himself has shone down a holy blessing of love into your fingertips.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("You notice a distinct shift in the way {} looks and moves, almost as if the petting it recieved flowed through it like happiness and life flows through you upon seeing a loved one. It's truly amazing.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health += 4
                    cat.mood += 5

                    continue


            elif activity_number == 2:
                # Grooming
                curr = activities[activity_number - 1]

                print("You have chosen: Grooming")
                print("(Press enter to continue) ", end = "")
                input()
                print("")

                luck = r.integer(0, 10)
                modifier = 0

                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 2

                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)

                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= r.integer(1, 2)

                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= 2

                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)

                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 3)

                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 2)

                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]

                    print(r.choice(phrases).format(cat.name))

                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]

                    print(r.choice(phrases).format(cat.name))

                print("(Press enter to continue) ", end = "")
                input()
                print("")


                luck = luck + modifier

                if luck <= 0:
                    print("As you press down the comb, you manage to trip, sending the pointed ends of the comb through the cat's skin. They reel back in pain as they let out a silent screech, before dropping to the floor, passed out.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After an emergency trip to the vet and a overnight rest, the sudden realisation hits you that you are now really hated by your cat. Loads. Not only that, but you've damaged its health.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 3
                    cat.mood -= 4

                    continue


                elif luck == 1:
                    print("You press the comb down so hard that you scrape off both fur and skin. It shrieks in terror.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("13 stiches later, the cat comes back from cat A&E and your relationship will probably never be the same.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 2
                    cat.mood -= 3

                    continue



                elif luck in [2, 3]:
                    print("You manage to groom in such a way that when you've finished the hair is completely on its end. {} hates you for it.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 1
                    cat.mood -= 2

                    continue


                elif luck in [4, 5]:
                    print("The grooming is OK, but a little hard at times. It doesn't mind it.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 0
                    cat.mood -= 0

                    continue


                elif luck in [6, 7]:
                    print("Your grooming skills were pretty good, and you both enjoyed the moment you shared together.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 0
                    cat.mood += 1

                    continue


                elif luck in [8, 9]:
                    print("Your grooming is 'on fleek' as the cool kids would say. The cat and also you, really enjoy the experince. It's amazing.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 2
                    cat.mood += 3

                    continue


                elif luck >= 10:
                    print("Before grooming, you must of accidentally whispered a quick prayer, because the amount of love and care you put into this grooming is outstanding. Its fur is so beatifully clean, you sure it would be suitable for a God.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("The energy between you and your cat has changed significantly, for the better.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health += 4
                    cat.mood += 5

                    continue


            elif activity_number == 3:
                # Walking
                curr = activities[activity_number - 1]

                print("You have chosen: Walking")
                print("(Press enter to continue) ", end = "")
                input()
                print("")

                luck = r.integer(0, 10)
                modifier = 0

                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 2

                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)

                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= r.integer(1, 2)

                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= 2

                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)

                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 3)

                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 2)

                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]

                    print(r.choice(phrases).format(cat.name))

                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]

                    print(r.choice(phrases).format(cat.name))

                print("(Press enter to continue) ", end = "")
                input()
                print("")


                luck = luck + modifier

                if luck <= 0:
                    print("As you take the first brave steps onto the road outside your residence, the cat is suddenly hit by a car- no, truck, creating a splatter on the road that you could probably frame and make modern art. Although there is blood, there is still a cat. Its eyes are beading with so much anger, you feel your stomach drop.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After you've visited the ER and had a small therapy session, you go back home. You sense a shift in mood between the two of you. I'd watch my back, if I were you.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 3
                    cat.mood -= 4

                    continue


                elif luck == 1:
                    print("The cat is hit by a car. As soon as you take a step outside, your cat is hit with a car. What's more, the car drives straight past, almost symbolising you and your cat's fleeting relationship.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After heavy surgery, the cat now hates you with a burning hatred that almost sears through your very soul.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 2
                    cat.mood -= 3

                    continue



                elif luck in [2, 3]:
                    print("You manage to tug the lead, causing the cat to scrape along the gravel road beside your house. {} is scratched, and they hate you.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 1
                    cat.mood -= 2

                    continue


                elif luck in [4, 5]:
                    print("It's a pretty bad walk. Although there is no injuries, it rains.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 0
                    cat.mood -= 0

                    continue


                elif luck in [6, 7]:
                    print("It was a severly OK walk. It wasn't sunny, but there was a slight hint of sun.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 0
                    cat.mood += 1

                    continue


                elif luck in [8, 9]:
                    print("Wow. This walk. It was just... amazing. You stroll down a path you haven't been down before, and it leads you to a beautiful park. By the time you get home, you feel a positive energy almost bond you and your cat.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 2
                    cat.mood += 3

                    continue


                elif luck >= 10:
                    print("I have no words. Who knew a walk could be so spiritual? Every step you took was like the moment you finally lie down on a Friday. Not only did the walk manage to somehow fix the cat's slight limp from previous circumstances, it rivatilised the bond you two had.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("The energy between you and your cat has changed significantly, for the better.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health += 4
                    cat.mood += 5

                    continue


            elif activity_number == 4:
                # Going to Park
                curr = activities[activity_number - 1]

                print("You have chosen: Going to Park")
                print("(Press enter to continue) ", end = "")
                input()
                print("")

                luck = r.integer(0, 10)
                modifier = 0

                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 2

                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)

                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= r.integer(1, 2)

                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= 2

                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)

                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 3)

                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 2)

                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]

                    print(r.choice(phrases).format(cat.name))

                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]

                    print(r.choice(phrases).format(cat.name))

                print("(Press enter to continue) ", end = "")
                input()
                print("")


                luck = luck + modifier

                if luck <= 0:
                    print("Phew. That incoming frisbee nearly hit your cat's head. You watch it glide off into the distance and hit a tree. Everything seems fine.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("But everything isn't fine. The frisbee richochets off the tree, and off into the face of a man who is for some reason shaving his beard with an old fashioned razor in the middle of the park. Instead of hitting him, it clips his razor, which embedds into the frisbee, forming a sharp edge. Luckily however, it darts off into nearby McDonalds, smashing through a window, not hitting your cat.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("Oh wait, no! The frisbee somehow magically rebounds and heads toward a woman to your left, lighting a cigarette. The only thing is that the frisbee is now covered in oil, and the flame from the lighter sends the frisbee into a flame.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("However, instead of hitting your cat, it embeds itself into a nearby tree.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("Oh. The tree topples over, crushing your cats puny body and spirit.")

                    cat.health -= 3
                    cat.mood -= 4

                    continue


                elif luck == 1:
                    print("For some reason, you think it's a good idea to let your kitty go down the slide. Spoiler: This does not end well.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("The cat slides down the slide so well, it flies up into the air, like some rubbish rip off of E.T., which then leads the cat to impaled on a nearby branch.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 2
                    cat.mood -= 3

                    continue



                elif luck in [2, 3]:
                    print("You look away whilst the cat attempts to climb a climbing frame. Unluckily, the cat falls to the ground. Unfortunately, this cat does not land on its feet, and instead lies facing up toward you with a large scowl on its face.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 1
                    cat.mood -= 2

                    continue


                elif luck in [4, 5]:
                    print("It's a 'meh' session at the park. You both get the idea that neither of you wanted to be doing other things.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 0
                    cat.mood -= 0

                    continue


                elif luck in [6, 7]:
                    print("Huh. It's pretty good actually. Cats don't normally like going to the park, but this one did.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 0
                    cat.mood += 1

                    continue


                elif luck in [8, 9]:
                    print("Jesus Christ. I had no idea you could have that much fun doing something as simple as... playing in the park. It invokes childhood memories of when you did the same thing, and way back when your parents still had faith in you.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 2
                    cat.mood += 3

                    continue


                elif luck >= 10:
                    print("It might of have been the dodgy catfood you bought from the man on the street, but {} seems especially happy during this Park session. You and {} imagine sailing a ship through a disturbed ocean, finding a secreted treasure inside a forgotten cage, fighting off armadas of spaceships.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("Your friendship has flowered into something beautiful.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health += 4
                    cat.mood += 5

                    continue


            elif activity_number == 5:
                # Dressing Up
                curr = activities[activity_number - 1]

                print("You have chosen: Dressing Up")
                print("(Press enter to continue) ", end = "")
                input()
                print("")

                luck = r.integer(0, 10)
                modifier = 0

                if (not curr in known_hates) and (not curr in known_hates) and (not curr in known_hates):
                    # FIRST TIME BONUS WOO
                    modifier += 2

                if curr in cat.hates and (not curr in known_hates):
                    # Is hated, but doesn't know it.
                    known_hates.append(curr)

                    phrases = ["Straight away, you realise {} hates this.", "All of a sudden, you realise this was a rubbish idea.", "As soon as you start, you notice a sudden shift in {} liking toward you. In a bad way. A vey bad way.", "Huh. {} hates this.", "You get a sudden scowl from {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= r.integer(1, 2)

                elif curr in cat.hates and curr in known_hates:
                    # Is hated, and totally knows it.
                    phrases = ["You already knew {} hated this. You horrible human being.", "You horrible, horrible human being.", "Forcing you cat to do something it doesn't like? You horrible person."]

                    print(r.choice(phrases).format(cat.name))

                    modifier -= 2

                elif curr in cat.likes and (not curr in known_likes):
                    # Is liked, but doesn't know it.
                    known_likes.append(curr)

                    phrases = ["This seems to bring {} joy like no other activity you've seen before.", "This is like heaven for {}. They really like you now."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 3)

                elif curr in cat.likes and curr in known_likes:
                    # Is liked, and knows it.
                    phrases = ["Like always. this is so much fun for {}.", "Once again, {} loves this.", "This brings the same feeling of joy both to you and {}."]

                    print(r.choice(phrases).format(cat.name))

                    modifier += r.integer(1, 2)

                elif curr in cat.passive and (not curr in known_passive):
                    # Is passive, but doesn't know it.
                    phrases = ["This seems very... normal for {}.", "{} doesn't mind this.", "{} shows no emotion whatsoever."]

                    print(r.choice(phrases).format(cat.name))

                elif curr in cat.passive and curr in known_passive:
                    # Is passive, and knows it.
                    phrases = ["Being mundane today are we?", "Like normal, this is normal.", "Once again, {} doesn't mind this.", "Like always, {} shows no emotion.", "As always, this is very normal for {}."]

                    print(r.choice(phrases).format(cat.name))

                print("(Press enter to continue) ", end = "")
                input()
                print("")


                luck = luck + modifier

                if luck <= 0:
                    print("As you take the first brave steps onto the road outside your residence, the cat is suddenly hit by a car- no, truck, creating a splatter on the road that you could probably frame and make modern art. Although there is blood, there is still a cat. Its eyes are beading with so much anger, you feel your stomach drop.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After you've visited the ER and had a small therapy session, you go back home. You sense a shift in mood between the two of you. I'd watch my back, if I were you.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 3
                    cat.mood -= 4

                    continue


                elif luck == 1:
                    print("The cat is hit by a car. As soon as you take a step outside, your cat is hit with a car. What's more, the car drives straight past, almost symbolising you and your cat's fleeting relationship.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("After heavy surgery, the cat now hates you with a burning hatred that almost sears through your very soul.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 2
                    cat.mood -= 3

                    continue



                elif luck in [2, 3]:
                    print("You manage to tug the lead, causing the cat to scrape along the gravel road beside your house. {} is scratched, and they hate you.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 1
                    cat.mood -= 2

                    continue


                elif luck in [4, 5]:
                    print("It's a pretty bad walk. Although there is no injuries, it rains.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health -= 0
                    cat.mood -= 0

                    continue


                elif luck in [6, 7]:
                    print("It was a severly OK walk. It wasn't sunny, but there was a slight hint of sun.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 0
                    cat.mood += 1

                    continue


                elif luck in [8, 9]:
                    print("Wow. This walk. It was just... amazing. You stroll down a path you haven't been down before, and it leads you to a beautiful park. By the time you get home, you feel a positive energy almost bond you and your cat.")
                    print("(Press enter to continue) ", end = "")
                    input()


                    cat.health += 2
                    cat.mood += 3

                    continue


                elif luck >= 10:
                    print("I have no words. Who knew a walk could be so spiritual? Every step you took was like the moment you finally lie down on a Friday. Not only did the walk manage to somehow fix the cat's slight limp from previous circumstances, it rivatilised the bond you two had.")
                    print("(Press enter to continue) ", end = "")
                    input()

                    print("")

                    print("The energy between you and your cat has changed significantly, for the better.".format(cat.name))
                    print("(Press enter to continue) ", end = "")
                    input()

                    cat.health += 4
                    cat.mood += 5

                    continue


            elif activity_number == 6:
                # Brush
                print("You have chosen: Brushing")


            elif activity_number == 7:
                # Listen to Music
                print("You have chosen: Listening to Music")


            elif activity_number == 8:
                # Take a Catnap
                print("You have chosen: Taking a Catnap")


            elif activity_number == 9:
                # Bird Watch
                print("You have chosen: Bird Watch")


            elif activity_number == 10:
                # Travel
                print("You have chosen: Travelling")


            elif activity_number == 11:
                # Zen
                print("You have chosen: Zenning")


            elif activity_number == 12:
                # Go Camping
                print("You have chosen: Camping")


            elif activity_number == 13:
                # High-Five
                print("You have chosen: High-Fiving")


            elif activity_number == 14:
                # Watch TV
                print("You have chosen: Watching TV")


            elif activity_number == 15:
                # Go to Work
                print("You have chosen: Going to Work")


            elif activity_number == 16:
                # Chill Out
                print("You have chosen: Chilling Out")






        elif action == "help" or action == "guide" or action == "h" or action == "g":
            pass # for now


    phrases = ["You have killed your cat. It is dead. If it were alive now, I bet it would have choice words for you, young man. You should feel bad.", "...I'm not sure how to break it to you... but you've killed your cat.", "Your cat is now deader that the relationship you had with it."]

    print(r.choice(phrases))
    print("(Press enter to end) ", end = "")
    input()


if __name__ == "__main__":
    #intro()
    main()
