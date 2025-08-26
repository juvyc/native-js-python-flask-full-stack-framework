class baseSecurity
{
    constructor(redirectTo)
    {
        this._redirectTo = redirectTo;
    }

    //Display template if secure
    async secure(fnc)
    {
        const isauth = await this.isAuthorized();

        if(!isauth){
            _utl.goto(this._redirectTo);
        }else{
            fnc();
        }
    }

    //Display template if not secure
    async notsecure(fnc)
    {
        const isauth = await this.isAuthorized();
        if(isauth){
            _utl.goto(this._redirectTo);
        }else{
            fnc();
        }
    }

    //Check if authorized
    async isAuthorized()
    {
        const checkauth = await fetch('/auth/check', {
            method: "POST"
        });

        const rs = await checkauth.json();
        return rs.status;
    }

    //set Authorization
    setAuthorization()
    {

    }
}