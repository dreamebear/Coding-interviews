class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # hmap ={val: count}
        self.hmap = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.hmap[number] = self.hmap.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        # print self.hmap
        for val, count in self.hmap.items():
            diff = value - val
            # first check if in this map
            if diff in self.hmap:
                # two different value pair
                if diff != val:
                    return True

                # two same numbers pair
                else:
                    if count >= 2:
                        return True

        return False




        # duplicates?

        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)