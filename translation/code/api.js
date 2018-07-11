var translationAPI = function() {
    var appid = '20180207000121543';
    var key = '3p7lIfgoQ0nngy3d0VTs';
    var salt = (new Date).getTime();
    var query = traStr;
    var from = 'en';
    var to = 'zh';
    var str1 = appid + query + salt +key;
    var sign = MD5(str1);
    $.ajax({
        url: 'https://fanyi-api.baidu.com/api/trans/vip/translate',
        type: 'get',
        dataType: 'json',
        data: {
            q: query,
            from: from,
            to: to,
            appid: appid,
            salt: salt,
            sign: sign
        },
        success: function (data) {
            console.log(data);
            var src = data.trans_result[0]['src'];
            $('#traSrc').text(src);
            $('#traDst').text(src + ': ' + data.trans_result[0]['dst']);
        } 
    });
}
