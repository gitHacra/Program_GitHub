var count = 50                            // 圆的数量
var length = 0.6                          // 移动距离
var canvas = null                         // 画布
var circles = []                          // 圆的属性
//var color = ['#F9F1B5', '#FD9C9C']      // 圆的颜色
var color = ['rgba(249, 241, 181, 0.6)', 'rgba(253, 156, 156, 0.6)']        // 圆的颜色
var run = null                            // 鼠标长按

/**
 * 初始化数据
 */
function initData() {
    // 获取对应的Canvas，并设置宽高
    canvas = document.getElementById('myCanvas')        
    canvas.width = Math.max(document.body.clientWidth, document.body.scrollWidth)
    canvas.height = Math.max(document.body.clientHeight, document.body.scrollHeight)
    // 产生count个随机圆
    for (var i = 0; i < count; i++) {
        var circle = new Array(5)                               // x,y,radius,angle
        circle[0] = Math.random() * 0.99 + 0.01                 // x:百分比[0.01, 0.99]
        circle[1] = Math.random() * 0.99 + 0.01                 // y:百分比[0.01, 0.99]
        circle[2] = Math.floor(Math.random() * 26 + 25)         // r:圆半径[25, 50]
        circle[3] = Math.floor(Math.random() * 361)             // a:圆角度[0, 360]
        circle[4] = color[0]
        circles.push(circle)
    }
}

/**
 * 创建动画
 */
function createAnimation() {
    drawCircle()            // 绘制随机圆
    checkCircle()           // 检查随机圆的角度
    moveCircle()            // 移动随机圆的位置
    requestAnimFrame(createAnimation)
}

/**
 * 绘制随机圆
 */
function drawCircle() {
    var context = canvas.getContext('2d')
    context.clearRect(0, 0, canvas.width, canvas.height)
    for (var i = 0; i < count; i++) {
        context.fillStyle = circles[i][4]
        context.beginPath()
        context.arc(circles[i][0] * canvas.width, circles[i][1] * canvas.height, circles[i][2], 0, Math.PI * 2, true)
        context.fill()
    }
}

/**
 * 检查随机圆的角度
 */
function checkCircle() {
    for (var i = 0; i < count; i++) {
        if (circles[i][0] <= 0 || circles[i][0] >= 1 || circles[i][1] <= 0 || circles[i][1] >= 1){
            circles[i][3] = (circles[i][3] + 90) % 360
            circles[i][4] = circles[i][4] == color[0] ? color[1] : color[0]
        }
    }
}

/**
 * 移动随机圆的位置
 */
function moveCircle() {
    for (var i = 0; i < count; i++) {
        var angle = circles[i][3]
        if (angle <= 90) {
            circles[i][0] += length * Math.cos(angle) / canvas.width
            circles[i][1] -= length * Math.sin(angle) / canvas.height
        }
        else if (angle <= 180) {
            circles[i][0] -= length * Math.cos(180 - angle) / canvas.width
            circles[i][1] -= length * Math.sin(180 - angle) / canvas.height
        }
        else if (angle <= 270) {
            circles[i][0] -= length * Math.cos(angle - 180) / canvas.width
            circles[i][1] += length * Math.sin(angle - 180) / canvas.height
        }
        else if (angle <= 360) {
            circles[i][0] += length * Math.cos(360 - angle) / canvas.width
            circles[i][1] += length * Math.sin(360 - angle) / canvas.height
        }
    }
}

/**
 * 兼容所有浏览器
 */
requestAnimFrame = function(){
    return  window.requestAnimationFrame       ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame    ||
            function (callback){
                window.setTimeout(callback, 1000 / 60)
            }
}();

/**
 * 改变窗口时改变canvas的大小
 */
window.onresize = function() {
    canvas.width = Math.max(document.body.clientWidth, document.body.scrollWidth)
    canvas.height = Math.max(document.body.clientHeight, document.body.scrollHeight)
}

/**
 * 长按加速移动
 */
window.onmousedown = function() {
    run = this.setTimeout(function() {
        length = 6
    }, 700)
}

/**
 * 长按加速移动
 */
window.onmouseup = function() {
    clearTimeout(run)
    length = 0.6
}

initData()
createAnimation()