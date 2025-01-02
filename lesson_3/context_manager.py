class Savedfile:
    def __init__(self, path: str, mode='r'):
        self.name = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, type, value, tb):
        if self.file:
            self.file.close()
#           print(f'Exception {type}')
#           return True

if __name__ == '__main__':
    with Savedfile('some.txt', 'w') as f:
        f.write('hello')