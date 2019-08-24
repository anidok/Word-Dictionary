class Utils:

    @staticmethod
    def words_from_file(file):
        return [word.decode('ascii') for line in file for word in line.split()]
