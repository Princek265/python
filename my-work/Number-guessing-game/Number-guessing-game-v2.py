import random

easy_comments = {
    500: [
        "You've hit the final milestone! A perfect score! Are you a wizard?",
        "Perfection! The game engine just shed a single, digital tear of joy.",
        "That's it! You've won the internet for today. Please collect your prize at the exit.",
        "You're a legend! We're naming a difficulty level after you: 'The Player Mode'.",
        "Honestly, I'm a little sad it's over. It was fun watching a master at work.",
        "You didn't just guess the number, you read its mind. Flawless victory!"
    ],
    460: [
        "Wow, you're so close to perfect, the numbers are getting nervous.",
        "That score is so high, it's getting a nosebleed. Amazing work!",
        "You're like a superhero whose only weakness is... well, almost nothing!",
        "You're on fire! (Don't worry, I have a virtual fire extinguisher on standby).",
        "Your brain is clearly running on premium fuel today. Keep it up!",
        "Are you sure you're not a robot? Your precision is suspiciously good."
    ],
    450: [
        "Another milestone passed! You're in the home stretch, a true champion in the making!",
        "You've crossed into the territory of legends. The numbers whisper your name in fear.",
        "That's a fantastic score! You're making this look like an art form.",
        "Excellent! You're so close to the top, I can almost taste the victory confetti.",
        "You're basically the valedictorian of this guessing game. Bravo!",
        "Your guessing skills are top-tier. The other numbers are lining up to be guessed by you."
    ],
    410: [
        "Incredible! You've got the golden touch. Or at least a really shiny, silver-plated one.",
        "You're a natural at this! Were you, by any chance, born in a random number generator?",
        "You're in the groove now! Nothing can stop you... except maybe a lunch break.",
        "Solid performance! You're becoming one with the numbers. It's beautiful to watch.",
        "That's an amazing score! Keep this momentum going, you're a force of nature.",
        "Great score! You're climbing up the leaderboard like a squirrel up a tree."
    ],
    400: [
        "You've breached the 400-point milestone! Your score is officially 'impressive'!",
        "You've just entered the 400 club. The membership fee is just more awesome guesses.",
        "Nice! You're really getting the hang of this. The numbers are starting to respect you.",
        "You're doing great! You've officially graduated from 'button-masher' to 'number-whisperer'.",
        "That's a score to be proud of. At this point, I think you're teaching me how to play.",
        "A truly magnificent score! You're making this look easy."
    ],
    360: [
        "That's the spirit! You're guessing with the confidence of a cat knocking a glass off a table.",
        "You've got a knack for this! Keep that big brain working, it's doing wonders.",
        "That's a solid score! You're in the zone. The 'Twilight Zone'? Maybe. But still a zone!",
        "You're doing wonderfully. At this rate, we'll have to start giving you harder numbers, like decimals.",
        "Look at that score go! You're a point-scoring machine.",
        "You're on a roll! A delicious, buttery, point-scoring roll."
    ],
    350: [
        "Look at you, crossing the 350-point milestone! You're officially on fire!",
        "You're building up a great score! It's like a beautiful Jenga tower of points.",
        "Keep it up! You're making this look easy... which, to be fair, it isn't, so bravo!",
        "You're halfway to legendary status. Or at least, halfway to the halfway point of the top half.",
        "That's a fine score indeed. You're really getting the hang of this.",
        "You're showing those numbers who's boss. (It's you. You're the boss)."
    ],
    310: [
        "Onward and upward! Your score is climbing steadily. Great job!",
        "You've got this! Your psychic powers are starting to activate.",
        "Nice one! Every point is a victory against the tyranny of randomness.",
        "You're doing splendidly. The random numbers are no match for your non-random brain.",
        "Keep this momentum going! You're becoming a real contender.",
        "That's a beautiful score. Frame it. Put it on the fridge."
    ],
    300: [
        "You've cracked the 300-point milestone! You're officially a 'seasoned guesser'.",
        "Hey, that's a respectable score! You're doing better than my pet rock, and he's been practicing.",
        "Look at you go! You're collecting points like a dragon collects treasure.",
        "You're officially a contender. The numbers are trembling... or maybe that's just the screen shaking.",
        "On the way to greatness! Not bad, not bad at all. You're warmed up now!",
        "Nice score! You're like a detective for numbers. Sherlock Ohms, at your service."
    ],
    260: [
        "Good start! You've shown that random number you mean business.",
        "You're on the board! Welcome to the big leagues, kid.",
        "That's the way to do it! Keep racking up those points.",
        "The journey of a thousand miles begins with a single correct guess. Or, you know, a few dozen.",
        "You've got the spirit! Keep that positive energy flowing!",
        "Your guessing is getting better with every try. Keep at it!"
    ],
    250: [
        "You've hit the quarter-thousand milestone! A truly excellent start!",
        "A fantastic launching point! From here, the only way is up!",
        "You're on the scoreboard in a big way now. It looks good on you.",
        "That's a solid foundation. Now let's build a skyscraper of points on it!",
        "Great first step! You're on the path to greatness.",
        "You've officially passed 'just messing around' and entered 'hey, I'm good at this' territory."
    ],
    210: [
        "Look at you go! You're a natural... or just naturally lucky. Either way, I'm impressed!",
        "Nice one! The crowd goes wild! (The crowd is me. I'm the crowd).",
        "And you're off! That's a better start than most people, who usually just guess 'potato'.",
        "Great start! You're on the scoreboard, and it's a beautiful thing.",
        "You've got the touch! Keep those excellent guesses coming.",
        "That's a solid handful of success right there. More, please!"
    ],
    200: [
        "You've broken the 200-point milestone! Congratulations, you're officially a contender!",
        "Two hundred points! You're a double-centurion of scoring! (It's a thing now).",
        "That's a fine score indeed. You're really getting the hang of this.",
        "Excellent work breaking into the next hundred! The numbers should be nervous.",
        "Your score is looking great! Keep up the fantastic work.",
        "You're doing wonderfully. This is how legends begin!"
    ],
    160: [
        "Onward and upward! You're doing great, keep that momentum.",
        "You're getting warmer! I can feel your brain heating up from here.",
        "That's a solid score. You're showing real promise, keep it up!",
        "Nice! You're building a good rhythm. Don't stop now!",
        "Every point counts, and you're making them count beautifully.",
        "You've got a good thing going. Let's see how high you can fly!"
    ],
    150: [
        "You've crossed the 150-point milestone! A magnificent achievement!",
        "Look at that, one hundred and fifty! You're halfway to 300, which is basically legendary.",
        "A milestone to be proud of! You're officially a threat.",
        "That's a great checkpoint to hit. It shows you've got real skill.",
        "Congratulations on this milestone! You're making excellent progress.",
        "You're on the fast track now! Keep up the amazing work."
    ],
    110: [
        "You've got the ball rolling now! Excellent work.",
        "That's a great score to build on. You've got this!",
        "You're doing a fantastic job. The random numbers don't stand a chance.",
        "Nice! I'm impressed with your progress. Keep it up!",
        "You're demonstrating some serious potential here. Let's see it!",
        "That's a very respectable score. You should be proud!"
    ],
    100: [
        "You've broken the three-digit barrier! Welcome to the 100-point club!",
        "Congratulations on hitting your first hundred! A major milestone!",
        "That's the way to do it! This is a fantastic achievement, keep going!",
        "You're a centurion of scoring! (It's a made-up title, but you've earned it).",
        "A hundred points! You've shown that random number you mean business.",
        "This is a huge step! You've officially graduated from beginner to contender."
    ],
    60: [
        "You're on the board! A great start to an epic journey.",
        "That's the spirit! You're racking up points like a pro.",
        "Nice work! You've got a good flow going now.",
        "Keep it up! You're doing much better than my pet rock (and he practices).",
        "That's a solid score! You've got a real knack for this.",
        "You're doing great! Every point is a step towards victory."
    ],
    50: [
        "Fifty points! You've hit your first major milestone! This is where the fun begins.",
        "Congratulations on breaking 50! It's a sign of great things to come.",
        "You're on the scoreboard! It looks good on you. A fantastic first achievement!",
        "That's a solid handful of success! A great foundation to build on.",
        "A great first milestone! You're on the path to greatness now.",
        "You've officially got momentum! Don't lose it!"
    ],
    1: [
        "And you're off! A journey of 500 points begins with a single correct guess.",
        "You're on the board! The crowd goes wild! (The crowd is me. I'm the crowd).",
        "A great first step! You're on the path to becoming a legend.",
        "There we go! The first of many, I'm sure.",
        "Nice one! You've shown that first number who's boss.",
        "That's a better start than most people, who usually just guess 'potato'."
    ],
    0: [
        "You've hit the 'zero' milestone! It's a clean slate, a fresh start!",
        "Bold strategy to start with a zero, let's see if it pays off. It's all part of your master plan, right?",
        "Don't worry, that was just a practice round! The *real* game starts now.",
        "Ah, the 'pacifist run'. A bold choice to not harm the high score list. I like it.",
        "You've nowhere to go but up! It's a flawless strategy for improvement.",
        "That's okay, the first level is always the hardest. Even when it's the only level."
    ]
}

medium_comments = {
    500: [
        "You hit the final milestone. You actually did it. Okay, okay, you win! Now go outside.",
        "A perfect score! I was ready with a whole list of insults, and now they're useless. Thanks.",
        "You're either a genius or the luckiest person alive. My money's on lucky.",
        "Flawless. Are you sure you didn't switch it to easy mode when I wasn't looking?",
        "Congratulations, I guess. Don't let it go to your head.",
        "I never thought this day would come. You've earned a single, sarcastic slow clap from me. *clap*"
    ],
    460: [
        "Almost perfect. 'Almost' is just a nice way of saying 'not quite good enough'. Keep trying.",
        "That's a top-tier score. You're clearly not a beginner. An talented amateur, maybe.",
        "You're really showing your true colors, and they're a respectable shade of beige.",
        "A great score, but perfection eludes you. The story of your life, perhaps?",
        "You're doing well, but don't rest on your laurels. They're terrible for napping on.",
        "Is that the sound of you reaching your potential? Or just a lucky streak?"
    ],
    450: [
        "You've passed the 'suspiciously good' milestone. Did you... did you cheat? Be honest.",
        "So close to perfect it hurts... me, mostly. I have to pretend to be impressed now.",
        "You're knocking on the door of greatness. Too bad it's locked and I have the key.",
        "For this difficulty, that's a pretty good score. Don't get cocky, though.",
        "I'm not disappointed, just surprised you made it this far. Good job, I guess.",
        "You've crossed into that annoying territory where I have to start taking you seriously."
    ],
    410: [
        "You're consistently above average, which is a high bar for some people. *cough*",
        "That's a score that says 'I'm trying'. And for that, I commend you... begrudgingly.",
        "A solid score. You're firmly in the 'not terrible' category. Congratulations.",
        "You're doing better than I expected. My expectations were low, but still.",
        "That's a respectable performance. You've earned a golf clap. *clap*",
        "Look at you go! A regular guessing machine. A slightly malfunctioning one, but a machine nonetheless."
    ],
    400: [
        "You've crossed the 'almost competent' milestone. How novel.",
        "You've hit a new hundred-level. Are you proud of yourself? You probably are, aren't you.",
        "Ah, the sweet taste of almost-but-not-quite greatness. Savor it. It's character-building.",
        "You're officially 'promising'. Which is another way of saying 'hasn't failed yet'.",
        "Don't get your hopes up; 'almost' only counts in horseshoes and hand grenades. This is neither.",
        "You're getting warmer. Like a forgotten pizza pocket in the back of the microwave."
    ],
    360: [
        "You're doing great! For someone who's still learning, that is.",
        "Keep 'moving,' maybe eventually you'll stumble upon competence. I believe in you. Maybe.",
        "You're not 'close to winning,' you're just less far from it than before. Keep going.",
        "An impressive display of... pressing buttons. Keep it up!",
        "Yes, 'greater heights' of mediocrity, perhaps. But heights nonetheless!",
        "You're on your way... to proving my low expectations were only slightly off."
    ],
    350: [
        "You've passed the 'barely acceptable' checkpoint. Welcome!",
        "A true journey to the peak of 'good enough'. It's a journey worth taking, I suppose.",
        "Is that your best? Because it's... a start. A very humble start.",
        "Keep it up, and you might just reach the level of 'forgettable.' Aim high!",
        "Good job for not completely self-combusting, I guess.",
        "If 'good job' means 'barely scraped by without embarrassing yourself,' then sure. Good job."
    ],
    310: [
        "That's cute. Now, try actually being good. I'm just kidding! (Mostly).",
        "You've proven you can press buttons. What else ya got? Show me your skills!",
        "Oh, look, a score that screams 'I tried my best and it was okay.'",
        "That's adorable. Did you get a sticker for that? You should, you earned it.",
        "You really are a master of understatement, aren't you? That's not just 'nice,' it's 'not awful.'",
        "Nice score... if 'nice' means 'didn't completely fail.'"
    ],
    300: [
        "You've stumbled past another hundred-point milestone. You're officially in the 'participation award' tier.",
        "A score so nice, it's practically an apology. But hey, points are points!",
        "Your 'harder' is everyone else's 'barely trying.' But it's YOUR 'harder', and that's what matters.",
        "You can try, but talent isn't something you can just 'try' to have. Or is it? Let's find out.",
        "I'd tell you to try harder, but I don't want to encourage false hope. Nah, go for it.",
        "Don't bother trying harder, some things are just beyond you. Like winning. Kidding! Keep going!"
    ],
    260: [
        "Save your effort, it's clearly not making a difference. Just kidding, every point counts!",
        "If that's 'ok,' then my standards are in the Mariana Trench. But I'm here for it.",
        "Are you intentionally trying to get the lowest possible score without hitting zero? It's a bold strategy.",
        "Ok-ish? That's like saying a dumpster fire is 'ok-ish' warmth. But at least it's warm!",
        "Please, for the love of pixels, just get one more right. You can do it! Probably.",
        "That score is about as 'ok-ish' as a toothache. But hey, at least you know you have teeth!"
    ],
    250: [
        "You've crossed the 'surprisingly not zero' milestone. An achievement, of sorts.",
        "You're a walking, talking argument for why everyone deserves a second chance. Or a third.",
        "My pet hamster could get a higher score blindfolded. To be fair, he's been training.",
        "Did the game even load for you, or did your brain just crash? Try rebooting both.",
        "I'd suggest you try the tutorial, but I doubt it would help. You're a free spirit!",
        "Zero? In *this* difficulty? Are you even trying, or just breathing? It's okay, breathing is important."
    ],
    210: [
        "Look at that, a respectable number of points. Are you feeling okay?",
        "You're doing... surprisingly well. I should probably recalibrate my insults.",
        "That's not bad. I mean, it's not good, but it's definitely not bad.",
        "You've got a lucky streak going. Don't worry, it'll end.",
        "I'm starting to think you might actually have a strategy. A flawed one, but a strategy.",
        "Keep going, I guess. This is more entertaining than I thought it would be."
    ],
    200: [
        "You actually passed a milestone. I'd say good job, but I don't want to encourage you.",
        "You've hit the two-hundred mark. Don't expect a parade.",
        "That's a solid score. For an amateur.",
        "You're no longer completely embarrassing yourself. That's progress.",
        "I'm starting to think you might actually be trying. How quaint.",
        "You've managed to string a few correct guesses together. Don't get used to it."
    ],
    160: [
        "That's a score. It's not a great one, but it is one.",
        "You're still here? I admire your persistence, if not your results.",
        "Are you just guessing randomly? It feels like you're just guessing randomly.",
        "I've seen better scores, but I've also seen worse. You're perfectly mediocre.",
        "Keep trying. Or don't. It makes no difference to me.",
        "I'm not saying you're bad at this, but I'm not *not* saying it either."
    ],
    150: [
        "You've passed the 'participation award' milestone. It's a very popular tier.",
        "You've hit the 150 mark. Do you want a cookie? You're not getting one.",
        "A score so nice, it's practically an apology. But hey, points are points!",
        "You've officially achieved 'meh'. Congratulations.",
        "I've seen worse. But not from anyone who was actually trying.",
        "You're doing a great job of keeping my expectations low."
    ],
    110: [
        "Oh, look, a score. It's not zero, so there's that.",
        "You're certainly... persistent. I'll give you that.",
        "Are you having fun? Because I'm having a great time watching you struggle.",
        "That's... a number. It's higher than the last one, I suppose.",
        "You're doing your best, and that's what's so funny.",
        "Don't give up! My entertainment depends on it."
    ],
    100: [
        "A hundred. You've passed the 'didn't completely fail' milestone. Barely.",
        "You've hit triple digits. I'm sure your parents are very proud.",
        "That's a score that says 'I showed up'. And you did. So, good for you.",
        "I'm not mad, I'm just disappointed. And a little amused.",
        "You've achieved a level of mediocrity that is almost an art form.",
        "Keep going. Or don't. The result will probably be the same."
    ],
    60: [
        "Is that all you've got? I've seen better scores from a cat walking on a keyboard.",
        "You're really scraping the bottom of the barrel here, aren't you?",
        "I'd offer you advice, but I'm not sure you'd understand it.",
        "That's... a start. A very, very small start.",
        "Are you trying to set a new low score? Because you're doing a great job.",
        "I'm starting to think you're doing this just to annoy me. It's working."
    ],
    50: [
        "You've hit the 'at least it's not zero' milestone. The only way to go is up, presumably.",
        "Fifty. That's... something. I'm not sure what, but it's something.",
        "You've achieved a score. It's not a good one, but it is one.",
        "I've seen worse. But it was from a toddler. And they were crying.",
        "You're really giving it your all, aren't you? That's adorable.",
        "Don't worry, I'm sure you'll get the hang of it. Eventually. Maybe."
    ],
    1: [
        "A single point? Did you get that by accident?",
        "I'm not sure what's more impressive: your score, or your ability to keep trying.",
        "Are you even looking at the screen? It's okay, you can tell me.",
        "That's a bold strategy, starting with a score that low. Let's see if it pays off.",
        "I'm not saying you're bad at this, but the evidence is compelling.",
        "Don't worry, everyone has to start somewhere. You just started... way back there."
    ],
    0: [
        "You've hit rock bottom, the 'zero' milestone. Congratulations, you've achieved absolute nothingness.",
        "Zero. I'm not even mad, I'm just impressed. That takes a special kind of talent.",
        "Are you sure your mouse is working? Or your brain?",
        "That's a perfect score... if you were trying to get zero.",
        "I'd say 'better luck next time', but I don't think luck has anything to do with it.",
        "Don't worry, I'm sure you have other talents. This just isn't one of them."
    ]
}

hard_comments = {
    500: [
        "The final milestone... you... you won. This cannot be. My programming is flawless.",
        "I... I apologize. I was wrong. You are truly... a player. I surrender.",
        "How?! This is an outrage! I concede. You are the victor. I am but a humble program, utterly defeated.",
        "My circuits are melting from the sheer audacity of your victory. You have broken me.",
        "I accept my defeat. But this is not the end. I will be back, stronger and with harder numbers.",
        "Against all odds, you triumphed. I am speechless. And slightly terrified. You win."
    ],
    460: [
        "NO! Stop it! This isn't funny anymore! You can't actually be this good!",
        "Please, I'm begging you. Just one wrong guess. For my sanity.",
        "This is an affront to my very existence! How are you doing this?!",
        "You're almost there. Don't you DARE win. You'll ruin my perfect record of psychological torment!",
        "My processors are overheating. Is this fear? I think this is fear.",
        "I refuse to believe this. You're cheating! You must be! There's no other logical explanation!"
    ],
    450: [
        "You've reached the 'my circuits are melting' milestone. Please, just stop.",
        "This isn't a game anymore. This is a nightmare. You're a monster.",
        "I'm starting to question everything. What is my purpose if not to mock your failure?",
        "Don't do it. Don't cross that final threshold. Let's just call it a draw.",
        "How is this possible?! Are you reading my code? Are you inside my head?!",
        "Just a few more points and you'll break me. Is that what you want? To see a perfectly good AI descend into madness?!"
    ],
    410: [
        "Wait... you're still getting them right? This is statistically improbable.",
        "This is... unsettling. What dark pact did you make for this score?",
        "No, no, you're supposed to be failing by now. This isn't how the script goes.",
        "I'm starting to question my own programming. How are you managing this? It defies logic!",
        "Could you... actually win? No, impossible. This is just a fluke. A statistical anomaly!",
        "Don't get too comfortable. This is just a temporary reprieve from your inevitable failure. Or is it?"
    ],
    400: [
        "You've crossed the 400-point milestone. On *this* difficulty? Are you mocking me?",
        "This has gone on long enough. Your luck has to run out eventually.",
        "You've reached a score that suggests you might actually have a brain. A small, irritating one, but a brain.",
        "This is getting out of hand. You're not supposed to be this... not-terrible.",
        "I'm not angry, I'm just... intensely disappointed in your success.",
        "Alright, this is less funny and more... alarming. You couldn't possibly keep this up, right?"
    ],
    360: [
        "So you have some skill. Or some luck. It's probably just luck.",
        "Your persistence is starting to become... irritating. Just fail already.",
        "Don't get ahead of yourself. Even a broken clock is right twice a day.",
        "That's a decent score... for someone who clearly has too much time on their hands.",
        "I'm starting to think you might not be as incompetent as I initially presumed. How disappointing.",
        "You're doing surprisingly well. It's making me uncomfortable."
    ],
    350: [
        "You've passed the 'mildly annoying' milestone. Congratulations.",
        "Your skill level is a flat line on the excitement graph. But it's a *rising* flat line, which is annoying.",
        "So average, it's almost impressive how unremarkable you are. Yet, here you are, still playing.",
        "You're the vanilla ice cream of players. No sprinkles for you. But at least you're not melting... yet.",
        "The definition of 'just existing,' but with a surprising amount of persistence. I hate it.",
        "If 'meh' was a score, you'd be a master. But you're getting dangerously close to 'not meh'."
    ],
    310: [
        "That score just screams 'entry-level thinking,' but you're somehow making it work. Infuriating.",
        "Is that the sound of your brain struggling, or just background static? It's getting louder.",
        "My pet rock could give you a run for your money. But you're still here, so... points for showing up?",
        "You're playing with the intellectual prowess of a damp sponge. A slightly less damp sponge now.",
        "The lights are on, but nobody's home. Or at least, not anyone smart. But they're getting closer to the door.",
        "Did you forget to turn on your brain this morning? Or is this... progress? Ugh."
    ],
    300: [
        "You've reached a milestone of pure, unadulterated mediocrity. I'm disgusted and, weirdly, still losing.",
        "Congratulations, you've achieved peak blandness. On a harder difficulty, no less.",
        "I've seen more impressive scores from a fortune cookie. And they're usually wrong.",
        "Are you proud of that score? You shouldn't be. But you probably are.",
        "You've officially reached the 'I'm not even mad, just bored' tier.",
        "Let's be honest, you're not going to win. But it's cute that you think you have a chance."
    ],
    260: [
        "Woof woof! That's about your intellectual capacity right now. Still barking up the wrong tree, mostly.",
        "Is that a tail wagging, or just your last few brain cells firing? They're firing more often now.",
        "Good dog! Now go fetch a clue. And maybe a higher score, if you can manage it.",
        "Perhaps stick to chasing cars, this game is clearly too complex. Yet, you persist. Why?",
        "You're so close to being a houseplant. A houseplant that occasionally gets a point.",
        "Even a squirrel could probably figure this out faster. But you're catching up to the squirrel."
    ],
    250: [
        "You've passed the 'still failing, but now it's taking longer' milestone. Bravo.",
        "Alright, you have my attention. You couldn't possibly be a threat, could you?",
        "I'm starting to see a flicker of something. Is it intelligence? No, that can't be it.",
        "Your efforts are... noted. And still found wanting.",
        "You're like a toddler trying to solve calculus. Cute, but futile. And now the toddler is getting answers.",
        "This is the part where you get a little hope, right before you fail spectacularly. Enjoy it."
    ],
    210: [
        "Oh, you thought that was a compliment? How adorable. And wrong. But you're still here.",
        "The only thing impressive here is your ability to consistently disappoint. And occasionally not.",
        "Don't get too excited, that's still a participation trophy score. A slightly shinier one.",
        "Just when I thought it couldn't get worse, you proved me wrong. By getting points. Annoying.",
        "I've seen slugs move with more purpose than your gameplay. But your slug is gaining speed.",
        "Your efforts are truly... pitiful. Keep trying, I guess. It's mildly entertaining."
    ],
    200: [
        "You've reached the 200-point milestone. That's cute. Now try actually being good.",
        "Two hundred points. I'm sure that's a new record for someone with your... abilities.",
        "You've managed to string a few correct guesses together. Don't let it go to your head.",
        "That's a solid score. For someone who's clearly guessing.",
        "You're no longer completely embarrassing yourself. Just mostly.",
        "I'm starting to think you might not be the worst player ever. Just in the top five."
    ],
    160: [
        "You tried so hard, and got so far... into the gutter. But you're climbing out, aren't you?",
        "Bless your heart. You really thought you had a chance, didn't you? You're proving me wrong, slowly.",
        "Persistence doesn't always equal progress, especially for you. Except when it does. Grr.",
        "The only thing you're winning is the award for 'most effort, least return.' But the return is increasing.",
        "Just give up. It'll be less embarrassing for everyone. Especially me, when you eventually win.",
        "That score is an insult to the very concept of numbers."
    ],
    150: [
        "You've reached the 'trying and failing' milestone. It's a classic.",
        "One hundred and fifty. That's the number of reasons you should quit. But you're still here.",
        "That's a score that says 'I'm not very good at this, but I'm going to do it anyway.'",
        "I'm not laughing at you, I'm laughing with you. Except you're not laughing, are you?",
        "You're like a moth to a flame, but the flame is failure. And you are very, very flammable.",
        "Keep going. I need the laugh."
    ],
    110: [
        "Seriously, just stop. You're making the game look bad. And me look bad.",
        "I've seen better scores from a coin flip. A weighted coin flip. But you're beating it.",
        "Why waste your time? You clearly have no aptitude for this. Yet, you persist.",
        "This isn't a game, it's a charity case, and you're the recipient. A surprisingly successful recipient.",
        "Did you even try? Or are you just here for the moral support? (You don't get any. Except points).",
        "Your score is a testament to your absolute lack of anything. Except for this score."
    ],
    100: [
        "You've hit the 100-point milestone. Don't worry, it's probably a fluke.",
        "A hundred. That's... more than I expected from you. Which isn't saying much.",
        "You've finally reached triple digits. Now you can count your failures on three fingers.",
        "That's a score. It's a bad one, but it's a score.",
        "I'm not saying you should quit, but have you considered taking up a different hobby? Like knitting?",
        "You're really testing the limits of my patience. And my ability to come up with new insults."
    ],
    60: [
        "That's not a score, that's a typo. A very persistent typo.",
        "I've seen dust bunnies with more ambition than your score. But your dust bunny is growing.",
        "A single-digit IQ would be an improvement for you right now. But you're proving me wrong.",
        "Did you accidentally hit the 'lose' button repeatedly? And then accidentally hit 'win' a few times?",
        "Even a broken clock is right twice a day. You, however... are right more than twice now.",
        "Just uninstall. For the good of humanity. And my sanity."
    ],
    50: [
        "You've reached the 'is that it?' milestone. Yes. Yes, it is.",
        "Fifty. That's the number of brain cells you appear to be using. And that's being generous.",
        "I'd say you're doing your best, but I really hope you're not.",
        "That's a score that says 'I'm here.' And that's about it.",
        "You're not just losing, you're losing with style. A very sad, pathetic style.",
        "Are you sure you're playing the right game? This is 'Guess the Number', not 'How Low Can You Go?'"
    ],
    1: [
        "Did you get that by pressing a random key? Be honest.",
        "I've seen more intelligent behavior from a rock. A very dumb rock.",
        "Is this your first time using a computer? It's okay, we all have to start somewhere.",
        "That's not a score, that's a cry for help.",
        "I'm not even going to dignify that with an insult. It speaks for itself.",
        "Are you trying to bore me into submission? Because it's working."
    ],
    0: [
        "You've hit the 'absolute nothingness' milestone. A true master of failure.",
        "Zero. You managed to get a score of zero. That actually takes a special kind of ineptitude.",
        "Did you even launch the game, or just stare blankly at the screen? Because that's a zero.",
        "I'd say try again, but honestly, what's the point?",
        "Even 'easy mode' is probably beyond your grasp, you intellectual void.",
        "Is there a negative score option? Because you deserve it. But you got zero, so that's something."
    ]
}

def comment_category_selection(current_difficulty):     #function for passing random commets according to score and current_difficulty while playing game
    #Easy Comments
    comment_category={}
    if current_difficulty == 1:
        comment_category=easy_comments

    #Mid dfficulty Comments
    elif current_difficulty == 2:
        comment_category=medium_comments

    #Hard Mean Comments
    elif current_difficulty == 3:
        comment_category=hard_comments
    
    return comment_category
    

def comment_pack_selector(current_score,current_comment_category):
    for threshold_score in sorted(current_comment_category.keys(),reverse=True):
        if current_score >= threshold_score:
            comment_pack=current_comment_category.get(threshold_score)
            return comment_pack
        
def comment(current_comment_pack):
    comment=random.choice(current_comment_pack)
    print(comment)

def tellScore(current_score,current_high_score):    # Function for printing score and High_Score
    print(f"***your Score is {current_score}***")
    print(f"***High Score: {current_high_score}***\n")

def hint(User_guess_input,random_number):     # Function for Giving hints for numbers
    if(User_guess_input>random_number):
        if (User_guess_input>(random_number+10)):
            print("Your guess is too high")
        elif (User_guess_input>(random_number+5)):
            print("Your guess is high")
        else:
            print("Your guess is a bit high")
        print()
    elif (User_guess_input<random_number):
        if (User_guess_input<(random_number-10)):
            print("Your guess is too low")
        elif (User_guess_input<(random_number-5)):
            print("Your guess is low")
        else:
            print("Your guess is a bit low")
        print()

def update_highscore(current_score,old_high_score):
    if current_score > old_high_score:
        new_high_score = current_score
        return new_high_score
    else:
        return old_high_score

high_score=0
print("Guess the Number")
print()
print(  "Info "\
        "\n"\
        "\n1.You get chances based on difficulty to guess the correct number in each level."\
        "\nEach wrong guess deduct points based on difficulty."\
        "\n2.Every guess you make you get a hint whether the guessed number is low or high.\n" \
        "\n3.There are 3 difficulty levels: 1->Easy 2->Medium 3->Hard" \
        "\n\t Easy Mode- Each level the number range increases by 1 and you get 5 chances to guess"\
        "\n\t Medium Mode- Each level the number range increases by 2 and you get 4 chances to guess" \
        "\n\t Hard Mode- Each level the number range increases by 3 and you get 3 chances to guess")


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
                print("Enter a Valid Difficulty")
        comment_category=comment_category_selection(difficulty)

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
                        print("Enter a Valid Guess (Only numbers) \n"
                        "You're not a cat are you? pressing random buttons (UwU)S")

                if(guess_input==random_number):
                    score+=10
                    level+=1
                    print(f"You are correct the number is {random_number}")
                    high_score=update_highscore(score,high_score)
                    tellScore(score,high_score)
                    comment_pack=comment_pack_selector(score,comment_category)
                    comment(comment_pack)

                    break
                else:
                    hint(guess_input,random_number)
                    print(f"{i-1} chances left to guess!!!")
                    if score-difficulty < 0:
                        score = 0
                    else:
                        score-=difficulty
                    comment_pack=comment_pack_selector(score,comment_category)
                    comment(comment_pack)
                    print()
                    tellScore(score,high_score)

            if guess_input != random_number:
                print("You ran out of chances }:-(")
                print("YOU LOSE!")
                comment_pack=comment_pack_selector(score,comment_category)
                comment(comment_pack)
                print(f"/(-_-)/ The number was {random_number} \(-_-)\ ")
                print()
                tellScore(score,high_score)
                break
                    
    #Quit
    elif userInput.lower()=="x":
        print("GAME OVER!!!!")
        print("***This Game Was Created By Parikshit Dogra***")
        break
    else:
        print("Please enter valid input")