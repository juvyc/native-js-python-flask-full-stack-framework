class baseSecurity
{
    constructor(redirectTo)
    {
        this._redirectTo = redirectTo;
    }

    //Display template if secure
    secure(fnc)
    {
        if(!this.isAuthorized()){
            _utl.goto(this._redirectTo);
        }else{
            fnc();
        }
    }

    //Display template if not secure
    notsecure(fnc)
    {
        if(this.isAuthorized()){
            _utl.goto(this._redirectTo);
        }else{
            fnc();
        }
    }

    //Check if authorized
    isAuthorized()
    {
        return false;
    }

    //set Authorization
    setAuthorization()
    {

    }
}