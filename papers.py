# HANDLES PAPERS AS OBJECTS ( INDEX, GRADE/CITATIONS, AUTHOR )
# AS WELL AS GENERATING COLLECTIONS OF PAPERS, NAMES AND GRADES
import os, random, papers
import names_generator as names
from dotenv import load_dotenv

load_dotenv()
SIM_DAILY_LIMIT_MAX_PAPERS = int(os.getenv('SIM_DAILY_LIMIT_MAX_PAPERS'))
SIM_DAILY_LIMIT_MAX_FAVORITES = int(os.getenv('SIM_DAILY_LIMIT_MAX_FAVORITES'))

def genAuthorName():
    Fname = names.generate_name(style='capital').split(" ")
    Lname = Fname
    while Lname == Fname:
        Lname = names.generate_name(style='capital').split(" ")
    name = Fname[1][0] + "."+ Lname[1]
    return name
class Paper:
    def __init__(self):
        self.index = None
        self.grade = random.randint(0, 1000)/10
        self.author = genAuthorName()
    def setIndex(self, index):
        self.index = index
    def setGrade(self, grade):
        self.grade = grade
    def getIndex(self):
        return self.index
    def getGrade(self):
        return self.grade
    def getAuthor(self):
        return self.author
def generatePapers(sequence_size):
    seq = []
    while sequence_size > 0:
        seq.append(papers.Paper())
        sequence_size -= 1
    return seq
def convertGradesToIntegers(papers_with_decimals):
    for paper in papers_with_decimals:
        paper.setGrade(int(paper.getGrade()*10))
    return papers_with_decimals  # converted
def convertGradesBackToDecimals(papers_with_integers):
    print("this is not working")
    for paper in papers_with_integers:
        paper.setGrade(float(paper.getGrade()/10))
    return papers_with_integers  # converted
def genNumPapers():  # 10 .. 100 inclusive
    return random.randint(10, SIM_DAILY_LIMIT_MAX_PAPERS)
def genNumFavorites(num_total_papers):  # 10 .. sizeOf(total_papers) inclusive
    return random.randint(2, SIM_DAILY_LIMIT_MAX_FAVORITES)
def printPapers(janes_papers):
    print()
    for p in janes_papers:
        print(f"[{p.getIndex()}] grade= {p.getGrade()} || author= {p.getAuthor()}")
def resetPaperIndices(janes_papers):
    for i, p in enumerate(janes_papers):
        p.setIndex(i + 1)
    return janes_papers
