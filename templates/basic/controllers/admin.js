/**
@path "/admin/dashboard", admin dashboard path
*/

paths['/admin/dashboard'] = async (t) => {

    const checkauth = await fetch('/admin/dashboard', {
        method: "PATCH"
    });

    const rs = await checkauth.json();

    if(typeof rs.status != 'undefined' && rs.status){
        var _cont = await _utl.getTmplt('admin/dashboard.html');
        await _utl.html(t, _cont);
    }else{
        _utl.goto('/login');
    }
}