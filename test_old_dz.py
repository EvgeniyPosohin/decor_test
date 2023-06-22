from log_second import logger


class FlatIterator:

    def __init__(self, *args):
        self.suppl_list = []
        self.set_plain(args)
        self.counter = -1

    @logger('iter_it.log')
    def __iter__(self):
        return self

    @logger('iter_next.log')
    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.suppl_list):
            raise StopIteration
        return self.suppl_list[self.counter]

    @logger(('iter_plain.log'))
    def set_plain(self, list_of_list):
        for item in list_of_list:
            if type(item) is list:
                self.set_plain(item)
            else:
                self.suppl_list.append(item)


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    flatiter = FlatIterator(list_of_lists_1)
    for item in flatiter:
        pass
