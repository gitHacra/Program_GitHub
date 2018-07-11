var isPlay = false
var runPlay = null

/**
 * 初始化歌曲
 */
function initMusic() {
    var music = [{'name':'高飞 - 刘心韵', 'img': '../html/img/MP3_img.jpg', 'mp3': '../html/mp3/高飞.mp3'},
    {'name':'往后余生 - Assen捷', 'img': 'http://oeff2vktt.bkt.clouddn.com/image/98.jpg', 'mp3': 'http://www.ytmp3.cn/?down/48749.mp3'},
    {'name':'长安醉 - 徐海乔', 'img': 'https://y.gtimg.cn/music/photo_new/T002R300x300M000000nJV000QRqeB.jpg?max_age=2592000', 'mp3': 'http://www.ytmp3.cn/?down/48747.mp3'},
    {'name':'最近 - 沙尘', 'img': 'http://oeff2vktt.bkt.clouddn.com/image/65.jpg', 'mp3': 'http://www.ytmp3.cn/?down/48743.mp3'},
    {'name':'雨姬桩 - 洛天依', 'img': 'http://img4.kuwo.cn/star/starheads/240/68/28/1484671759.jpg', 'mp3': 'http://www.ytmp3.cn/?down/48731.mp3'},
    {'name':'佛系少女 - 冯提莫', 'img': 'https://y.gtimg.cn/music/photo_new/T002R300x300M000001CrpRT25yAN5.jpg?max_age=2592000', 'mp3': 'http://www.ytmp3.cn/?down/46741.mp3'}]
    var index = navigator.onLine ? index = Math.floor(Math.random() * (music.length - 1) + 1) : 0
    document.getElementById('audio_name').innerText = music[index]['name']
    document.getElementById('audio_small_img').src = document.getElementById('audio_small_img2').src = music[index]['img']
    document.getElementById('my_audio').src = music[index]['mp3']
}
 
/**
 * 设置事件监听
 */
function setListener() {
    // 点击播放
    document.getElementById('audio_img').onclick = function () {
        if (isPlay) audioPause()
        else audioPlay()
    }
    // 调节进度
    document.getElementById('audio_progress_1').onclick = function (event) {
        var value = event.clientX / 250
        value = value <= 0 ? 0 : value >= 1 ? 1 : value
        document.getElementById('audio_progress_2').style.width = value * 100 + '%'
        document.getElementById('my_audio').currentTime = document.getElementById('my_audio').duration * value
        if (!isPlay) audioPlay()
    }
    // 调节音量
    var progress_3 = document.getElementById('audio_volume_progress_3')
    var flag = false
    progress_3.addEventListener('mousedown', function (event) {
        progress_3.src = '../html/img/audio/progress_1.png'
        event.preventDefault()
        flag = true
    })
    document.addEventListener('mousemove', function (event) {
        if (flag) {
            var volume = event.clientX - 105
            volume = volume <= 0 ? 0 : volume >= 100 ? 100 : volume
            document.getElementById('audio_volume_progress_2').style.width = volume
            progress_3.style.marginLeft = volume - 8
            document.getElementById('my_audio').volume = volume * 0.007
        }
    })
    document.addEventListener('mouseup', function (event) {
        progress_3.src = '../html/img/audio/progress_2.png'
        flag = false
    })
}

/**
 * Audio播放
 */
function audioPlay() {
    isPlay = true
    document.getElementById('audio_img_1').src = '../html/img/audio/stop.png'
    document.getElementById('my_audio').play()
    runPlay = setInterval(function () {
        var audio = document.getElementById('my_audio')
        var progress = document.getElementById('audio_progress_2')
        progress.style.width = audio.currentTime / audio.duration * 100 + '%'
        if (audio.duration - audio.currentTime <= 0.8) {
            audio.currentTime = progress.style.width = 0
            initMusic()
            audioPlay()
        }
    }, 300)
}

/**
 * Audio暂停
 */
function audioPause() {
    isPlay = false
    clearInterval(runPlay)
    document.getElementById('my_audio').pause()
    document.getElementById('audio_img_1').src = '../html/img/audio/start.png'
}

/**
 * 设置Audio的动画
 */
function setAnimation() {
    // 进入动画
    document.getElementById('audio').addEventListener('mouseover', function () {
        if (document.getElementById('audio_big').style.display == 'inline') return
        document.getElementById('audio_small').style.display = 'none'
        document.getElementById('audio_big').style.marginLeft = -195
        document.getElementById('audio_big').style.display = 'inline'
        var i = -195
        var run = setInterval(function () {
            i += 30
            if (i >= 0) {
                document.getElementById('audio_big').style.marginLeft = 0
                clearInterval(run)
                return
            }
            document.getElementById('audio_big').style.marginLeft = i
        }, 25)
    })
    // 离开动画
    document.getElementById('audio_end').onclick = function () {
        var i = 0
        var run = setInterval(function () {
            i -= 30
            document.getElementById('audio_big').style.marginLeft = i
            if (i <= -260) {
                clearInterval(run)
                document.getElementById('audio_big').style.display = 'none'
                document.getElementById('audio_small').style.marginLeft = -63
                document.getElementById('audio_small').style.display = 'inline'
                var i2 = -63
                var run2 = setInterval(function () {
                    i2 += 20
                    if (i2 >= 7) {
                        document.getElementById('audio_small').style.marginLeft = 7
                        clearInterval(run2)
                        return
                    }
                    document.getElementById('audio_small').style.marginLeft = i2
                }, 25)
            }
        }, 25)
    }
}

initMusic()
setListener()
setAnimation()
document.getElementById('my_audio').volume = 0.28
