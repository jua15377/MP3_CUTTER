from pydub import AudioSegment
from time import asctime

file_name = 'AUDIO 12-07-19 Part 2'

startMin = 9
startSec = 0

# endMin = 405
# endSec = 58

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
# endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment
print('reading', asctime())
song = AudioSegment.from_mp3(file_name+'.mp3')
print('cutting', asctime())
extract = song[startTime:len(song)]

# Saving
print('saving', asctime())
extract.export(file_name+'-cortado.mp3', format="mp3", bitrate='128k')
print('DONE!', asctime())