var htmlHeight = {"main":960, "message":485, "photo":630, "table":270}

function setIframeHeight(html) {
    window.scroll(0, 0)
    document.getElementById('iframe').style.height = htmlHeight[html]
}
