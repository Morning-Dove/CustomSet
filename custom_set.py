class CustomSet:

    def __init__(self):
        self.list = []

    def add(self, item):
        if item not in self.list:
            self.list.append(item)
        else:
            return "Can not add to list"
    
    def remove(self, item):
        if item in self.list:
            self.list.remove(item)
        else:
            raise KeyError
    
    def as_list(self):
        return self.list

    def clear(self): 
        for item in self.list:
            self.list.remove(item)


def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list())
    
    my_set.remove("item 2")
    print(my_set.as_list())

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list())
        









if __name__ == "__main__":
    main()
