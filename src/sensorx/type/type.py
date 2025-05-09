class Type:
    def __init__(self, val_dims:tuple , frequency:float):
        '''
        :param val_dims:
        :param frequency: Average frequency
        '''
        self._val_dims = val_dims
        self._frequency = frequency