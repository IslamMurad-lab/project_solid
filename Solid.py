from abc import ABC,abstractclassmethod

class File_Manager(ABC):
    @abstractclassmethod
    def Read(self):
        pass
    
    @abstractclassmethod
    def Write(self,data):
        pass
    
class Zip_Manager(ABC):
    @abstractclassmethod
    def Compress(self):
        pass
    
    
    @abstractclassmethod
    def Decompress(self):
        pass
    
class LocalFileManager(File_Manager):
    def Read(self):
        print("Reading file locally")

    def Write(self, data):
        print(f"Writing data locally: {data}")

class LocalZipManager(Zip_Manager):
    def Compress(self):
        print("Compressing file locally")

    def Decompress(self):
        print("Decompressing file locally")
