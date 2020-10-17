import requests
import moviepy.editor as mp
import shutil
import os

def fetchWord(word, curPos):
	print(word)
	oWord = word
	cacheWords = os.listdir('./cache')
	if oWord+'.mp4' in cacheWords:
		return
	word = ''.join([a.lower().strip("!,.?") for a in word.split()])
	link = 'https://handspeak.com/word/{}/{}.mp4'.format(word[0], word)
	print(link)
	result = requests.get(link)
	if result.text[:15] == '<!DOCTYPE html>':
		c = []
		for l in word:
			if l.isalpha():
				c.append(mp.VideoFileClip('./letters/{}-abc.mp4'.format(l)))#.resize(height=320, width=240)
		f = mp.concatenate_videoclips(c, method="compose")
		f.write_videofile('./cache/{}.mp4'.format(oWord))
		#return mp.VideoFileClip('./data/{}.mp4'.format(curPos))#.resize(height=320, width=240)
	else:
		f = open('./cache/{}.mp4'.format(oWord), 'wb')
		for chunk in result.iter_content(chunk_size=255):
			if chunk:
				f.write(chunk)
		f.close()
		#return mp.VideoFileClip('./data/{}.mp4'.format(curPos))#.speedx(factor=0.5)#.resize(height=320, width=240)

def finalMerge(words):
	clips = [mp.VideoFileClip('./cache/{}.mp4'.format(word)).resize(height=320, width=240) for word in words]
	final_clip = mp.concatenate_videoclips(clips, method="compose")
	final_clip.write_videofile("final_clip.mp4")
