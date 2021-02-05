import data

class MusicalPicker:

    def __init__(self, root_note, scale_type, scale_genre, pattern, *args, **kwargs):
        
        self.root = root_note
        self.pattern = pattern
        self.scale_type = scale_type
        self.scale_genre = scale_genre

        self.rolled_notes = []
    
    def __str__(self):
        return 'The {self.root} {self.scale_type} {self.scale_genre}:'.format(self=self)

    def set_root(self):
        '''From C chromatic scale, returns a chromatic scale based on what root user's choose.
            
            This particulary weird little method is designed to avoid use NumPy in order
            to fetch the correct note's order when root is selected.'''

        for index, enharmonic_notes in enumerate(data.notes):
            
            if enharmonic_notes[0] == self.root or enharmonic_notes[1] == self.root:

                self.rolled_notes.append(data.notes[index:])
                self.rolled_notes.append(data.notes[:index])

        behind_the_index = self.rolled_notes[0]
        ahead_of_index = self.rolled_notes[1]

        self.rolled_notes.clear()
        
        for list_tuple in behind_the_index:
            self.rolled_notes.append(list_tuple)
        for list_tuple in ahead_of_index:
            self.rolled_notes.append(list_tuple)

        paired_rolled_notes = list(zip(self.rolled_notes, data.intervals))
        
        return paired_rolled_notes


    def pattern_to_musical_thing(self, scale_with_intervals):

        final_scale = []
        final_scale.append(self.root)

        for matched_tuple in scale_with_intervals[1:]:
            
            for interval in self.pattern:
                
                if interval in matched_tuple[1]:
                    
                    if interval == matched_tuple[1][0]:
                        right_choice = 0
                        final_scale.append(matched_tuple[0][right_choice])

                    else:
                        right_choice = 1
                        final_scale.append(matched_tuple[0][right_choice])

        return f"- {', '.join(final_scale)}"

