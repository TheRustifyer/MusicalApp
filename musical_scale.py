import data
import numpy

class MusicalPattern:

	def __init__(self, genre, name, pattern, user):

		self.genre = genre
		self.name = name
		self.pattern = pattern


	def set_root(root_note):
	    '''From C chromatic scale, returns a chromatic scale based on what root user's choose'''
	    for index, enharmonic_notes in enumerate(data.notes):
	        if enharmonic_notes[0] == user or enharmonic_notes[1] == user:
	            self.offset = [0 if enharmonic_notes[0] == user else 1]
	            self.rolled_notes = numpy.roll(data.notes, -index*2)
	            break
	def pattern_to_notes():
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
	                
	                if correct_note[0] not in [note[0] for note in desired_scale]:
	                    
	                    desired_scale.append(correct_note)

	                else:

	                    correct_note = self.rolled_notes[index][1-self.offset[0]]
	                    desired_scale.append(correct_note)
	                
	                break
	        
	            else: 

	                continue



musical_db = [MusicalPattern(instance[0], instance[1], instance[2]) for instance in data.musical_toolkit]
final_name = [musicalobject.pattern for musicalobject in musical_db]


