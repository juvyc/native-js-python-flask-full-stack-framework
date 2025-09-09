/**
@path "/_m_", any path
*/

paths['/_m_'] = async (t) => {
    var _cont = await _utl.getTmplt('_m_.html');
    await _utl.html(t, _cont);
}