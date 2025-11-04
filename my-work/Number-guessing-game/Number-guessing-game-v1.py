import random

def tellScore():    # Function for printing score and High_Score
    print(f"***your Score is {score}***")
    print(f"***High Score: {high_score}***\n")

def hint():     # Function for Giving hints for numbers
    if(guess_input>random_number):
        if (guess_input>(random_number+10)):
            print("Your guess is too high")
        elif (guess_input>(random_number+5)):
            print("Your guess is high")
        else:
            print("Your guess is a bit high")
        print()
    elif (guess_input<random_number):
        if (guess_input<(random_number-10)):
            print("Your guess is too low")
        elif (guess_input<(random_number-5)):
            print("Your guess is low")
        else:
            print("Your guess is a bit low")
        print()

def comments():     #function for passing random commets while playing game
    #Easy Comments
    if difficulty == 1:
        if score >= 500:
            mid_comments_500 = [
                "Godly? On *this* difficulty? You flatter yourself.",
                "Ah, the apex of unimpressive achievements. Truly divine.",
                "You're a god among ants, perhaps. Don't expect a parade.",
                "Did you actually break a sweat achieving that on the *easiest* setting?",
                "The only thing godly about that score is how little it means.",
                "If that's godly, then the actual gods must be terribly bored."
            ]
            print(random.choice(mid_comments_500))
        elif score >= 450: 
            mid_comments_450 = [
                "Almost perfect on the absolute easiest setting? Did you get a medal for tying your shoes too?",
                "You thought this was an achievement? Cute. Very cute.",
                "That score just proves anyone can get lucky, even you.",
                "You're trying to impress me with *that*? I'm not even blinking.",
                "A 450 on 'easy' is like bragging about winning a race against a turtle.",
                "Did you need a participation trophy for this, too?"
            ]
            print(random.choice(mid_comments_450))
        elif score >= 400: 
            mid_comments_400 = [
                "Congratulations, you've achieved 'slightly less pathetic' status.",
                "That's a score that says, 'I tried, but not really.'",
                "400 points? Did you accidentally lean on the keyboard for half the game?",
                "You're consistently average, even when the game holds your hand.",
                "I'm sure your mom will be very proud of your 'hard work'.",
                "That's about as inspiring as watching paint dry, slowly."
            ]
            print(random.choice(mid_comments_400))
        elif score >= 350: 
            mid_comments_350 = [
                "A score so forgettable, it barely even registered.",
                "Did you spend half the game admiring the pretty colors?",
                "That's not a score, it's a mild suggestion of effort.",
                "You're the reason they invented 'easy mode'.",
                "Proof that a pulse doesn't necessarily mean talent.",
                "You're making a strong case for 'beginner' difficulty having a negative score option."
            ]
            print(random.choice(mid_comments_350))
        elif score >= 300:
            mid_comments_300 = [
                "Possible? Yes, for someone with functional brain cells. Clearly not you.",
                "You're questioning if *this* is possible? My dear, you set the bar low.",
                "That's a score you get when you accidentally bump the keyboard.",
                "The only impossible thing is how little talent you displayed to get it.",
                "Is it possible to be this mediocre and still get a non-zero score? Apparently.",
                "Don't confuse 'possible' with 'impressive.' They're miles apart for you."
            ]
            print(random.choice(mid_comments_300))
        elif score >= 250:
            mid_comments_250 = [
                "Highest score ever? In the 'pathetic attempts' category, maybe.",
                "You're certainly setting a record... for being spectacularly average.",
                "The only thing 'ever' about that score is how forgettable it is.",
                "Did you pat yourself on the back for that? How quaint.",
                "That's about as 'highest ever' as a pebble is a mountain.",
                "Yes, the highest score ever achieved by someone still learning to tie their shoes."
            ]
            print(random.choice(mid_comments_250))
        elif score >= 200:
            mid_comments_200 = [
                "Marvelous? You must have a very low bar for 'marvelous'.",
                "That's 'marvelous' if you're measuring by the effort a sloth expends.",
                "The only thing marvelous is your ability to underperform consistently.",
                "You're getting excited over *that*? How utterly depressing.",
                "I've seen more 'marvelous' things in a dusty corner.",
                "A truly 'marvelous' display of... existing."
            ]
            print(random.choice(mid_comments_200))
        elif score >= 150:
            mid_comments_150 = [
                "Great score! If 'great' means 'barely worth mentioning.'",
                "That's a 'great' score for someone who just woke up from a coma.",
                "The only thing great about that is my patience watching you play.",
                "Did you misread 'mediocre' as 'great'?",
                "You should frame that score. As a warning to others.",
                "A score so 'great' it's almost an insult."
            ]
            print(random.choice(mid_comments_150))
        elif score >= 100:
            mid_comments_100 = [
                "Good score! For a houseplant.",
                "That's 'good' in the same way a flat tire is 'good' for a car.",
                "Are you going for 'bare minimum effort' and succeeding?",
                "If that's 'good,' I weep for the future of gaming.",
                "You can certainly call that 'good' if you enjoy lying to yourself.",
                "A score that practically screams 'I tried and failed, but still got points!'"
            ]
            print(random.choice(mid_comments_100))
        elif score >= 50:
            mid_comments_50 = [
                "Nice score! For someone who played with their eyes closed.",
                "That's about as 'nice' as a stubbed toe.",
                "I've seen toddlers do better, and they chew on the controller.",
                "Did you find those points on the ground?",
                "A 'nice' little reminder of your utter lack of skill.",
                "That score is 'nice' if 'nice' means 'almost zero.'"
            ]
            print(random.choice(mid_comments_50))
        elif score >= 0:
            mid_comments_0 = [
                "How did you even manage a zero on *easy* mode? That's impressive, in a sad way.",
                "Did you confuse the 'play' button with the 'self-destruct' button?",
                "You're a pioneer in failing at the simplest tasks.",
                "I'm genuinely curious: what was your strategy for achieving absolute nothingness?",
                "Even the game is probably embarrassed for you right now.",
                "Just... uninstall. Please."
            ]
            print(random.choice(mid_comments_0))
        print()
    #Mid dfficulty Comments
    elif difficulty == 2:
        if score >= 500:
            print("You Win!!!! I never thought this day would come :) Congratulations")
        elif score >= 450: 
            mid_comments_450 = [
                "Almost perfect on *easy* mode? My, how the mighty have fallen.",
                "You got *that* score here? What a waste of potential... or lack thereof.",
                "Did you get confused and think this was the 'hard' setting? Bless your heart.",
                "You're trying so hard to impress, and failing so spectacularly at it.",
                "Even on this setting, you're just scraping by, aren't you?",
                "A score that says, 'I exist, barely.'"
            ]
            print(random.choice(mid_comments_450))
        elif score >= 400:
            mid_comments_400 = [
                "Ah, 400. The score of 'almost competent,' but not quite.",
                "You're really showing your true colors, and they're not very vibrant.",
                "For this difficulty, that's less 'good' and more 'sad.'",
                "You're consistently average, which, for you, is a high bar.",
                "I'm not disappointed, just bored by your predictable mediocrity.",
                "Is that the sound of you reaching your absolute limit?"
            ]
            print(random.choice(mid_comments_400))
        elif score >= 350:
            mid_comments_350 = [
                "You managed to hit a score that's equally uninspiring in any mode.",
                "The very definition of 'just filling space.'",
                "Did you accidentally play with one hand tied behind your back? Or just usually this bad?",
                "At least you're consistently... below impressive.",
                "A true testament to how little effort you can put in and still get a non-zero score.",
                "That's a score a placeholder character would be ashamed of."
            ]
            print(random.choice(mid_comments_350))
        elif score >= 300:
            mid_comments_300 = [
                "You're not 'close to winning,' you're just less of a failure than before.",
                "Ah, the sweet taste of almost-but-not-quite. Savor it.",
                "You're closer to being good, like a snail is closer to the finish line of a marathon.",
                "Don't get your hopes up; 'almost' only counts in horseshoes and hand grenades. Not here.",
                "If that's 'close,' then I'm a supermodel.",
                "You're not even in the same zip code as 'winning.'"
            ]
            print(random.choice(mid_comments_300))
        elif score >= 250:
            mid_comments_250 = [
                "Yes, 'greater heights' of mediocrity, perhaps.",
                "You're moving, alright. Straight into the 'barely acceptable' category.",
                "Impressive, for someone with such limited potential.",
                "You're on your way... to proving my low expectations right.",
                "Keep 'moving,' maybe eventually you'll stumble upon competence.",
                "A true journey to the peak of unimpressive performance."
            ]
            print(random.choice(mid_comments_250))
        elif score >= 200:
            mid_comments_200 = [
                "Good job for not completely self-combusting, I guess.",
                "If 'good job' means 'barely scraped by,' then sure.",
                "Is that your best? Because it's not saying much.",
                "Keep it up, and you might just reach the level of 'forgettable.'",
                "That's cute. Now, try actually being good.",
                "You've proven you can press buttons. What else ya got?"
            ]
            print(random.choice(mid_comments_200))
        elif score >= 150:
            mid_comments_150 = [
                "Nice score... if 'nice' means 'woefully inadequate.'",
                "Oh, look, a score that screams 'I tried my best and failed.'",
                "That's adorable. Did you get a sticker for that?",
                "You really are a master of understatement, aren't you? That's not 'nice.'",
                "A score so 'nice' it's practically an insult.",
                "Congrats on reaching the 'participation award' tier."
            ]
            print(random.choice(mid_comments_150))
        elif score >= 100:
            mid_comments_100 = [
                "Try harder? You couldn't try harder if your life depended on it.",
                "Your 'harder' is everyone else's 'barely breathing.'",
                "Don't bother trying harder, some things are just beyond you.",
                "You can try, but talent isn't something you can just 'try' to have.",
                "Save your effort, it's clearly not making a difference.",
                "I'd tell you to try harder, but I don't want to encourage false hope."
            ]
            print(random.choice(mid_comments_100))
        elif score >= 50:
            mid_comments_50 = [
                "Ok-ish? That's like saying a dumpster fire is 'ok-ish' warmth.",
                "That score is about as 'ok-ish' as a toothache.",
                "Are you intentionally trying to get the lowest possible score without hitting zero?",
                "The only thing 'ok-ish' about that is my tolerance for your incompetence.",
                "If that's 'ok,' then my standards are in the Mariana Trench.",
                "Please, for the love of pixels, just stop."
            ]
            print(random.choice(mid_comments_50))
        elif score >= 0:
            mid_comments_0 = [
                "Zero? In *this* difficulty? Are you even trying, or just breathing?",
                "Congratulations, you've achieved absolute nothingness. Again.",
                "Did the game even load for you, or did your brain just crash?",
                "I'd suggest you try the tutorial, but I doubt it would help.",
                "You're a walking, talking argument against giving everyone a chance.",
                "My pet hamster could get a higher score blindfolded."
            ]
            print(random.choice(mid_comments_0))
        print()
    #Hard Mean Comments
    elif difficulty == 3:
        if score >= 500:
            print("You Win, whatever... What did you expect")
        elif score >= 450:
            
            mean_comments_450 = [
                "Did you cheat, or just get lucky? Either way, still unimpressive.",
                "A perfect score on *this*? Truly a momentous occasion for mediocrity.",
                "Wow, you really peaked with this one. Don't expect it to happen again.",
                "And the crowd goes mild! Barely a ripple of excitement.",
                "Your high score is inversely proportional to my interest.",
                "A chimpanzee could do that. Probably faster."
            ]
            print(random.choice(mean_comments_450))


        elif score >= 400:
            mean_comments_400 = [
                "Oh, look, a faint glimmer of competence. Don't strain yourself.",
                "Almost decent. Almost.",
                "You're making progress... towards being less of a disappointment.",
                "Did you consult a Ouija board for that guess? Because it certainly wasn't skill.",
                "Just barely above 'total failure.' Bravo.",
                "Still not good enough to earn my respect. Or anyone's."
            ]
            print(random.choice(mean_comments_400))


        elif score >= 350:
            mean_comments_350 = [
                "Congratulations, you've achieved peak blandness. Enjoy your beige existence.",
                "You're the vanilla ice cream of players. No sprinkles for you.",
                "So average, it's almost impressive how unremarkable you are.",
                "Your skill level is a flat line on the excitement graph.",
                "The definition of 'just existing.'",
                "If 'meh' was a score, you'd be a master."
            ]
            print(random.choice(mean_comments_350))


        elif score >= 300:
            mean_comments_300 = [
                "Is that the sound of your brain struggling, or just background static?",
                "My pet rock could give you a run for your money.",
                "You're playing with the intellectual prowess of a damp sponge.",
                "Did you forget to turn on your brain this morning? Or ever?",
                "The lights are on, but nobody's home. Or at least, not anyone smart.",
                "That score just screams 'entry-level thinking.'"
            ]
            print(random.choice(mean_comments_300))


        elif score >= 250:
            mean_comments_250 = [
                "Woof woof! That's about your intellectual capacity right now.",
                "Even a squirrel could probably figure this out faster.",
                "Good dog! Now go fetch a clue.",
                "You're so close to being a houseplant.",
                "Is that a tail wagging, or just your last few brain cells firing?",
                "Perhaps stick to chasing cars, this game is clearly too complex."
            ]
            print(random.choice(mean_comments_250))


        elif score >= 200:
            mean_comments_200 = [
                "Oh, you thought that was a compliment? How adorable. And wrong.",
                "Don't get too excited, that's still a participation trophy score.",
                "The only thing impressive here is your ability to consistently disappoint.",
                "Just when I thought it couldn't get worse, you proved me wrong.",
                "Your efforts are truly... pitiful. Keep trying, I guess.",
                "I've seen slugs move with more purpose than your gameplay."
            ]
            print(random.choice(mean_comments_200))


        elif score >= 150:
            mean_comments_150 = [
                "You tried so hard, and got so far... into the gutter.",
                "Bless your heart. You really thought you had a chance, didn't you?",
                "Persistence doesn't always equal progress, especially for you.",
                "The only thing you're winning is the award for 'most effort, least return.'",
                "You're like a toddler trying to solve calculus. Cute, but futile.",
                "Just give up. It'll be less embarrassing for everyone."
            ]
            print(random.choice(mean_comments_150))


        elif score >= 100:
            mean_comments_100 = [
                "Seriously, just stop. You're making the game look bad.",
                "Did you even try? Or are you just here for the moral support? (You don't get any.)",
                "I've seen better scores from a coin flip. A weighted coin flip.",
                "Your score is a testament to your absolute lack of anything.",
                "Why waste your time? You clearly have no aptitude for this.",
                "This isn't a game, it's a charity case, and you're the recipient."
            ]
            print(random.choice(mean_comments_100))


        elif score >= 50:
            mean_comments_50 = [
                "That's not a score, that's a typo.",
                "Did you accidentally hit the 'lose' button repeatedly?",
                "A single-digit IQ would be an improvement for you right now.",
                "I've seen dust bunnies with more ambition than your score.",
                "Even a broken clock is right twice a day. You, however...",
                "Just uninstall. For the good of humanity."
            ]
            print(random.choice(mean_comments_50))


        elif score >= 0:
            mean_comments_0 = [
                "Congratulations, you've achieved absolute nothingness. A true master of failure.",
                "Did you even launch the game, or just stare blankly at the screen?",
                "You managed to get a score of zero. That actually takes a special kind of ineptitude.",
                "I'd say try again, but honestly, what's the point?",
                "Even 'easy mode' is probably beyond your grasp, you intellectual void.",
                "Is there a negative score option? Because you deserve it."
            ]
            print(random.choice(mean_comments_0))
    print()









high_score=0
print("Guess the Number")
print()
print(  "Info "\
        "\n"\
        "\n1.You get 3 chances to guess the correct number in each level."\
        "\n2.Every guess you make you get a hint whether the guessed number is low or high.\n" \
        "\n3.There are 3 difficulty levels: 1->Easy 2->Medium 3->Hard" \
        "\n\t Easy Mode- Each level the number range increases by 1 and you get 5 chances to guess"\
        "\n\t Medium Mode- Each level the number range increases by 3 and you get 4 chances to guess" \
        "\n\t Hard Mode- Each level the number range increases by 5 and you get 3 chances to guess")


# main code

while True:
    level = 1
    score=0

    userInput=input("Press \'Enter\' to start\nPress \'x\' to quit\n")
    if userInput=="":
        print("Welcome to the game")
        while True:
            try:
                difficulty = int(input("Enter Difficulty (1/2/3):  "))
                if difficulty not in [1,2,3]:
                    raise ValueError
                break
            except ValueError:
                print("Please Enter Valid Difficulty")

        while True:
            last_num=level*difficulty
            print(f"Level: {level}")
            random_number=random.randrange(0,last_num)
            for i in range(6-difficulty,0,-1):

                while True:
                    try:
                        guess_input=int(input("Enter your guess: "))
                        break
                    except ValueError:
                        print("Please Enter a Valid Guess (Only numbers)")

                if(guess_input==random_number):
                    score+=10
                    level+=1
                    print(f"You are correct the number is {random_number}")
                    tellScore()
                    comments()
                    break
                else:
                    hint()
                    print(f"{i-1} chances left to guess!!!")

            if guess_input != random_number:
                print("You ran out of chances }:-(")
                print("YOU LOSE!")
                print(f"The number was {random_number}")
                
                if score > high_score:
                    high_score = score

                tellScore()
                break
                    
            
    #Quit
    elif userInput.lower()=="x":
        print("GAME OVER!!!!")
        break
    else:
        print("Please enter valid input")