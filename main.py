import data
from musical import MusicalPicker


if __name__ == '__main__':

    #Told me which musical note u want to work with
    user_desired_root = input('Introduce una nota musical: \n').capitalize()[0]

    #Showing the user a simply command-line mode of choose musical things
    user_genre_set = set([row[0][0] for row in data.musical_toolkit])
    user_genre_selection = {key + 1 : value for key, value in enumerate(user_genre_set)}
    print('')
    for key, value in user_genre_selection.items():
        print(f'{key} -> {value}')

    # Ckecking the user's IQ 
    user_genre_input = ''
    while user_genre_input not in user_genre_selection.keys():

        user_genre_input = int(input('\nIntroduce el número de una de las opciones disponibles: \n'))

    user_genre_input = user_genre_selection.get(user_genre_input)
    

    # And finally, select the desired musical scale
    scale_availiable_options = [scale[1][0] for scale in data.musical_toolkit if scale[0][0] == user_genre_input]

    scale_availiable_options_dict = {option + 1 : scale for option, scale in enumerate(scale_availiable_options)}
    print('')

    for key, value in scale_availiable_options_dict.items():
        print(f'{key} -> {value}')

    scale_type = ''
    while scale_type not in scale_availiable_options_dict.keys():

        scale_type = int(input('\nIntroduce una de las opciones disponibles: \n'))
        print('')

    scale_type = scale_availiable_options_dict.get(scale_type)

    for row in data.musical_toolkit:

        if row[1][0] == scale_type and row[0][0] == user_genre_input:
            pattern = row[2]

    # And finally, our object giving us back the desired INFO :)
    my_music_tool = MusicalPicker(user_desired_root, scale_type, user_genre_input, pattern)

    # Set root gives us back a chromatic scale starting on the designed root.
    rotated_scale = my_music_tool.set_root()

    print(my_music_tool)
    print(my_music_tool.pattern_to_musical_thing(rotated_scale))
