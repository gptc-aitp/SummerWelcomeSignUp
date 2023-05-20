class Response:
    def __init__( self ):
        self.response = None
    def get( self ):
        return self.response
    def set( self, response ):
        self.response = response
    def format( self, firstName:str, lastName:str, emailAddress:str, selections:dict ):
        try:
            joinedSelections = ", ".join( selections[ 'aitp programming' ] )
            formatted = f"{ firstName }|{lastName }|{ emailAddress }|{ joinedSelections }"
            self.set( formatted )
        except Exception:
            print( "an exception has occured" )