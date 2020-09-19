import data
import numpy

class MusicalPattern:

    def __init__(self, genre, name, pattern, user):

        self.genre = genre
        self.name = name
        self.pattern = pattern
        self.set_root(user)
        self.pattern_to_notes()


    def set_root(self, root_note):
        '''From C chromatic scale, returns a chromatic scale based on what root user's choose'''
        for index, enharmonic_notes in enumerate(data.notes):
            
            if enharmonic_notes[0] == root_note or enharmonic_notes[1] == root_note:
                
                self.offset = [0 if enharmonic_notes[0] == root_note else 1]
                self.rolled_notes = numpy.roll(data.notes, - index * 2)
                
                break
                
    def pattern_to_notes(self):
        '''Transform the intevals of a scale, chord, mode... on musical notes'''

        self.desired_scale = []
        
        for interval in self.pattern:

            for index, intervals in enumerate(data.intervals):

                if intervals[0] == interval:

                    correct_note = self.rolled_notes[index][0 + self.offset[0]]
                    
                    if correct_note[0] not in [note[0] for note in self.desired_scale]:
                        
                        self.desired_scale.append(correct_note)

                    else:

                        correct_note = self.rolled_notes[index][1-self.offset[0]]
                        self.desired_scale.append(correct_note)
                    
                    break

                elif intervals[1] == interval:

                    correct_note = self.rolled_notes[index][0 + self.offset[0]]
                    
                    if correct_note[0] not in [note[0] for note in self.desired_scale]:
                        
                        self.desired_scale.append(correct_note)

                    else:

                        correct_note = self.rolled_notes[index][1-self.offset[0]]
                        self.desired_scale.append(correct_note)
                    
                    break
            
                else: 

                    continue

#Told me which musical note u want to work with
user_input = input('Introduce una nota musical: \n').capitalize()

#Showing the user a simply command-line non really graphical mode of choose things avoiding type in str mode.
user_genre_set = set([row[0][0] for row in data.musical_toolkit])
user_genre_selection = {key+1 : value for key, value in enumerate(user_genre_set)}
for key, value in user_genre_selection.items():
    print(f'{key} -> {value}')

#Ckecking the IQ of the user
user_genre_input = ''
while user_genre_input not in user_genre_selection.keys():

    user_genre_input = int(input('Introduce una de las opciones disponibles: \n'))

user_genre_input = user_genre_selection.get(user_genre_input)

#And finally, go select the desired musical scale

scale_availiable_options = [scale[1][0] for scale in data.musical_toolkit if scale[0][0] == user_genre_input]

scale_availiable_options_dict = {option+1 : scale for option, scale in enumerate(scale_availiable_options)}

for key, value in scale_availiable_options_dict.items():
    print(f'{key} -> {value}')

user_name_input = ''
while user_name_input not in scale_availiable_options_dict.keys():

    user_name_input = int(input('Introduce una de las opciones disponibles: \n'))

user_name_input = scale_availiable_options_dict.get(user_name_input)

for row in data.musical_toolkit:

    if row[1][0] == user_name_input and row[0][0] == user_genre_input:

        choosen_pattern = row[2]


final_scale = MusicalPattern(user_genre_input, user_name_input, choosen_pattern, user_input)
print(final_scale.desired_scale)
