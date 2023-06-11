
"""
first just take The name of the lessons (maybe in a Dict(Fr:En)),
	then check the Doc for the Keys of that Dict and look for the Teacher of it

	for showing it i have no idea at this point!
"""


import re
from PyPDF2 import PdfReader

def Get_Lessons(reader):
	"""
		Will get the two pages (3, 4) and add the names of lessons to a dict
	"""

	Lessons = dict()
	for i in [2, 3]:
		page = reader.pages[i]
		text = page.extract_text()
		l = re.findall("(.*\d\s+)(.*)([a-zA-Z]*)\s+", text)
		for i in range(3, len(l)):
			print(l[i][1].rstrip())
		break

def main():
	reader = PdfReader("ms-ds-00.pdf")
	Get_Lessons(reader)

# make it to run it self!
main()