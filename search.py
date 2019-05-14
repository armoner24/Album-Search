import sys
file=open("records.txt","r")
text_search=sys.argv[1]
count=0
song_save=[]
for song in file:
	if text_search in song:
		song_save.append(song.strip())
		count+=1
file.close()
print song_save, ':-  '+str(count)+' matches found for the given query.'



