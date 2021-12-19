from collections import namedtuple


Item = namedtuple('Item', 'value weight value_to_weight_ratio')
KnapsackSolution = namedtuple('KnapsackSolution', 'items value')
SearchState = namedtuple('SearchState', 'upper_bound lower_bound remaining_items packed_items weight_limit value')


def knapsack_solution(items):
    return KnapsackSolution(items, sum(item.value for item in items))


def item(value, weight):
    assert weight > 0
    return Item(value, weight, float(value)/weight)


class Items:
    def __init__(self, items, i=0):
        self._items = items
        self._i = i

    def empty(self):
        return self._i >= len(self._items)

    def first(self):
        return self._items[self._i]

    def rest(self):
        return Items(self._items, self._i + 1)

    def __iter__(self):
        return (self._items[i] for i in xrange(self._i, len(self._items)))

    def __len__(self):
        return 0 if self.empty() else (len(self._items) - self._i)


class Heap:
    # "heap property": a binary tree has the heap property established if
    # the root node has no descendants or is smaller than or equal to all
    # descendants and the left and right subtrees also have the heap property
    # established.

    # For all big-oh notations below, N = len(self._heap).

    def __init__(self, elements, key=lambda x: x):
        self._key = key
        self._heap = elements[:]  # heap property not necessarily established
        self._heapify()  # heap property established

    def __bool__(self):
        return len(self._heap) > 0

    def __repr__(self):
        return repr(self._heap)

    def push(self, element):
        # precondition: heap property exists
        self._heap.append(element)  # heap property possibly violated; O(1) time
        self._bubble_up()  # heap property restored; O(logN) time

    def pop(self):
        # precondition: heap property exists
        assert len(self._heap) > 0

        if len(self._heap) == 1:
            return self._heap.pop()  # heap property maintained; O(1) time
        else:
            head_element = self._heap[0]
            self._heap[0] = self._heap.pop()  # heap property possibly violated; O(1) time
            self._bubble_down(0)  # heap property restored; O(logN) time
            return head_element

    def _bubble_up(self):
        # O(logN) time
        assert len(self._heap) > 0

        parent_index = lambda i: (i + 1) // 2 - 1
        parent = lambda i: self._heap[parent_index(i)]
        parent_key = lambda i: self._key(parent(i))

        element_index = len(self._heap) - 1
        element = self._heap[element_index]
        element_key = self._key(element)

        while element_index != 0 and element_key < parent_key(element_index):
            self._heap[element_index] = parent(element_index)
            element_index = parent_index(element_index)

        self._heap[element_index] = element

    def _bubble_down(self, element_index):
        # O(logN) time
        # precondition: the left and right subtrees of element have the heap property
        assert 0 <= element_index < len(self._heap)

        element = self._heap[element_index]
        element_key = self._key(element)

        child_indices = lambda i: filter(lambda j: j < len(self._heap), (i * 2 + 1, i * 2 + 2))
        has_children = lambda i: len(child_indices(i)) > 0
        index_of_smaller_child = lambda i: min(child_indices(i), key=lambda j: self._key(self._heap[j]))
        smaller_child = lambda i: self._heap[index_of_smaller_child(i)]
        key_of_smaller_child = lambda i: self._key(smaller_child(i))

        while has_children(element_index) and element_key > key_of_smaller_child(element_index):
            self._heap[element_index] = smaller_child(element_index)
            element_index = index_of_smaller_child(element_index)

        self._heap[element_index] = element

    def _heapify(self):
        # O(N) time. Why? The analysis is subtle. See the following:
        # https://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        # Here's another interesting perspective to check out:
        # https://math.stackexchange.com/questions/181022/worst-case-analysis-of-max-heapify-procedure
        
        n = len(self._heap)
        indices_from_bottom_to_top = reversed(xrange(n))

        for i in indices_from_bottom_to_top:
            self._bubble_down(i)

        # Note: for simplicity, we iterate over the indices [n-1, n-2, ..., 1, 0].
        # However, there's no need to heapify any leaf node (e.g., node n-1) since they
        # all already have the heap property established. Therefore, we could introduce a
        # small optimization by setting setting n above to one plus the largest index for a
        # non-leaf node in self._heap. What is the largest index for a non-leaf node? The last
        # non-leaf node must be the parent of the very last element in the heap, which has an
        # index of n-1. The parent index of n-1 is (((n-1) + 1) // 2 - 1) = n // 2 - 1.
        # Therefore, we could get the optimization above by setting n = 1 + (n // 2 - 1) = n // 2,
        # in which case we would just iterate over [n//2 - 1, n//2 - 2, ..., 1, 0], saving some time.
        # Either way, the algorithm is correct and has the same asymptotic runtime.
