var dirname // Global Variable(정원찡's Good idea ㅎㅎ)

$('#editModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var id = button.data('id')
    var keyword = button.data('keyword')
    var urls = button.data('urls')

    var modal = $(this)

    modal.find('.modal-title').text('편집하기')
    modal.find('.modal-body input').val(keyword)
    modal.find('.modal-body textarea').val(urls)

    $('.modal-complete').click(function(){

        console.log($("#keyword").val())
        console.log($("#urls").val())

        splited_urls = $("#urls").val().split('\n')

        modal.find('.modal-footer a').attr('href', '/edit_memo/' + id + '/' + $("#keyword").val() +'/' + splited_urls)
    })
})

$('#moveModal').on('show.bs.modal', function (event) {

    var button = $(event.relatedTarget)
    var id = button.data('id')
    var modal = $(this)

    $('.recently-clicked').click(function(){

        var recently = document.getElementById("recently").name
        modal.find('.modal-body a').attr('href', '/movedir/' + id + '/' + 'recently')
    })

    $('.dirname-clicked').click(function(){

        modal.find('.modal-body a').attr('href', '/movedir/' + id + '/' + dirname)
    })

})


$('#editdirname').on('show.bs.modal', function (event) {

var button = $(event.relatedTarget)
var id = button.data('id')
var modal = $(this)

$('#editnametxt').change(function(){
    modal.find('.modal-body form').attr('action', '/changedirname/' + id)
})

})

$('#moreModal').on('show.bs.modal', function(event) {
    var button = $(event.relatedTarget)
    var key = button.data('keyword')
    var urls = button.data('urls')
    var lines = urls.split("\n")
    console.log(key)
    console.log(urls)
    $('.modal-key').html(key)
    $('.modal-urls').html(urls)
});

function setDirname(name){
    dirname = name
}