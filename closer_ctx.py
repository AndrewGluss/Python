class Closer:

    def __init__(self, obj):
        self.obj = obj
        self.closed = True

    def __enter__(self):
        self.closed = False
        return self.obj


    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except Exception as e:
            print("Незакрываемый объект")


with Closer(5) as i:
    i += 1

print(i)