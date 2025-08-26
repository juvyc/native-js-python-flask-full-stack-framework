/**
@path "/", login path
*/

paths['/login'] = async (t) => {
    new baseSecurity('/').notsecure(async ()=>{
        var _cont = await _utl.getTmplt('user/login.html');
        await _utl.html(t, _cont); 
    });
}