from os import remove
from abc import ABC, abstractmethod

class FileOperations(ABC):
    def file_open(self, filename):
        self.filename = filename
        self.file = open(file=filename, mode='w+')
        return self.file

    @abstractmethod
    def add_data(self):
        pass # template method

    def read_file(self):
        self.file.seek(0)
        return self.file.readline()    

    def file_close(self) -> None:
        self.file.close()
        remove(self.filename)


class TextFileOperations(FileOperations):
    def add_data(self, data) -> None:
        self.file.write(data)
        

text_file = TextFileOperations()
text_file.file_open('Sample.txt')    
text_file.add_data('Sample add data')

print(text_file.read_file())
text_file.file_close()
