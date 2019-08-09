var selected="" ;
var delcontext='폴더 삭제시 해당 폴더의 메모들도 함께 삭제됩니다.\n정말 삭제 하시겠습니까?';

var app = new Vue({
    el: '#app',
    delimiters: ['{', '}'],
    data: {
        message: 'test app',
        newMessage: '',
    },
    created: function () {
        console.log("created");
    },
    mounted: function() {
        console.log("mounted");
        if(localStorage.getItem('temp') == null) localStorage.getItem('temp') = ''
        document.getElementById("review_text").defaultValue = localStorage.getItem('temp');
    },
    updated: function() {
        console.log("upadated");
    },
    methods: {
        renew: function(){
            if(this.newMessage == '') this.newMessage = localStorage.getItem('temp');
            localStorage.setItem('temp', this.newMessage);
        }
    },
})