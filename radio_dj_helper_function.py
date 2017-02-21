# https://www.codewars.com/kata/radio-dj-helper-function

def longest_possible(playback):
    playback_str = '{:02d}:{:02d}'.format(*divmod(playback, 60))
    longest = {}
    for song in songs:
        if longest.get('playback', '') < song.get('playback') < playback_str:
            longest = song
    return longest.get('title', False)