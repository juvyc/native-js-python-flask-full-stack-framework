/**
@path "/admin", admin dashboard path
*/

paths['/admin'] = async (t) => {
    await new baseSecurity('/login').secure(async ()=>{
        var _cont = await _utl.getTmplt('admin/dashboard.html');
        await _utl.html(t, _cont);
    });
}