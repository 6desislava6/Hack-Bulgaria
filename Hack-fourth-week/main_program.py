from MusicPlayer import MusicPlayer


def show_commands():
    print('Press "D" to add new directory with mp3 songs')
    print('Press "SM" to change shuffle mode')
    print('Press "RM" to change repeat mode')
    print('Press "P" to play next song')
    print('Press "S" to stop playing at all')
    print('Press "SP" to show playlist')
    print('Press "Q" to quit')


def main():
    music_player = MusicPlayer()

    print('Hello! Welcome to Panda Music Player!')
    print('/Panda because I could not figure out another name.../')
    print('Type "list" to show all commads')
    show_commands()
    switchOn = True
    while(switchOn):
        input_command = input('Type command here: ')
        if input_command == "Q":
            music_player.stop_playing_all()
            switchOn = False
            break
        elif input_command == "D":
            directory = input('Write the path to your directory: ')
            music_player.add_songs_from_dir(directory)
        elif input_command == "SM":
            shuffle = bool(input('write True or False'))
            music_player.change_shuffle_mode(shuffle)
        elif input_command == "RM":
            repeat = bool(input('write True or False'))
            music_player.change_shuffle_mode(repeat)
        elif input_command == "P":
            music_player.stop_playing_all()
            music_player.play_next_song()
        elif input_command == "S":
            music_player.stop_playing_all()
        elif input_command == "SP":
            music_player.show_playlist()
        elif input_command == "list":
            show_commands()
        else:
            print('Invalid command!')

if __name__ == '__main__':
    main()
