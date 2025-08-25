/**
@path "/", admin dashboard path
*/

paths['/admin'] = async (t) => {

    var _cont = await _utl.getTmplt('admin/dashboard.html');
    //await _utl.el_append(t, _cont);
    
    await _utl.html(t, _cont);
}