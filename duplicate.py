import os

def arrTotext(res):
	str1 = '\n'
	return (str1.join(res))

def welcome():
	print('Selamat datang\n yang mau mengembangkan script ini silahkan komen di\n https://github.com/ahmad190617/findDup\n tolong hargai owner dengan cara tidak menghilangkan hak cipta\n\t\tsalam hangat dari cr4r\n\nsilahkan ketik letak/nama file anda misalkan (/sdcard/disini.txt)')


def find_dup_char(input):
	t = input('letak file : ')
	input = open(str(t),'r').read().split('\n')
	res = sorted(set(input), key = lambda ele: input.count(ele))
	tex = arrTotext(res)
	open('output.txt','w+').write(str(tex)).close()
	print ('Done, file telah tersimpan bernama output.txt')


if __name__ == "__main__":
	os.system('clear')
	welcome()
	find_dup_char(input) 
