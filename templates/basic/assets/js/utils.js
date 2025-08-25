const _utl = {
    /**
    @param t, for target parent element
    @param cont, is the element in text type
    @param p, is for the position
    */
    el_append : (t, cont, p) =>{
        t.insertAdjacentHTML((p ? p : 'beforeend'), cont);
        var scrpts = t.querySelectorAll('script');
        if(scrpts.length){
            scrpts.forEach((s)=>{
                var sc = _utl.c_el('script');
                sc.innerHTML = s.innerHTML;
                s.after(sc);
                s.remove();
            });
        }
    },

    //Replace content of a container
    html : (t, cont) =>{
        t.innerHTML = cont;
        var scrpts = t.querySelectorAll('script');
        if(scrpts.length){
            scrpts.forEach((s)=>{
                var sc = _utl.c_el('script');
                sc.innerHTML = s.innerHTML;
                s.after(sc);
                s.remove();
            });
        }
    },

    el : (_tid) => {
        return document.querySelector(_tid);
    },

    //Create element
    c_el : (t) => {
        var _cel = document.createElement(t);
        return _cel;
    },

    //Get template content
    getTmplt : (tmptn) => {
        var _c = document.querySelector('[data-name="'+ tmptn +'"]');
        if(_c) return _c.innerHTML;
        else return false;
    },

    //Navigate to other page
    goto : (url) => {
        var _turi = url;
        if(typeof url != "string")
            _turi = url.getAttribute('href');

        window.history.pushState({"html":_turi}, "", _turi);

        currentEndPoint = _turi;

        new baseApp(baseWrp);

        return false;
    }
};