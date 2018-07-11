// ------- //
// 搜索页面 //
// ------- //

Page({
  data: {
    flag: true,
    txt: "",
    books: [],
    history: []
  },
  // 获取搜索历史记录
  onLoad: function(e) {
    var that = this
    var his = []
    wx.getStorage({
      key: 'history',
      success: function(res) {
        his = his.concat(res.data)
        that.setData({
          history: his
        })
      },
    })
  },
  // 图书搜索
  formSubmit: function (e) {
    this.search(e.detail.value.input, true)
  },
  // 输入操作
  inputTap: function () {
    this.setData({
      flag: true,
      books: []
    })
  },
  // 图书信息
  bookTap: function (e) {
    wx.navigateTo({
      url: '../info/info?isbn=' + e.target.dataset.hi,
    })
  },
  // 搜索历史
  hisTap: function(e) {
    this.setData({
      txt: e.target.dataset.hi
    })
    this.search(e.target.dataset.hi, false)
  },
  // 清空历史
  hiTap: function() {
    this.setData({
      history: []
    })
    wx.setStorage({
      key: 'history',
      data: [],
    })
  },
  // 图书搜索
  search: function(v, f) {
    var that = this
    if (v.trim().length != 0) {
      var name = v.trim()
      wx.getNetworkType({
        success: function (res) {
          if (res.networkType != 'none') {
            wx.showNavigationBarLoading()
            wx.request({
              url: 'https://api.douban.com/v2/book/search?q=' + name, 
              header: {
                "Content-Type": "application/text"
              },
              success: function (e) {
                that.setData({
                  books: e.data.books,
                  flag: false
                })
                if (e.data.count == 0) {
                  wx.showToast({
                    title: '未找到相关书籍',
                  })
                }
              },
              complete: function () {
                wx.hideNavigationBarLoading()
                if(f) {
                  var his = that.data.history
                  for(var h = 0; h < his.length; h++) {
                    if(his[h] == name) {
                      return
                    }
                  }
                  his.push(name)
                  that.setData({
                    history: his
                  })
                  wx.setStorage({
                    key: 'history',
                    data: that.data.history,
                  })
                }
              }
            })
          }
          else {
            wx.showToast({
              title: '无法连接到网络',
            })
          }
        },
      })
    }
  }
})
