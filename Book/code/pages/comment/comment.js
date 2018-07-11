// ------- //
// 评论页面 //
// ------- //

// comment.js
Page({
  data: {
    empty: "../../images/empty.png"
  },
  onLoad: function() {
    wx.setNavigationBarTitle({
      title: '最新评论'
    })
  }
})