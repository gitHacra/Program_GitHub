// ----------------- //
// 预定、归还、借书页面 //
// ----------------- //

// show.js
Page({
  data: {
    title: ["预定书籍", "归还书籍", "推荐书籍", "借书历史", "我的收藏"],
    empty: "../../images/empty.png",
    books: [{
      isbn: "9787115282828",
      title: "数学之美",
      author: "[美] 吴军",
      publisher: "人民邮电出版社",
      pubdate: "2012-5-1",
      grade: "8.7",
      image: "../../images/books/shu.jpg"
    }, {
      isbn: "9787508649719",
      title: "从0到1",
      author: "彼得·蒂尔",
      publisher: "中信出版股份有限公司",
      pubdate: "2015-1-1",
      grade: "7.6",
      image: "../../images/books/cong.jpg"
    }, {
      isbn: "9787544752473",
      title: "你一生的故事",
      author: "[美] 特德·姜",
      publisher: "译林出版社",
      pubdate: "2015-5",
      grade: "8.6",
      image: "../../images/books/ni.jpg"
    }]
  },
  onLoad: function (e) {
    var that = this
    wx.setNavigationBarTitle({
      title: that.data.title[e.id]
    })
    wx.showNavigationBarLoading()
    if (e.id == 0) {
      that.setData({
        books: []
      })
      wx.getStorage({
        key: 'jie',
        success: function (res) {
          for (var j = 0; j < res.data.length; j++) {
            that.search(res.data[j])
          }
        },
      })
    }
    else if (e.id == 1) {
      that.setData({
        books: []
      })
    }
    else if (e.id == 2) {
      if (!getApp().globalData.flag) {
        that.setData({
          books: []
        })
      }
    }
    else if (e.id == 3) {
      that.setData({
        books: []
      })
    }
    else if (e.id == 4) {
      that.setData({
        books: []
      })
      wx.getStorage({
        key: 'cang',
        success: function (res) {
          for (var j = 0; j < res.data.length; j++) {
            that.search(res.data[j])
          }
        },
      })
    }
    wx.hideNavigationBarLoading()
  },
  // bookTap
  bookTap: function (e) {
    wx.navigateTo({
      url: '../info/info?isbn=' + e.target.dataset.hi,
    })
  },
  // 获取图书信息
  search: function (isbn) {
    var that = this
    wx.request({
      url: 'https://api.douban.com/v2/book/isbn/' + isbn,
      header: {
        "Content-Type": "application/text"
      },
      success: function (e) {
        var book = {}
        book.isbn = e.data.isbn13
        book.title = e.data.title
        book.author = e.data.author[0]
        book.publisher = e.data.publisher
        book.pubdate = e.data.pubdate
        book.grade = e.data.rating.average
        book.image = e.data.image
        var bs = that.data.books
        bs.push(book)
        that.setData({
          books: bs
        })
      }
    })
  }
})

