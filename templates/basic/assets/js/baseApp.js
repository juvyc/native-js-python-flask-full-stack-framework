const paths = {};
var baseWrp = "";

class baseApp
{
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
            }else{
                t.innerHTML = '404 Not Found!';
            }
        }
    }
}

//Watch the back and forth browser button
window.addEventListener("popstate", (e) => {
    if(e.state){
        var _path = window.location.pathname;
        console.log(_path);
        _path = _path.split('?')[0];
        _utl.goto(_path);
    }
});