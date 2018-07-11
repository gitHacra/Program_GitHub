// 获取选择的内容
var selectText = function() {
    traStr = window.getSelection().toString();
    var reg1 = new RegExp("[\\u4E00-\\u9FFF]+","g");
    var reg2 = new RegExp("[a-zA-Z]+");
　　if (!reg1.test(traStr) && reg2.test(traStr)) {
        showIcon();
    } 
} 

// 鼠标选择的内容位置
var getPosition = function() {
    var e = event || window.event;
    var scrollX = document.documentElement.scrollLeft || document.body.scrollLeft;
    var scrollY = document.documentElement.scrollTop || document.body.scrollTop;
    x = (e.pageX || e.clientX + scrollX) + 10;
    y = (e.pageY || e.clientY + scrollY) + 15;
}

// 显示翻译图标
var showIcon = function() {
    // 如果已经显示图标，则不必再显示
    var img = document.getElementById("translationImg");
    if (img) return;
    // 获取鼠标选词位置
    getPosition();
    // 创建翻译图标
    var img = document.createElement("img");
    img.id = "translationImg";
    img.src = "https://raw.githubusercontent.com/gitHacra/Gadget/master/translation/code/search.png";
    img.style.width = "25px";
    img.style.height = "24px";
    img.style.position='absolute';
    img.style.left = x + "px";
    img.style.top = y + "px";
    document.body.appendChild(img);
    // 进行翻译，并显示翻译界面
    img.onclick = function() {
        translationAPI();
        document.body.removeChild(img);
        var tra = document.getElementById('translationDiv');
        tra.style.display = "";
        tra.style.position = "absolute";
        tra.style.left = x + "px";
        tra.style.top = y + "px";
        window.getSelection().removeAllRanges();
    }
    // 图标延时关闭
    setTimeout(function() {
        var img = document.getElementById("translationImg");
        if (img) {   
            document.body.removeChild(img);
        }
    }, 2300);
}

// 翻译界面
var addElement = function() {
    // 翻译界面
    var tra = document.createElement('div');
    tra.id = "translationDiv";
    tra.style.display = "none";
    tra.style.width = "265px";
    tra.style.fontSize = "12px";
    tra.innerHTML = "<style type='text/css'> .div1 { height: 24px; color: #FFFFFF; cursor: move; padding-left: 5px; line-height: 25px; border: 1px solid #6896DC; border-radius: 2px 2px 0 0; background-color: #4DA2FD; } .div11 { width: 26px; float: right; cursor: pointer; text-align: center; } .div2 { color: #333333; padding: 18px 10px 0 10px; border-radius: 0 0 2px 2px; border-left: 1px solid #D2CCC3; border-right: 1px solid #D2CCC3; border-bottom: 1px solid #D2CCC3; background-color: #FFFFFF; } .div21 { width: 55px; color: #75A7F6; cursor: pointer; margin-top: 10px; margin-left: 190px; margin-bottom: 10px; text-align: center; } </style> <div id='traTitleDiv' class='div1'> <span>网页翻译</span> <div id='traCloseDiv' class='div11' title='关闭'>X</div> </div> <div class='div2'> <div id='traSrc' style='display: none'></div> <div id='traDst'></div> <div style='height:1px; margin-top:17px; background-color:#EFEFEF'></div> <div> <div id='traMoreDiv' class='div21'>查看更多</div> </div> </div>";
    document.body.appendChild(tra);
    // 界面拖动
    tra.onmousedown = function(ev) {
        var oevent = ev || event;
        var distanceX = oevent.clientX - tra.offsetLeft;
        var distanceY = oevent.clientY - tra.offsetTop;
        document.onmousemove = function(ev){
            var oevent = ev || event;
            tra.style.left = oevent.clientX - distanceX + 'px';
            tra.style.top = oevent.clientY - distanceY + 'px'; 
　　　　}
        document.onmouseup = function(){
            document.onmousemove = null;
            document.onmouseup = null;
　　　　}
    }
    // 关闭事件
    var traClose = document.getElementById('traCloseDiv');
    traClose.onclick = function() {
        tra.style.display = 'none';
        document.getElementById('traDst').innerHTML = '';
    }
    // 查看更多
    var traMore = document.getElementById('traMoreDiv');
    traMore.onclick = function() {
        var url = 'http://fanyi.baidu.com/translate#en/zh/' + document.getElementById('traSrc').innerText;
        window.open(url);
    }
}

var traStr = '';
var x = 0, y = 0;
addElement();
document.addEventListener("mouseup", selectText, true);
