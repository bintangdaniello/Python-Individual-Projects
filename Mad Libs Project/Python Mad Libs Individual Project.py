# import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('400x600')
root.title('DataFlair-Mad Libs Generator')
root.configure(bg='#FDE2E4')

# Header labels
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold', bg='#FDE2E4', fg='black').pack(pady=(10,5))
Label(root, text='Click Any One :', font='arial 15 bold', bg='#FDE2E4', fg='black').pack(pady=(10))
Label(root, text='Daniel Daniello | 2025-12-05', font='arial 15 bold', fg='blue', bg='#FDE2E4').pack(pady=5)


################Stories##############

def madlib1(): # The Photographer
    animals = input("Enter an animal name: ")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a piece of cloth: ")
    things = input("Enter a thing: ")
    name = input("Enter a name: ")
    place = input("Enter a place name: ")
    verb = input("Enter a verb ending with -ing: ")
    food = input("Enter a food name: ")

    print(
        'say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place + ' to get our photos taken today. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + ' .when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')


def madlib2(): # The Butterfly
    adjective = input("Enter an adjective: ")
    color = input("Enter a color name: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place name: ")
    person = input("Enter a person name: ")
    adjective1 = input("Enter another adjective: ")
    insect = input("Enter an insect name: ")
    food = input("Enter a food name: ")
    verb = input("Enter a verb: ")

    print(
        'Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + ' splocthes that looked like ' + thing + ' .I flew to ' + place + ' with my bestfriend and ' + person + ' who was a ' + adjective1 + ' ' + insect + ' .We ate some ' + food + ' when we got there and then decided to ' + verb + ' and the dream ended when I said-- lets ' + verb + '.')


def madlib3(): # Apple and Apple
    person = input("Enter a person name: ")
    color = input("Enter a color: ")
    foods = input("Enter a food name: ")
    adjective = input("Enter an adjective: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    food = input("Enter a food name: ")
    things = input("Enter another thing: ")

    print(
        'Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective + ' apple that looked like a ' + thing + '. When our bag were full, we went on a free hay ride to ' + place + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make apple ' + food + ' and ' + things + ' pies!.')

def madlib4(): # Beach day
    place = input("Enter a place name: ")
    person = input("Enter a person name: ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter another adjective: ")
    noun3 = input("Enter another noun: ")
    number = input("Enter a number: ")
    noun4 = input("Enter another noun: ")
    food = input("Enter a food name: ")
    verb = input("Enter a verb: ")

    print("I went to the beach in " + place + " today with " + person + ". We had a " + adjective1 + " time. We first built a " + noun1 + " and then we ran around in the " + noun2 + " for a little while. The water was a bit " + adjective2 + ". The sun was very " + adjective3 + " so we made sure to wear a lot of " + noun3 + ". We spent " + number + " hours there. At the end of the day, we treated ourselves to a " + noun4 + " and had " + food + " for dinner. I definitely want to go to the beach again but next time I want to " + verb + ".")

def madlib5(): # Going to the movies
    person1 = input("Enter a person name: ")
    person2 = input("Enter another person name: ")
    movie = input("Enter a movie name: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    noun1 = input("Enter a noun: ")
    candy = input("Enter a candy name: ")
    food = input("Enter a food name: ")
    verb2 = input("Enter a verb: ")
    verb3 = input("Enter another verb: ")
    verb4 = input("Enter another verb: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter another adjective: ")
    adjective4 = input("Enter another adjective: ")
    adjective5 = input("Enter another adjective: ")

    print("I went to the movies yesterday with " + person1 + " and " + person2 + " We saw " + movie + ". It was " + adjective1 + ". At one part, I even " + verb1 + " and ran for the " + noun1 + ". During the move, we ate " + candy + " and " + food + ". I got mad because the person sitting behind me kept " + verb2 + " during the movie and wouldn't stop " + verb3 + ". He was asked to leave after he " + verb4 + " across the theatre. It was pretty " + adjective2 + ". Overall, I liked the movie because it was " + adjective3 + " and the main character was super " + adjective4 + ". Hopefully next time the people sitting behind me will be more " + adjective5 + ".")

def madlib6(): # Flying to Australia
    noun1 = input("Enter a noun: ")
    number = input("Enter a number: ")
    noun2 = input("Enter another noun: ")
    food = input("Enter a food name: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    work = input("Enter a type of work/job: ")
    noun3 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter a verb: ")
    verb3 = input("Enter another verb: ")
    adjective3 = input("Enter another adjective: ")

    print("I decided to go on a vacation to Australia with " + noun1 + ". We got to the airport " + number + " hours early. When we went through security, I got stopped because I forgot to take " + noun2 + " out of my pocket. We got some " + food + " for the flight and arrived at the gate. Once we boarded the plane, I was sitting next to a very " + adjective1 + " man. He spent the entire flight " + verb1 + " and talking about his job doing " + work + ". Whenever I tried to sleep, he would step around me to go to the " + noun3 + ". I was so " + adjective2 + ". Since I couldn't sleep, I decided to " + verb2 + " and " + verb3 + " instead. Finally, we arrived in Australia. All in all, the flight was " + adjective3 + ".")


# Buttons to select stories
Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='#A8E6CF', fg='black').pack(pady=10, fill='x', padx=50)
Button(root, text='Apple and Apple', font='arial 15', command=madlib3, bg='#FFD3B6', fg='black').pack(pady=10, fill='x', padx=50)
Button(root, text='The Butterfly', font='arial 15', command=madlib2, bg='#A8E6CF', fg='black').pack(pady=10, fill='x', padx=50)
Button(root, text='Beach Day', font='arial 15', command=madlib4, bg='#FFD3B6', fg='black').pack(pady=10, fill='x', padx=50)
Button(root, text='Going to the movies', font='arial 15', command=madlib5, bg='#A8E6CF', fg='black').pack(pady=10, fill='x', padx=50)
Button(root, text='Flying to Australia', font='arial 15', command=madlib6, bg='#FFD3B6', fg='black').pack(pady=10, fill='x', padx=50)



root.mainloop()
