class MyIterator:
    def __init__(self, data):
        """
        Initialize the iterator with the data collection and index.
        """
        self.data = data
        self.index = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next element from the data collection.
        """
        if self.index >= len(self.data):
            # Raise StopIteration when there are no more elements.
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_data = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_data)

# Iterate over the elements using the iterator
for item in my_iterator:
    print(item)


'''
# Output:
1
2
3
4
5
'''