/**
@path "/page", page path
*/

paths['/page'] = async (t) => {
    await new baseSecurity('/').notsecure(async ()=>{
        var _cont = await _utl.getTmplt('page.html');
        await _utl.html(t, _cont); 

        //Now fetch data from server
        //await _utl.fetch_data('/page');
    });
}