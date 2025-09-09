const paths = {};
var baseWrp = "";

class baseApp{
    constructor(_target){
        this._target = _target;
        baseWrp = _target;
        this.init();
        this.renderer(this.elem_target);
    }

    init(){
        const _target = document.querySelector(this._target);
        this.elem_target = _target;
    }

    async renderer(t){
        if(t){
            if(typeof paths[currentEndPoint] != 'undefined'){
                await paths[currentEndPoint](t);
            }else if(typeof paths['/_m_'] != 'undefined'){
                await paths['/_m_'](t);
            }else{
                t.innerHTML = '404 Not Found!';
            }

            this.preLinks(t);
        }
    }

    //Use this to prepare all links in the document
    preLinks(t){
        if(!t) return false;
        //Get all non reloadable links and use the goto function
        t.querySelectorAll('a:not([reload])').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                _utl.goto(e.target);
            });
        });
    }
}

//Watch the back and forth browser button
window.addEventListener("popstate", (e) => {
    var _path = window.location.pathname;
    var _turi = _path.split('?')[0];
    currentEndPoint = _turi;
    new baseApp(baseWrp);
});