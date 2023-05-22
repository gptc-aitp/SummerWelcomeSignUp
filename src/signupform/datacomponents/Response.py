#!/bin/env/python3
""" 
    @module Response.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes model for a Response.
"""
class Response:
    def __init__( self ):
        self.response = None
    def get( self ):
        """ 
            @method get
            @purpose getter. returns instance variable, response.
            @return string
        """
        return self.response
    def set( self, response ):
        """ 
            @method set
            @purpose rsetter. returns instance variable, response.
            @return string
        """
        self.response = response
    def format( self, firstName:str, lastName:str, emailAddress:str, selections:dict ):
        """ 
            @method format
            @param firstName:string
            @lastName:string
            @emailAddress:string
            @selections:list
            @purpose formats the response string.
            @return void
        """
        try:
            joinedSelections = ", ".join( selections[ 'aitp programming' ] )
            formatted = f"{ firstName }|{lastName }|{ emailAddress }|{ joinedSelections }"
            self.set( formatted )
        except Exception:
            print( "an exception has occured." )