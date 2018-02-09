import pandas as pd
import numpy as np

class course():
    def __init__(self, category, name, prof):
        self.category = category
        self.name = name
        self.prof = prof
        self.comments = []
    def addComment(self, comment):
        self.comments.append(comment)
    def addPrereq(self, prereq):
        self.prereq = str(prereq)
    def addAlsoTake(self, alsoTake):
        self.alsoTake = str(alsoTake)
    def dump(self, f):
        f.write('\n')
        f.write('> {}\n'.format(self.name))
        f.write('\n')
        f.write('* 開課教授：{}\n'.format(self.prof))
        if self.alsoTake != 'nan':
            f.write('* 推薦同時修習的課程：{}\n'.format(self.alsoTake))
        if self.prereq != 'nan':
            f.write('* 推薦預先修習的課程：{}\n'.format(self.prereq))
        f.write('* 課程小卦：\n')
        for comm in self.comments:
            f.write(' - {}\n'.format(comm))


data = np.array(pd.read_csv('../dat/elective.csv', header=None))

category = {}

for row in data:
    course_i = course(row[0], row[1], row[2])
    #if row[3] != 'nan':
    course_i.addAlsoTake(row[3])
    #if row[4] != 'nan':
    course_i.addPrereq(row[4])
    for i in range(5,10):
        if str(row[i]) == 'nan':
            break
        else:
            course_i.addComment(row[i])

    if row[0] in category:
        category[row[0]].append(course_i)
    else:
        category[row[0]] = [course_i]

for cate in category:
    with open('../106-1/elective/{}.md'.format(cate), 'w') as f:
        f.write('# {}\n'.format(cate))
        for course_i in category[cate]:
            course_i.dump(f)


