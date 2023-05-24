#!/bin/env/python3
""" 
    @module Email.py 
    @author jack l.
    @date 2023 05 22
    @purpose module describes a model for an Email.
"""
import re
class Email:
    _emailsAdded = 0
    """ constructor """
    def __init__( self ):
        self.emailAddress = None
    def getEmailAddress( self ):
        """
            @method getEmailAddress
            @purpose getter. returns the instance variable, emailAddress
            @return string
        """
        return self.emailAddress
    def setEmailAddress( self, emailAddress ):
        """
            @method setEmailAddress
            @param emailAddress:string
            @purpose setter. sets the instance variable to a string.
            @return void
        """
        self.emailAddress = emailAddress
    def inputEmailAddress( self ):
        """
            @method inputEmailAddress
            @purpose triggers input loop for email address entry.
            @return void
        """
        try:
            validEmail = False
            emailPattern = re.compile( r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@student\.gptc\.edu" )
            while validEmail is False:
                emailAddress = str( input( "> gptc email: ") )
                if emailAddress.upper() == "QUIT":
                    break
                if self.emailIsValid( emailAddress, emailPattern ) != False:
                    self.setEmailAddress( emailAddress )
                    self._emailsAdded += 1
                    validEmail = True
                    break
        except Exception:
            print( "an exception has occured." )

    def emailIsValid( self, emailAddress, emailPattern ):
        """
            @method emailIsValid
            @param emailAddress:string
            @param emailPattern:string
            @purpose validates the entered email address.
            @return true | false
        """
        try:
            indexAtSymbol = emailAddress.index("@")
            gptcDomain = "@student.gptc.edu"
            if re.fullmatch( emailPattern, emailAddress ):
                return True
            else:
                print( "!!invalid email" )
                if emailAddress[indexAtSymbol+1::] != "student.gptc.edu":
                    print( "email does not contain 'student.gptc.edu'" )
                    return False
        except:
            print( "an exception has occured." )
    def view(self):
        """
            @method view
            @purpose prints the current email address to the screen.
            @return void
        """
        if self.emailAddress != None:
            print( f"email: { self.emailAddress }" )
        else:
            print("an email has not been inputted yet.")
            self.inputEmailAddress()