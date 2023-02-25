class IO:
    @staticmethod
    def saveToFile(answer, name):
        with open(f"../test/{name}.txt", "w") as file:
            file.write(answer)
            file.close()