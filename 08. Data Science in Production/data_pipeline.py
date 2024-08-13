import pandas as pd
import luigi

class Print(luigi.Task):
    def run(self):
        # print("Hello World!")
        with self.output().open("w") as file:
            file.write("Hello World!")
    
    def requires(self):
        pass
    
    def output(self):
        return luigi.LocalTarget("hello.txt")
    

class Read(luigi.Task):
    def requires(self):
        return Print()
    
    def run(self):
        with self.input().open("r") as file:
            file_content = file.read()
            print(file_content)

        with self.output().open("w") as file:
            file.write("Hello World - modified!")

    def output(self):
        return luigi.LocalTarget("hello-mod.txt")
    

# class Modify(luigi.Task):
#     number = luigi.Parameter(5)