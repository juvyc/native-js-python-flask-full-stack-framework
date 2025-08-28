/**
@path "/", home path
*/

paths['/'] = async (t) => {

    var _cont = await _utl.getTmplt('home.html');
    //await _utl.el_append(t, _cont);
    
    await _utl.html(t, _cont);

    //Now fetch data from server
    await _utl.fetch_data('/?ft=home');

    var tst = _utl.el('.test');
    if(tst){
        tst.style.color = 'red';
    }
}