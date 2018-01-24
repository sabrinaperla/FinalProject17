# players have to type in their name, their crushes name, and their pronouns

crushpronoun= input("What is your crush's pronoun? ex. she/he/they ").lower()
yourpronoun= input("What is your pronoun? ex. she/he/they ").lower()
crushname= input("What is your crush's name? ")
name= input("What is your name?")

# according to the player's crush's pronoun, the following chooses the correct object and possesive pronouns

if crushpronoun == 'he':
    object_pronoun = 'him'
    possessive_pronoun = 'his'
if crushpronoun == 'she':
    object_pronoun = 'her'
    possessive_pronoun = 'hers'
if crushpronoun == 'they':
    object_pronoun = 'them'
    possessive_pronoun = 'theirs'




#the following is the story that the pronouns and names will be input into

story = """You and {} have been best friends forever; perhaps not forever, but for as long as either of you can remember.
Prom is rapidly approaching; 4 weeks away to be exact. You secretly want {} to ask you, and {} secretly wants to ask you.
But you are both aware of the elephant in the room; what if things don’t work out?
You decide life is too short to worry about if’s, so you convince yourself to ask your best friend before it’s too late.
You are planning a scavenger hunt promposal with your crushes favorite things.
You will tell your crush to go to {} favorite places, where {} will hopefully find a piece of the heart.
The catch is: if your hints don't lead your crush to their favorite place, {} won’t find a piece of the heart.
At the end, {} will hopefully have enough pieces to complete your half of the heart, and you will go happily to prom together.
""".format(crushname, object_pronoun, crushpronoun, object_pronoun, crushpronoun, object_pronoun, crushpronoun, crushpronoun, object_pronoun)

rules = """You will be asked 20 questions, you need to get at least 15 right in order for your crush to complete the scavenger height. For the following multiple choice questions, only answer the letter. If the answer is d only type in d"""
# the following is the multiple choices that their crush will follow to find the next clue in the scavenger hunt

class Crush():
    def __init__(self):
        self.question1 = """What is your crush’s favorite fast food restaurant? Hint: freshly made
        a. McDonalds
        b. Burger King
        c. Wendy’s
        d. Chick-fila
        """
        self.answer1 = 'c'
        self.question2 = """What is your crush’s favorite pizzeria? Hint: favorite order is panmade pizza
        a. Dominos
        b. Pizza Hut
        c. Little Caesars
        d. Papa John’s
        """
        self.answer2 = 'a'
        self.question3 = """What is your crush’s favorite restaurant? hint: seafood
        a. Olive Garden
        b. Red Lobster
        c. Applebee’s
        d. TGI Friday
        """
        self.answer3 = 'b'
        self.question4 = """What is your crush’s favorite breakfast spot? hint: it's packed on weekends
        a. IHOP
        b. Diner
        c. Denny’s
        d. Dunkin Donuts
        """
        self.answer4 = 'a'
        self.question5 = """What is your crush’s favorite place to get subs? hint: it has a catchy name
        a. Quickchek
        b. Wawa
        c. Subway
        d. Quiznos
        """
        self.answer5 = 'b'
        self.question6 = """What is your crush’s favorite mexican restaurant? hint: real burritos
        a. Chipotle
        b. Qdoba
        c. Chevy’s
        d. Authentic
        """
        self.answer6 = 'd'
        self.question7 = """What is your crush’s favorite fun thing to do? hint: action
        a. Lasertag
        b. Trampolines
        c. Paintball
        d. Go-karts
        """
        self.answer7 = 'a'
        self.question8 = """What is your crush’s favorite superhero? hint: fought the nazis
        a. Superman
        b. Batman
        c. Spiderman
        d. Captain America
        """
        self.answer8 = 'd'
        self.question9 = """What is your crush’s favorite cartoon? hint: It is on nickelodeon
        a. Spongebob
        b. Tom and Jerry
        c. Fairly Odd Parents
        d. Power Puff Girls
        """
        self.answer9 = 'a'
        self.question10 = """What is your crush’s favorite Nickelodeon show? hint: Sam is in it
        a. iCarly
        b. Sam and Cat
        c. Victorious
        d.Big Time Rush
        """
        self.answer10 = 'a'
        self.question11 = """What is pet does your crush own? Hint: It has white fur
        a. Dog
        b. Cat
        c. Fish
        d. Bunny
        """
        self.answer11 = 'd'
        self.question12 = """How many siblings does your crush have?
        a. 1
        b. 2
        c. 3
        d. 4
        """
        self.answer12 = 'c'
        self.question13 = """Where did you and your crush meet? hint: basic teenage love story
        a. School
        b. The movies
        c. The mall
        d. A party
        """
        self.answer13 = 'a'
        self.question14 = """What is your crush’s best feature? hint: it's what's in the heart that matters
        a. Smile
        b. Eyes
        c. Hair
        d. Personality
        """
        self.answer13 = 'd'
        self.question14 = """What is your crush’s favorite season? Hint: you have a break
        a. Winter
        b. Spring
        c. Summer
        d. Fall
        """
        self.answer14 = 'c'
        self.question15 = """What is your crush’s favorite subject? Hint: It involves numbers
        a. Math
        b. Science
        c. English
        d. History
        """
        self.answer15 = 'a'
        self.question16 = """What sport does your crush play? Hint: It is played indoors
        a. Football
        b. Soccer
        c. Basketball
        d. Baseball
        """
        self.answer16 = 'c'
        self.question17 = """What kind of car does your crush have? hint: _____ murano
        a. Toyota
        b. Ford
        c. Honda
        d. Nissan
        """
        self.answer17 = 'd'
        self.question18 = """What is your crush’s favorite female rapper? Hint: these expensive, these is red bottoms, these is bloody shoes
        a. Cardi B
        b. Nicki Minaj
        c. Remy Ma
        d. Lil Kim
        """
        self.answer18 = ' a'
        self.question19 = """What is your crush's favorite male rapper? Hint: I know when that hotline bling, that could only mean one thing
        a. Lil Wayne
        b. Drake
        c. Lil Uzi
        d. Kodak Black
        """
        self.answer19 = 'b'
        self.question20 = """What is your crush's favorite pop artist? Hint: work, work, work, work, work, work
        a. Katy Perry
        b. Rihanna
        c. Beyonce
        d. Taylor Swift
        """
        self.answer20 = 'b'


print(story)
print(rules)

#the following will make sure you're answering questions in order

c = Crush()
questions = [c.question1, c.question2, c.question3, c.question4, c.question5, c.question6, c.question7, c.question8, c.question9, c.question10, c.question11, c.question12, c.question13, c.question14, c.question15, c.question16, c.question17, c.question18, c.question19, c.question20]
answers = [c.answer1, c.answer2, c.answer3, c.answer4, c.answer5, c.answer6, c.answer7, c.answer8, c.answer9, c.answer10, c.answer11, c.answer12, c.answer13, c.answer14, c.answer15, c.answer16, c.answer17, c.answer18, c.answer19, c.answer20]
question_counter = 0
heart_counter = 0

#the following will lead you to the next question and track and update you of how many you have right so far

while question_counter <= 19:
    user_answer = input(questions[question_counter])
    if user_answer == answers[question_counter]:
        heart_counter += 1
        print(f"Good job! You found {heart_counter} out of the 20 pieces of your heart. Now proceed to find another piece.")
        question_counter += 1
    elif user_answer != answers[question_counter]:
        print(f"Sorry that was wrong! You still have {heart_counter} out of the 20 pieces of your heart. Now proceed to find another piece. ")
        question_counter += 1
    else:
        print("That's not an option. Better luck next time! ")

#the following will count if you have enough right answers that lead you to the end of the scavenger hunt

if heart_counter >= 15:
        print(f"Congratulations your crush has successfully gone through the scavenger hunt and found enough hints to lead them to you. You can now prompose to them!")
elif heart_counter <= 15:
        print(f"Turns out you don't know your crush as well as you thought you did. Your crush got lost in the scavenger hunt!")