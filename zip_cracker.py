import zipfile
import rarfile
import string
rarfile.UNRAR_TOOL = "unrar.exe"

def extract_dict():
	word_list = []
	with open('rockyou.txt','rb') as f:
		word = f.read()
		for i in word.split():
			word_list.append(str(i,'latin-1'))
	return word_list



def brute(word_list,path):
		try:
		z = rarfile.RarFile(PATH,'r')

		print("passed tis")
		print (z.namelist())

		for pwd in word_list:
			print("==============================")
			print ("TESTING: "+pwd)
			print("==============================")
			try:
			
				z.extract(z.namelist()[1],pwd=pwd)
			except Exception as e:
				pass
		z.close()
	except Exception as e:
		print (e)

#brute()
print("==============================")
print("TRYHARDBOI CRACKER LAUNCHING")
print("==============================")
word_list = extract_dict()

print("==============================")
print("WORD LIST EXTRACTED")
print("==============================")
brute(word_list)