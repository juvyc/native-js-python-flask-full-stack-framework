/**
@path "/", home path
*/

paths['/'] = async (t) => {

    var _cont = await _utl.getTmplt('home.html');
    await _utl.html(t, _cont);

    //Now fetch data from server
    await _utl.fetch_data('/');
}