// ---------- //
// 图书详情页面 //
// ---------- //

Page({
  data: {
    hide: false,
    isbn: "",
    info: {},
    tabIndex: 1,
    tabColor1: "#FFFFFF",
    tabColor2: "#DADADA",
    tabColor3: "#DADADA",
    jieImg0: "../../images/tab/ding.png",
    cangImg0: "../../images/tab/shou.png",
    xiangImg0: "../../images/tab/xiang.png",
    jieImg: "../../images/jie.png",
    cangImg: "../../images/cang.png",
    xiang: [{
      isbn: "9787115282828",
      title: "数学之美",
      image: "../../images/books/shu.jpg"
    }, {
      isbn: "9787508649719",
      title: "从0到1",
      image: "../../images/books/cong.jpg"
    }, {
      isbn: "9787544752473",
      title: "你一生的故事",
      image: "../../images/books/ni.jpg"
    }]
  },
  // 由ISBN获取详细信息
  onLoad: function (e) {
    var that = this
    wx.showNavigationBarLoading()
    wx.request({
      url: 'https://api.douban.com/v2/book/isbn/' + e.isbn,
      header: {
        "Content-Type": "application/text"
      },
      success: function (e) {
        that.setData({
          info: e.data,
          isbn: e.data.isbn13
        })
        wx.setNavigationBarTitle({
          title: e.data.title
        })
        wx.getStorage({
          key: 'jie',
          success: function (res) {
            for (var j = 0; j < res.data.length; j++) {
              if (res.data[j] == that.data.isbn) {
                that.setData({
                  jieImg: "../../images/jie1.png"
                })
                break
              }
            }
          },
        })
        wx.getStorage({
          key: 'cang',
          success: function (res) {
            for (var c = 0; c < res.data.length; c++) {
              if (res.data[c] == that.data.isbn) {
                that.setData({
                  cangImg: "../../images/cang1.png"
                })
              }
            }
          },
        })
      },
      complete: function () {
        that.setData({
          hide: true
        })
        wx.hideNavigationBarLoading()
      }
    })
  },
  // 内容简介
  tabTap1: function () {
    this.setData({
      tabIndex: 1,
      tabColor1: "#FFFFFF",
      tabColor2: "#DADADA",
      tabColor3: "#DADADA"
    })
  },
  // 作者简介
  tabTap2: function () {
    this.setData({
      tabIndex: 2,
      tabColor1: "#DADADA",
      tabColor2: "#FFFFFF",
      tabColor3: "#DADADA"
    })
  },
  // 借阅选项
  tabTap3: function () {
    this.setData({
      tabIndex: 3,
      tabColor1: "#DADADA",
      tabColor2: "#DADADA",
      tabColor3: "#FFFFFF"
    })
  },
  // 借阅
  jieTap: function () {
    var that = this
    if (!getApp().globalData.flag) {
      wx.showModal({
        title: '请登录账号',
        content: '',
        success: function (res) {
          if (res.confirm) {
            wx.switchTab({
              url: '../user/user',
            })
          }
        }
      })
    }
    else if (this.data.jieImg == "../../images/jie.png") {
      var jie1 = []
      wx.getStorage({
        key: 'jie',
        success: function (res) {
          jie1 = res.data
          jie1 = jie1.concat([that.data.isbn])
          wx.setStorage({
            key: 'jie',
            data: jie1,
          })
        },
        fail: function () {
          jie1 = [that.data.isbn]
          wx.setStorage({
            key: 'jie',
            data: jie1,
          })
        },
        complete: function () {
          that.setData({
            jieImg: "../../images/jie1.png"
          })
        }
      })
      wx.showToast({
        title: '已借阅',
      })
    }
    else {
      var jie1 = []
      wx.getStorage({
        key: 'jie',
        success: function (res) {
          jie1 = res.data
          for (var j = 0; j < jie1.length; j++) {
            if (jie1[j] == that.data.isbn) {
              jie1.splice(j, 1)
              wx.setStorage({
                key: 'jie',
                data: jie1,
              })
              break
            }
          }
          that.setData({
            jieImg: "../../images/jie.png"
          })
        }
      })
      wx.showToast({
        title: '取消借阅',
      })
    }
  },
  // 收藏
  cangTap: function () {
    var that = this
    if (!getApp().globalData.flag) {
      wx.showModal({
        title: '请登录账号',
        content: '',
        success: function (res) {
          if (res.confirm) {
            wx.switchTab({
              url: '../user/user',
            })
          }
        }
      })
    }
    else if (this.data.cangImg == "../../images/cang.png") {
      var cang1 = []
      wx.getStorage({
        key: 'cang',
        success: function (res) {
          cang1 = res.data
          cang1 = cang1.concat([that.data.isbn])
          wx.setStorage({
            key: 'cang',
            data: cang1,
          })
        },
        fail: function () {
          cang1 = [that.data.isbn]
          wx.setStorage({
            key: 'cang',
            data: cang1,
          })
        },
        complete: function () {
          that.setData({
            cangImg: "../../images/cang1.png"
          })
        }
      })
      wx.showToast({
        title: '已收藏',
      })
    }
    else {
      var cang1 = []
      wx.getStorage({
        key: 'cang',
        success: function (res) {
          cang1 = res.data
          for (var j = 0; j < cang1.length; j++) {
            if (cang1[j] == that.data.isbn) {
              cang1.splice(j, 1)
              wx.setStorage({
                key: 'cang',
                data: cang1,
              })
              break
            }
          }
          that.setData({
            cangImg: "../../images/cang.png"
          })
        }
      })
      wx.showToast({
        title: '取消收藏',
      })
    }
  },
  // 相关书籍
  xiangTap: function (e) {
    wx.redirectTo({
      url: '../info/info?isbn=' + e.target.dataset.hi,
    })
  },
  // 转发
  onShareAppMessage: function () {
    var that = this
    return {
      title: "《" + that.data.info.title + "》",
      path: '/index/index'
    }
  }
})

