// ---------- //
// 个人信息页面 //
// ---------- //

// user.js
Page({
  data: {
    name: "咏文图书",
    image: "../../images/icon.png",
    city: "点击登陆",
    yuImg: "../../images/tab/ding.png",
    guiImg: "../../images/tab/gui.png",
    tuiImg: "../../images/tab/tui.png",
    jieImg: "../../images/tab/jie.png",
    shouImg: "../../images/tab/shou.png",
    numYu: 0,
    numGui: 0,
    numTui: 0,
    numJie: 0,
    numCang: 0
  },
  // 获取用户信息
  onLoad: function () {
    var that = this
    wx.login({
      success: function (res) {
        wx.getUserInfo({
          success: function (res) {
            getApp().globalData.flag = true
            that.setData({
              numTui: 3,
              name: res.userInfo.nickName,
              image: res.userInfo.avatarUrl,
              city: res.userInfo.city
            })
          }
        })
      }
    })
  },
  // 登陆
  loginTap: function () {
    var that = this
    if (!getApp().globalData.flag) {
      wx.openSetting({
        success: (res) => {
          res.authSetting = {
            "scope.userInfo": true
          }
        },
        success: function () {
          wx.getUserInfo({
            success: function (res) {
              getApp().globalData.flag = true
              that.setData({
                numTui: 3,
                name: res.userInfo.nickName,
                image: res.userInfo.avatarUrl,
                city: res.userInfo.city
              })
            }
          })
        }
      })
    }
  },
  // 获取缓存数据
  onShow: function () {
    var that = this
    if (getApp().globalData.flag) {
      wx.getStorage({
        key: 'jie',
        success: function (res) {
          that.setData({
            numYu: res.data.length
          })
        },
      })
      wx.getStorage({
        key: 'cang',
        success: function (res) {
          that.setData({
            numCang: res.data.length
          })
        },
      })
      that.setData({
        numTui: 3
      })
    }
  },
  // showTap
  showTap: function (e) {
    if (getApp().globalData.flag) {
      wx.navigateTo({
        url: '../show/show?id=' + e.target.dataset.hi,
      })
    }
  }
})
