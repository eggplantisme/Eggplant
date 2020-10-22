$(function() {
    var body_parent = $("#id_body").parent();
    var body_val = $("#id_body").val();
    var body = "<div id='bodycotent'></div>";
    body_parent.append(body);
    testEditor = editormd("bodycotent", {
        value   : body_val,
        path    : "/static/editor.md/lib/",
        syncScrolling : "single",
        width: "90%",
        height: "90%"
    });
    $("")

});

