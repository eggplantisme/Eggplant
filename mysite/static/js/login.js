$(document).ready(function () {
    $('#id_username').focus()
    $('#id_username').blur()
    $('#id_password').focus()
    $('#id_password').blur()
})
$('#id_username').blur(function () {
    pass_reg = /\S{6,}/
    if ($('#id_username').val() == '') {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("请输入用户名")
        $('#submit').attr('disabled', 'disabled')
    }
    else if ($('#id_password').val() == '') {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("请输入密码")
        $('#submit').attr('disabled', 'disabled')
    }
    else if (!pass_reg.test($('#id_password').val())) {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("密码至少为6位非空白字符")
        $('#submit').attr('disabled', 'disabled')
    } else {
        $('#msg').attr('class', 'text-success')
        $('#msg').text("")
        $('#submit').removeAttr('disabled')
    }
})
$('#id_password').blur(function () {
    pass_reg = /\S{6,}/
    if ($('#id_password').val() == '') {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("请输入密码")
        $('#submit').attr('disabled', 'disabled')
    } else if (!pass_reg.test($('#id_password').val())) {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("密码至少为6位非空白字符")
        $('#submit').attr('disabled', 'disabled')
    } else if ($('#id_username').val() == '') {
        $('#msg').attr('class', 'text-danger')
        $('#msg').text("请输入用户名")
        $('#submit').attr('disabled', 'disabled')
    } else {
        $('#msg').attr('class', 'text-success')
        $('#msg').text("")
        $('#submit').removeAttr('disabled')
    }
})
//$('#id_password').blur()