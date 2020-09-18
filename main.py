import data
import numpy

user = 'F'

def set_root(root_note):
    '''From C chromatic scale, returns a chromatic scale based on what root user's choose'''
    
    for index, enharmonic_notes in enumerate(data.notes):
        
        if enharmonic_notes[0] == user or enharmonic_notes[1] == user:
            
            offset = [0 if enharmonic_notes[0] == user else 1]
            rolled_notes = numpy.roll(data.notes, -index*2)
            
            break

    return pattern_to_notes(offset, rolled_notes)


desired_scale = []
def pattern_to_notes(offset, rolled_notes):
    '''Transform the intevals of a scale, chord, mode... on musical notes'''

    for interval in data.musical_toolkit[0][2]:

        for index, intervals in enumerate(data.intervals):

            if intervals[0] == interval:

                correct_note = rolled_notes[index][0 + offset[0]]
                
                if correct_note[0] not in [note[0] for note in desired_scale]:
                    
                    desired_scale.append(correct_note)

                else:

                    correct_note = rolled_notes[index][1-offset[0]]
                    desired_scale.append(correct_note)
                
                break

            elif intervals[1] == interval:

                correct_note = rolled_notes[index][0 + offset[0]]
                
                if correct_note[0] not in [note[0] for note in desired_scale]:
                    
                    desired_scale.append(correct_note)

                else:

                    correct_note = rolled_notes[index][1-offset[0]]
                    desired_scale.append(correct_note)
                
                break
        
            else: 

                continue

    return desired_scale


print(set_root(user))