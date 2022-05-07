class BinaryHeap:
    def __init__(self):
        self.heap = []

    def perc_up(self, cur_idx):
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self.heap[cur_idx] < self.heap[parent_idx]:
                self.heap[cur_idx], self.heap[parent_idx] = (
                    self.heap[parent_idx],
                    self.heap[cur_idx],
                )
            cur_idx = parent_idx

    def insert(self, item):
        self.heap.append(item)
        self.perc_up(len(self._heap) - 1)

    def perc_down(self, cur_idx):
        while 2 * cur_idx + 1 < len(self.heap):
            min_child_idx = self.get_min_child(cur_idx)
            if self.heap[cur_idx] > self.heap[min_child_idx]:
                self.heap[cur_idx], self.heap[min_child_idx] = (
                    self.heap[min_child_idx],
                    self.heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    def get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self.heap) - 1:
            return 2 * parent_idx + 1
        if self.heap[2 * parent_idx + 1] < self.heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def deleteMin(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        result = self.heap.pop()
        self.perc_down(0)
        return result

    def heapify(self, alist):
        i = len(alist) // 2
        self.heap = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def __str__(self):
        ordered_list = []
        for _ in range(len(self.heap)):
            ordered_list.append(self.deleteMin())
        return f"Heap = {self.heap}; Ordered List: {ordered_list}"


b = BinaryHeap()
b.heapify([2, 4, 56, 7, 3, 1, 34, 5, 7, 8, 9, 5, 3, 21])
print(b)
