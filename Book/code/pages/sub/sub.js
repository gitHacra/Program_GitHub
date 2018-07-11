// ---------- //
// 图书分类页面 //
// ---------- //

// sub.js
Page({
  data: {
    dir: [{
      name: "文学",
      image: "../../images/dir/wenxue.png",
      sub: ["小说", "随笔", "经典", "诗歌", "杂文", "童话", "余华", "鲁迅", "诗词", "港台", "钱钟书", "古典文学", "外国名著"]
    }, {
      name: "经管",
      image: "../../images/dir/jing.png",
      sub: ["管理", "商业", "股票", "策划", "广告", "创业", "理财", "金融", "营销", "企业史", "经济学"]
    }, {
      name: "流行",
      image: "../../images/dir/liu.png",
      sub: ["漫画", "推理", "青春", "科幻", "奇幻", "穿越", "悬疑", "武侠", "校园", "绘本", "魔幻", "几米", "古龙", "落落", "张小娴", "郭敬明", "网络小说"]
    }, {
      name: "文化",
      image: "../../images/dir/wenhua.png",
      sub: ["历史", "哲学", "人文", "美术", "考古", "设计", "传记", "宗教", "佛学", "电影", "国学", "建筑", "音乐", "军事", "数学", "心理学", "社会学", "回忆录", "近代史", "政治学"]
    }, {
      name: "生活",
      image: "../../images/dir/sheng.png",
      sub: ["旅游", "成长", "健康", "摄影", "心里", "职场", "养生", "手工", "生活", "爱情", "家居", "励志", "美食", "情感", "游记", "自助游", "人际关系"]
    }, {
      name: "科技",
      image: "../../images/dir/ke.png",
      sub: ["UE", "UCD", "web", "科普", "编程", "科学", "算法", "交互", "程序", "通信", "互联网", "神经网络", "用户体验"]
    }]
  },
  // subTap
  subTap: function(e) {
    wx.getNetworkType({
      success: function(res) {
        if(res.networkType != 'none') {
          wx.navigateTo({
            url: '../list/list?sub=' + e.target.dataset.hi,
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
})