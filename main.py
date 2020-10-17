from includes import voice2text
from includes import record
from includes import text2sign
import threading
import time

words = []
threads = []
RUNNING = True

def compileVideo():
	curPos = 0
	while RUNNING or curPos < len(words):
		#print(words)
		if curPos < len(words) and words[curPos] != None:
			chunk = words[curPos]
			l = chunk.strip().split(' ')
			for word in l:
				if word in ['', ' ']:
					continue
				text2sign.fetchWord(word, curPos)
			curPos += 1
	clips = [word for word in words if word not in ['', ' ', None]]
	if len(clips) > 0:
		text2sign.finalMerge(clips)

if __name__ == '__main__':
	print('Mic started.\nNOTE :: Use keyboard interupt for stopping.')
	file_num = 0
	converterThread = threading.Thread(target=compileVideo, args=())
	converterThread.start()
	while True:
		try:
			file_name = './data/{}.wav'.format(file_num)
			record.record_to_file(file_name)
			words.append(None)
			thread = threading.Thread(target=voice2text.getWord, args=(file_name, words, file_num))
			thread.start()
			threads.append(thread)
			file_num += 1
		except KeyboardInterrupt:
			break
	for thread in threads:
		thread.join()
	RUNNING = False
	print(' '.join(words).strip())
	converterThread.join()
