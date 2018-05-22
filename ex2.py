import timeit

CONST_H_LENGTH = 31
CONST_LINE_LENGTH = 21


def getColumnIndex(col_name):
    """
    The function return the index of col_name
    :param col_name: the name of the column
    """
    if col_name == 'lid':
        return 0
    if col_name == 'loan_amount':
        return 1
    if col_name == 'currency':
        return 2
    if col_name == 'sector':
        return 3


class Heap(object):

    def __init__(self, file_name):
        """
        :param file_name: the name of the heap file to create. example: kiva_heap.txt
        """
        self.m_myFileName = "heap_index_file_%s" % file_name
        self.lastIndex = 0

    def create(self, source_file):
        """
        The function create heap file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        my_index_file = open("%s" % self.m_myFileName, "w+")
        with my_index_file:
            try:
                sourceFile = open("%s" % source_file, "r")
            except IOError:
                print "Could not open file!"
            with sourceFile:
                for line in sourceFile:
                    my_index_file.write("%s" % line)
                    self.lastIndex += 1
                my_index_file.close()
                sourceFile.close()

    def insert(self, line):
        """
        The function insert new line to heap file
        :param line: string reprsent new row, separated by comma. example: '653207,1500.0,USD,Agriculture'
        """
        index_file = open("%s" % self.m_myFileName, "a")
        with index_file:
            index_file.write("%s\n" % line)
            self.lastIndex += 1
            index_file.close()

    def delete(self, col_name, value):
        """
        The function delete records from the heap file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param col_name: the name of the column. example: 'currency'
        :param value: example: 'PKR'
        """
        # index_file = open("index_file_%s" % self.m_myFileName, "r+")
        heap_file = open("%s" % self.m_myFileName, "r+")
        helper_file = open("helper_file_%s" % self.m_myFileName, "w+")
        index = 0
        columnIndex = getColumnIndex(col_name)
        with heap_file:
            for line in heap_file:
                if line.split(",")[columnIndex] == value:
                    helper_file.write(line.replace(line, "#%s" % line[1:]))
                else:
                    helper_file.write(line)
            heap_file.close()
        helper_file.seek(0)
        heap_file = open("%s" % self.m_myFileName, "w+")
        with heap_file:
            for line in helper_file:
                heap_file.write(line)
        helper_file.close()
        heap_file.close()

    def update(self, col_name, old_value, new_value):
        """
        The function update records from the heap file where their value in col_name is old_value to new_value.
        :param col_name: the name of the column. example: 'currency'
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """
        heap_file = open("%s" % self.m_myFileName, "r+")
        helper_file = open("helper_file_%s" % self.m_myFileName, "w+")
        columnIndex = getColumnIndex(col_name)
        with heap_file:
            for line in heap_file:
                splitedLine = line.split(",")
                newLine = line
                if old_value in splitedLine[columnIndex]:
                    splitedLine[columnIndex] = new_value
                    newLine = ",".join(str(x) for x in splitedLine)
                    if columnIndex + 1 == splitedLine.__len__():
                        newLine += "\n"
                helper_file.write(newLine)
            heap_file.close()
            helper_file.seek(0)
            heap_file = open("%s" % self.m_myFileName, "w+")
            with heap_file:
                for line in helper_file:
                    heap_file.write(line)
            helper_file.close()


heap = Heap('kiva.txt')
heap.create('kiva_loans.txt')
#heap.insert('653207,1500.0,USD,Agriculture')
# heap.delete('currency', 'PKR')
# heap.delete('currency','NIS')
#heap.update('sector', 'Food', 'Mons')


# heap = Heap('heap.txt')
# heap.create('kiva.txt')
# heap.insert('653207,1500.0,USD,Agriculture')
# heap.update('currency','PKR','NIS')
# heap.delete('currency','NIS')

def insertionSort(m_index_file, sortedByColumnIndex, lineToInsert):
    helper_file = open("sort_helper_file.txt", "w+")
    index_file = open(m_index_file, "r")
    with helper_file:
        helper_file.write(index_file.readline())
        for line in index_file:
            if line.split(","[sortedByColumnIndex]) < lineToInsert.split(","[sortedByColumnIndex]):
                helper_file.write(line)
            else:
                helper_file.write(lineToInsert)
                helper_file.write(line)
                break
        for line in index_file:
            helper_file.write(line)
        index_file.close()
        index_file = open(m_index_file, "w+")
        for line in helper_file:
            index_file.write(line)
        helper_file.close()
        index_file.close()


class SortedFile:
    def __init__(self, file_name, col_name):
        """
        :param file_name: the name of the sorted file to create. example: kiva_sorted.txt
        :param col_name: the name of the column to sort by. example: 'lid'
        """
        self.m_myFileName = "%s_%s" % (col_name, file_name)
        self.m_sorted_by = col_name
        self.m_lastIndex = 0

    def create(self, source_file):
        """
        The function create sorted file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        my_file = open("%s" % self.m_myFileName, "w+")
        columnIndex = getColumnIndex(self.m_sorted_by)
        try:
            sourceFile = open("%s" % source_file, "r")
        except IOError:
            print "Could not open file!"
        with sourceFile:
            my_file.write(sourceFile.readline())
            my_file.close()
            lines = 0
            for line in sourceFile:
                if lines > 100:
                    break
                insertionSort(self.m_myFileName, columnIndex, line)
                # my_file.write("%s" % line)
                self.m_lastIndex += 1
                lines += 1
            my_file.close()
            sourceFile.close()


def insert(self, line):
    """
    The function insert new line to sorted file according to the value of col_name.
    :param line: string of row separated by comma. example: '653207,1500.0,USD,Agriculture'
    """


def delete(self, value):
    """
    The function delete records from sorted file where their value in col_name is value.
    Deletion done by mark # in the head of line.
    :param value: example: 'PKR'
    """


def update(self, old_value, new_value):
    """
    The function update records from the sorted file where their value in col_name is old_value to new_value.
    :param old_value: example: 'TZS'
    :param new_value: example: 'NIS'
    """


@classmethod
def insertHelper(cls, fileName, line, index):
    my_index_file = open("index_file_%s" % fileName, "r+")
    helper_file = open("helper_file_%s" % fileName, "w+")
    with helper_file:
        my_index_file.seek(index)
        for line in my_index_file:
            helper_file.write(line)
        my_index_file.seek(index)
        my_index_file.write(line)
        for line in helper_file:
            my_index_file.write(line)


def writeToASortedIndexFile(cls, fileName, keyParam, originalIndex):
    index = 0
    with fileName:
        for line in fileName:
            if index != 0:
                if keyParam > line.split(",", 0):
                    index += 1
                    continue
                else:
                    lineToInsert = "%s,%s" % (keyParam, originalIndex)
                    SortedFile.insertHelper(fileName, lineToInsert, index)
                    break
        fileName.close()


sf = SortedFile('SortedFile.txt', 'lid')
sf.create('kiva_loans.txt')


# sf = SortedFile('SortedFile.txt', 'currency')
# sf.create('kiva.txt')
# sf.insert('653207,2.0,USD,Agriculture')
# sf.delete('625.0')
# sf.update('150.0','12')

class Hash:
    def __init__(self, file_name, N=5):
        """
        :param file_name: the name of the hash file to create. example: kiva_hash.txt
        :param N: number of buckets/slots.
        """

    def create(self, source_file, col_name):
        """
        :param source_file: name of file to create from. example: kiva.txt
        :param col_name: the name of the column to index by example: 'lid'
        Every row will represent a bucket, every tuple <value|ptr> will separates by comma.
        Example for the first 20 instances in 'kiva.txt' and N=10:
        653060|11,
        653091|17,653051|1,
        653052|18,653062|14,653082|9,
        653063|4,653053|2,
        653054|16,653084|5,
        653075|15,
        653066|19,
        653067|7,
        653088|12,653048|10,653078|8,1080148|6,653068|3,
        653089|13,
        """

    def add(self, value, ptr):
        """
        The function insert <value|ptr> to hash table according to the result of the hash function on value.
        :param value: the value of col_name of the new instance.
        :param ptr: the row number of the new instance in the heap file.
        """

    def remove(self, value, ptr):
        """
        The function delete <value|ptr> from hash table.
        :param value: the value of col_name.
        :param ptr: the row number of the instance in the heap file.
        """

# heap = Heap("heap_for_hash.txt")
# hash = Hash('hash_file.txt', 10)

# heap.create('kiva.txt')
# hash.create('kiva.txt', 'lid')

# heap.insert('653207,1500.0,USD,Agriculture')
# hash.add('653207','11')
