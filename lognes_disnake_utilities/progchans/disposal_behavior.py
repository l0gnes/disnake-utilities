from enum import Enum

class DisposalBehaviour(Enum):

    # Does nothing when the time comes to dispose of the channel
    # This is the default because idk
    NONE        = 0
    
    # Tries to delete the channel when it gets put into the disposal queue
    DESTROY     = 1
    
    # Tries to remove all permissions when time comes to close the channel
    DEPERMIT    = 2