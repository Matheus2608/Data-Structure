class BinaryHeap:
  def __init__(self):
      self._heap = []
      
  def _perc_up(self, cur_idx):
    while (cur_idx - 1) // 2 >= 0:
        parent_idx = (cur_idx - 1) // 2
        if self._heap[cur_idx] < self._heap[parent_idx]:
            self._heap[cur_idx], self._heap[parent_idx] = (
                self._heap[parent_idx],
                self._heap[cur_idx],
            )
        cur_idx = parent_idx
        
  def insert(self, item):
    self._heap.append(item)
    self._perc_up(len(self._heap) - 1)
  def _perc_down(self, cur_idx):
    while 2 * cur_idx + 1 < len(self._heap):
        min_child_idx = self._get_min_child(cur_idx)
        if self._heap[cur_idx] > self._heap[min_child_idx]:
            self._heap[cur_idx], self._heap[min_child_idx] = (
                self._heap[min_child_idx],
                self._heap[cur_idx],
            )
        else:
            return
        cur_idx = min_child_idx

  def _get_min_child(self, parent_idx):
      if 2 * parent_idx + 2 > len(self._heap) - 1:
          return 2 * parent_idx + 1
      if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
          return 2 * parent_idx + 1
      return 2 * parent_idx + 2
