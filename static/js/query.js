var dirname // Global Variable(정원찡's Good idea ㅎㅎ)

$('#editModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var id = button.data('id')
    var modal = $(this)
    modal.find('.modal-body #keyword').val(button.data('keyword'))
    modal.find('.modal-body #urls').val(button.data('urls'))
    modal.find('.modal-body #memo').val(button.data('memo'))
    modal.find('.modal-body #tag').val(button.data('tag').replace(/\,/g, '#'))
    modal.find('.modal-body #tag').val(button.data('memo'))
    modal.find('.modal-body form').attr('action', '/edit_memo/' + id + '/')
    $('#confirmEdit').click(function(event){
        modal.find('.modal-body form').submit()
    });
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
    $('.modal-key').html(button.data('keyword'))
    $('.modal-urls').html(button.data('urls'))
    $('.modal-memo').html(button.data('memo'))
    $('.modal-tag').html(button.data('tag').replace(/\,/g, '#'))
});

function setDirname(name){
    dirname = name
}
