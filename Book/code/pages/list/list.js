// ------------- //
// 二级分类列表页面 //
// ------------- //

// list.js
Page({
  data: {
    books: [{
      title: "社会学的想象力",
      author: "C·赖特·米尔斯 ",
      publisher: "北京师范大学出版社",
      pubdate: "2017-3-2",
      grade: "8.9",
      isbn: "9787303212842",
      image: "../../images/books/shehui.jpg"
    }, {
      title: "照相本子",
      author: "幾米",
      publisher: "大塊文化出版公司",
      pubdate: "2001-6-18",
      grade: "8.4",
      isbn: "9789570316759",
      image: "../../images/books/zhaoxiang.jpg"
    }, {
      title: "地下铁",
      author: "幾米",
      publisher: "辽宁教育出版社",
      pubdate: "2002-2",
      grade: "8.3",
      isbn: "9787538262537",
      image: "../../images/books/dixia.jpg"
    }, {
      title: "杂草记",
      author: "柳宗民",
      publisher: "四川文艺出版社",
      pubdate: "2017-4-1",
      grade: "9.1",
      isbn: "9787541145711",
      image: "../../images/books/zacao.jpg"
    }, {
      title: "呼吸课",
      author: "安·泰勒",
      publisher: "百花文艺出版社",
      pubdate: "2017-3",
      grade: "8.0",
      isbn: "9787530655603",
      image: "../../images/books/huxi.jpg"
    }, {
      title: "社会学的想象力",
      author: "C·赖特·米尔斯 ",
      publisher: "北京师范大学出版社",
      pubdate: "2017-3-2",
      grade: "8.9",
      isbn: "9787303212842",
      image: "../../images/books/shehui.jpg"
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
    }]
  },
  onLoad: function (e) {
    wx.setNavigationBarTitle({
      title: e.sub,
    })
  },
  bookTap: function (e) {
    wx.navigateTo({
      url: '../info/info?isbn=' + e.target.dataset.hi,
    })
  }
})
