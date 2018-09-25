from statistics import median
from array import array


class Array:
    '''
    This is a single-dimensional numeric array for scientific computing.

    This array will compute lots of basic statics

    Parameters
    ----------
    data: list
        List of numbers
    '''

    def __init__(self, data):
        # Allow a user to pass only an array or a list
        if isinstance(data, array):
            self.data = data
        elif isinstance(data, list):
            if len(data) == 0:
                # hack - forcinng array to be a float
                first_item = 0.0
            else:
                first_item = data[0]
            first_item = data[0]
            if isinstance(first_item, bool):
                dtype = 'b'
            elif isinstance(first_item, int):
                dtype = 'q'
            elif isinstance(first_item, float):
                dtype = 'd'
            else:
                raise TypeError('List must only contain bool, '
                                'intsm or floats')
            try:
                self.data = array(dtype, data)
            except TypeError:
                self.data = array('d', data)
        else:
            raise TypeError('Array constructor only accepts lists or arrays')
        # b - boolean (1 byte integer)
        # q - integer (4 bytes)
        # d - float (8 bytes)
        self.dtype = self.data.typecode
        self.data = array('d', data)

    def sum(self):
        '''
        Sums all the valuses in the array

        Returns
        -------
        int or float
        '''
        return sum(self.data)

    def min(self):
        '''
        Returns the smallest value in the array

        Returns
        -------
        int or float
        '''
        return min(self.data)

    def max(self):
        '''
        Returns the highest value in the array

        Returns
        -------
        int or float

        '''
        return max(self.data)

    def median(self):
        '''
        Returns the median value in the array

        Returns
        -------
        int or float
        '''
        return median(self.data)

    def mean(self):
        '''
        Returns the mean value in the array

        Returns
        -------
        int or float
        '''
        return self.sum() / len(self.data)
