// -------------- //
//     书籍页面
// -------------- //
Page({
  data: {
    searchImg: "../../images/search.png",
    searchTxt: "输入图书名称",
    scanImg: "../../images/scan.png",
    showImg: "../../images/showImg.jpg",
    paiImg: "../../images/tab/pai.png",
    fenImg: "../../images/tab/fen.png",
    xinImg: "../../images/tab/xin.png",
    pingImg: "../../images/tab/ping.png",
    tabIndex: 1,
    paibooks: [{
      title: "社会学的想象力",
      author: "C·赖特·米尔斯 ",
      publisher: "北京师范大学出版社",
      pubdate: "2017-3-2",
      grade: "8.9",
      isbn: "9787303212842",
      image: "../../images/books/shehui.jpg"
    }, {
      title: "哈佛商学院谈判课",
      author: "[美] 迪帕克·马哈拉 ",
      publisher: "湖南文艺出版社",
      pubdate: "2017-6",
      grade: "9.4",
      isbn: "9787540480608",
      image: "../../images/books/hafo.jpg"
    }, {
      title: "地下铁",
      author: "幾米",
      publisher: "辽宁教育出版社",
      pubdate: "2002-2",
      grade: "8.3",
      isbn: "9787538262537",
      image: "../../images/books/dixia.jpg"
    }, {
      title: "呼吸课",
      author: "安·泰勒",
      publisher: "百花文艺出版社",
      pubdate: "2017-3",
      grade: "8.0",
      isbn: "9787530655603",
      image: "../../images/books/huxi.jpg"
    }, {
      title: "故事思维",
      author: "安妮特·西蒙斯 ",
      publisher: "江西人民出版社",
      pubdate: "2017-3",
      grade: "8.0",
      isbn: "9787210075172",
      image: "../../images/books/gushi.jpg"
    }],
    xinbooks: [{
      title: "杂草记",
      author: "柳宗民",
      publisher: "四川文艺出版社",
      pubdate: "2017-4-1",
      grade: "9.1",
      isbn: "9787541145711",
      image: "../../images/books/zacao.jpg"
    }, {
      title: "社会学的想象力",
      author: "C·赖特·米尔斯 ",
      publisher: "北京师范大学出版社",
      pubdate: "2017-3-2",
      grade: "8.9",
      isbn: "9787303212842",
      image: "../../images/books/shehui.jpg"
    }, {
      title: "呼吸课",
      author: "安·泰勒",
      publisher: "百花文艺出版社",
      pubdate: "2017-3",
      grade: "8.0",
      isbn: "9787530655603",
      image: "../../images/books/huxi.jpg"
    }, {
      title: "故事思维",
      author: "安妮特·西蒙斯 ",
      publisher: "江西人民出版社",
      pubdate: "2017-3",
      grade: "8.0",
      isbn: "9787210075172",
      image: "../../images/books/gushi.jpg"
    }, {
      title: "地下铁",
      author: "幾米",
      publisher: "辽宁教育出版社",
      pubdate: "2002-2",
      grade: "8.3",
      isbn: "9787538262537",
      image: "../../images/books/dixia.jpg"
    }, {
      title: "照相本子",
      author: "幾米",
      publisher: "大塊文化出版公司",
      pubdate: "2001-6-18",
      grade: "8.4",
      isbn: "9789570316759",
      image: "../../images/books/zhaoxiang.jpg"
    }]
  },
  // 搜索跳转
  searchTap: function () {
    wx.navigateTo({
      url: '../search/search',
    })
  },
  // 条码扫描
  scanTap: function () {
    wx.scanCode({
      success: function (e) {
        if (e.result.length == 13 && e.result.substring(0, 3) == '978') {
          wx.navigateTo({
            url: '../info/info?isbn=' + e.result,
          })
        }
        else {
          wx.showToast({
            title: '请扫描图书编码',
          })
        }
      }
    })
  },
  // 排行列表
  paiTap: function () {
    this.setData({
      tabIndex: 1
    })
  },
  // 分类跳转
  fenTap: function () {
    wx.navigateTo({
      url: '../sub/sub',
    })
  },
  // 新书列表
  xinTap: function () {
    this.setData({
      tabIndex: 2
    })
  },
  // 评论跳转
  pingTap: function () {
    wx.navigateTo({
      url: '../comment/comment',
    })
  },
  // 图书信息
  bookTap: function (e) {
    wx.getNetworkType({
      success: function (res) {
        if (res.networkType != 'none') {
          wx.navigateTo({
            url: '../info/info?isbn=' + e.target.dataset.hi,
          })
        }
        else {
          wx.showToast({
            title: '无法连接到网络',
          })
        }
      },
    })
  },
  // 转发
  onShareAppMessage: function () {
    return {
      title: '咏其文，思其义',
      path: '/index/index'
    }
  }
})
