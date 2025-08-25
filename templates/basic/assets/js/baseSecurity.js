class baseSecurity
{
    constructor(redirectTo)
    {
        this._redirectTo = redirectTo;
    }

    secure(fnc)
    {
        if(!this.isAuthorized()){
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