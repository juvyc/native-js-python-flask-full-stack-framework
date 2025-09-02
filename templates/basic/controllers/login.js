/**
@path "/login", login path
*/

paths['/login'] = async (t) => {
    await new baseSecurity('/').notsecure(async ()=>{
        var _cont = await _utl.getTmplt('user/login.html');
        await _utl.html(t, _cont); 

        //Now fetch data from server
        await _utl.fetch_data('/?ft=login/login');
    });
}