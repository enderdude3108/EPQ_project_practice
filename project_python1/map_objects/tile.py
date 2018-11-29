

class Tile:
    #A tile

    def __init__(self,blocked,block_sight=None):
        self.blocked=blocked

        #by deafualt sight is blocked
        if block_sight is None:
            block_sight=blocked
            
        self.block_sight=block_sight
