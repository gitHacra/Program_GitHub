package com.hacra.timetable.util;

import android.content.Context;
import android.widget.ListView;

import com.hacra.timetable.acitvity.MainActivity;
import com.hacra.timetable.adapter.MyBaseAdapter;

import java.util.List;
import java.util.Map;

/**
 * @name: TaskFragmentUtil
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/20 20:51
 * @comment: TaskFragment工具类
 */

public class TaskFragmentUtil {

    /**
     * 为TaskFragment碎片中listView创建适配器
     * @param context 当前上下文
     * @param listView listView
     * @param week 星期下标[0~6]
     */
    public static boolean loadAdapter(Context context, ListView listView, int week) {
        List<Map<String, String>> taskList = WeekTaskUtil.getTaskList(context, week);
        if(taskList == null || taskList.size() == 0) {
            return false;
        }
        /* flag: 两位数[是否更换颜色]
                 99表示全部字体为默认颜色
                 其他数字表示任务下标，并将其设置为指定颜色 */
        int flag = WeekTaskUtil.getCurrentTaskIndex(context, week, MainActivity.TIME);
        MyBaseAdapter baseAdapter = new MyBaseAdapter(context, taskList, flag);
        listView.setAdapter(baseAdapter);
        return true;
    }
}
