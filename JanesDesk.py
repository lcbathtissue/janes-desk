import papers, test, radixSort
# RADIX SORT ==> Dimitrije Stamenic , https://stackabuse.com/radix-sort-in-python/

# SIMULATION SETTINGS
full_year = False
if full_year:
    number_cycles = 365
else:
    number_cycles = 6

# INITIALIZE THE DAY ONE PAPERS
day = 1
number_papers = papers.genNumPapers()  # 10 .. 100 inclusive
number_favorites = papers.genNumFavorites(number_papers)  # 10 .. number_papers inclusive

janes_papers = papers.generatePapers(number_papers)  # creates day 1 papers
janes_papers = papers.resetPaperIndices(janes_papers)  # assigns indices to papers
answers = test.findNTrueMaxes(janes_papers, number_favorites)  # *** CONFIRMATION ONLY
print(f"DAY {day}\nnFAVS= {number_favorites} , ANS: {answers}")  # day 1
# papers.printPapers(janes_papers)  # print papers as generated

# [1/3] START OF ALGORITHM
janes_papers = papers.convertGradesToIntegers(janes_papers)
janes_papers = radixSort.radixSort(janes_papers)  # initial sort
janes_papers = list(reversed(janes_papers))  # REMOVE THIS AFTER MODIFYING RADIX SORT ALGORITM
papers.printPapers(janes_papers)
print("^ list after radix sorting")

# [2/3] DAY 1 FAVORITES
print()
janes_favorites = []
while number_favorites > 0:
    next_favorite = janes_papers.pop(0)
    print(f"{next_favorite.getGrade()} || {next_favorite.getAuthor()}")
    janes_favorites.append(next_favorite)
    number_favorites -= 1
print("^ favorites determined by algorithm")

# [3/3] RECURRENCE FOR N CYCLES/DAYS
while number_cycles > 1:
    # HANDLE NEW DAILY PAPERS
    day += 1
    new_papers = papers.generatePapers(10)  # papers.genNumPapers())  # creates day 1 papers
    new_papers = papers.resetPaperIndices(new_papers)  # assigns indices to papers
    number_favorites = 3  # papers.genNumFavorites(number_papers)
    print(f"\nDAY {day}\nNEW PAPERS:", end="")  # \nANS: {answers}")
    papers.printPapers(new_papers)
    answers = test.findNTrueMaxes(new_papers, number_favorites)  # *** CONFIRMATION ONLY

    # AMALGAMATE NEW PAPERS INTO COLLECTION
    new_papers = papers.convertGradesToIntegers(new_papers)
    for new_paper in new_papers:
        janes_papers.append(new_paper)
    answers = test.findNTrueMaxes(janes_papers, number_favorites)  # *** CONFIRMATION ONLY
    papers.resetPaperIndices(janes_papers)
    print(f"\nALL PAPERS:\nnFAVS= {number_favorites} , ANS: {answers}", end="")
    janes_papers = radixSort.radixSort(janes_papers)  # initial sort
    janes_papers = list(reversed(janes_papers))  # REMOVE THIS AFTER MODIFYING
    papers.printPapers(janes_papers)
    print("^ list after radix sorting\n")

    # DAY N FAVORITES
    janes_favorites = []
    while number_favorites > 0:
        next_favorite = janes_papers.pop(0)
        print(f"{next_favorite.getGrade()} || {next_favorite.getAuthor()}")
        janes_favorites.append(next_favorite)
        number_favorites -= 1
    print("^ favorites determined by algorithm")

    number_cycles -= 1
