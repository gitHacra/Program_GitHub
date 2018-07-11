package com.hacra.timetable.util;

import android.content.Context;

import com.google.gson.Gson;
import com.hacra.timetable.acitvity.MainActivity;
import com.hacra.timetable.model.WeekTaskBean;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @name: WeekTaskUtil
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/19 12:30
 * @comment: 处理任务
 */

public class WeekTaskUtil {

    /**
     * 单个星期的任务数据模型
     */
    private static WeekTaskBean weekTaskBean;

    /**
     * 获取某一天的任务数据模型
     * @param position 星期下标
     * @return 当天任务数据模型
     */
    private static List<WeekTaskBean.WeekBean> getWeekBeanList(Context context, int position) {
        if (weekTaskBean == null) {
            Gson gson = new Gson();
            String json = StorageUtil.readTask(context);
            if(json == null) {
                weekTaskBean = new WeekTaskBean();
                List<WeekTaskBean.WeekBean> weekBeanList1 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList2 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList3 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList4 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList5 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList6 = new ArrayList<>();
                List<WeekTaskBean.WeekBean> weekBeanList7 = new ArrayList<>();
                weekTaskBean.setWeek1(weekBeanList1);
                weekTaskBean.setWeek2(weekBeanList2);
                weekTaskBean.setWeek3(weekBeanList3);
                weekTaskBean.setWeek4(weekBeanList4);
                weekTaskBean.setWeek5(weekBeanList5);
                weekTaskBean.setWeek6(weekBeanList6);
                weekTaskBean.setWeek7(weekBeanList7);
                return null;
            }
            weekTaskBean = gson.fromJson(json, WeekTaskBean.class);
        }
        switch (position) {
            case 0: return weekTaskBean.getWeek1();
            case 1: return weekTaskBean.getWeek2();
            case 2: return weekTaskBean.getWeek3();
            case 3: return weekTaskBean.getWeek4();
            case 4: return weekTaskBean.getWeek5();
            case 5: return weekTaskBean.getWeek6();
            default: return weekTaskBean.getWeek7();
        }
    }

    /**
     * 获取某一天的任务数据
     * @param position 星期下标
     * @return 当天任务数据
     */
    static List<Map<String, String>> getTaskList(Context context, int position) {
        List<Map<String, String>> taskList = new ArrayList<>();
        List<WeekTaskBean.WeekBean> weekBeanList = getWeekBeanList(context, position);
        if(weekBeanList == null) {
            return null;
        }
        for(WeekTaskBean.WeekBean weekBean : weekBeanList) {
            Map<String, String> map = new HashMap<>(3);
            map.put("time", weekBean.getTime());
            map.put("task", weekBean.getTask());
            taskList.add(map);
        }
        return taskList;
    }

    /**
     * 获取某一天某一个任务模型
     * @param context 当前上下文
     * @param week 星期下标
     * @param position 当天任务下标
     * @return 某一个任务模型
     */
    public static WeekTaskBean.WeekBean getWeekBean(Context context, int week, int position) {
        List<WeekTaskBean.WeekBean> weekBeanList = getWeekBeanList(context, week);
        if(weekBeanList == null || weekBeanList.size() <= position) {
            return null;
        }
        return weekBeanList.get(position);
    }

    /**
     * 获取当天某一时刻任务的下标
     * @param position 星期下标
     * @param currentTime 当前时间，单位为分钟
     * @return 任务下标或者99[代表不再此范围内]
     */
    static int getCurrentTaskIndex(Context context, int position, int currentTime) {
        List<WeekTaskBean.WeekBean> weekBeanList = getWeekBeanList(context, position);
        if(weekBeanList == null || position != MainActivity.WEEK) {
            return 99;
        }
        for(int i = 0; i < weekBeanList.size(); i++) {
            WeekTaskBean.WeekBean weekBean = weekBeanList.get(i);
            String time = weekBean.getTime();
            int startTime = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3, 5));
            int endTime = Integer.parseInt(time.substring(8, 10)) * 60 + Integer.parseInt(time.substring(11));
            if(currentTime >= startTime && currentTime < endTime) {
                return i;
            }
        }
        return 99;
    }

    /**
     * 添加新任务，共有5种情况
     * 情况1: 如果为空，直接添加
     * 情况2: 是否可以添加在开头
     * 情况3: 是否可以添加在结尾
     * 情况4: 是否可以添加在中间
     * @param context 当前上下文
     * @param week 星期下标
     * @param bean 任务对象
     * @return 1：保存成功，2：保存失败，3：时间段重叠
     */
    public static int addNewTask(Context context, int week, WeekTaskBean.WeekBean bean) {
        List<WeekTaskBean.WeekBean> weekBeanList = getWeekBeanList(context, week);
        Gson gson = new Gson();
        // 情况1: 如果为空，直接添加
        assert weekBeanList != null;
        if(weekBeanList.size() == 0) {
            weekBeanList.add(bean);
            return StorageUtil.writeTask(context, gson.toJson(weekTaskBean));
        }
        // 情况2: 是否可以添加在开头
        String time = bean.getTime();
        String time2 = weekBeanList.get(0).getTime();
        int end1 = Integer.parseInt(time.substring(8, 10)) * 60 + Integer.parseInt(time.substring(11));
        int start2 = Integer.parseInt(time2.substring(0, 2)) * 60 + Integer.parseInt(time2.substring(3, 5));
        if(end1 <= start2) {
            weekBeanList.add(0, bean);
            return StorageUtil.writeTask(context, gson.toJson(weekTaskBean));
        }
        // 情况3: 是否可以添加在结尾
        time2 = weekBeanList.get(weekBeanList.size() - 1).getTime();
        int start1 = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3, 5));
        int end2 = Integer.parseInt(time2.substring(8, 10)) * 60 + Integer.parseInt(time2.substring(11));
        if(end2 <= start1) {
            weekBeanList.add(bean);
            return StorageUtil.writeTask(context, gson.toJson(weekTaskBean));
        }
        // 情况4: 是否可以添加在中间
        for(int i = 1; i < weekBeanList.size(); i++) {
            time2 = weekBeanList.get(i-1).getTime();
            end2 = Integer.parseInt(time2.substring(8, 10)) * 60 + Integer.parseInt(time2.substring(11));
            time2 = weekBeanList.get(i).getTime();
            start2 = Integer.parseInt(time2.substring(0, 2)) * 60 + Integer.parseInt(time2.substring(3, 5));
            if(end2 <= start1 && end1 <= start2) {
                weekBeanList.add(i, bean);
                return StorageUtil.writeTask(context, gson.toJson(weekTaskBean));
            }
            else if(end2 > start1) {
                break;
            }
        }
        // 情况5: 时间段重叠
        return 3;
    }

    /**
     * 修改任务
     * @param context 当前上下文
     * @param week 星期下标
     * @param index 任务下标
     * @param bean 任务对象
     * @return 1：成功，2：失败，3：时间段重叠
     */
    public static int updateTask(Context context, int week, int index, WeekTaskBean.WeekBean bean) {
        if(removeTask(context, week, index)) {
            return addNewTask(context, week, bean);
        }
        else {
            return 2;
        }
    }

    /**
     * 删除任务
     * @param context 当前上下文
     * @param week 星期下标
     * @param index 任务下标
     * @return true：成功，false：失败
     */
    public static boolean removeTask(Context context, int week, int index) {
        List<WeekTaskBean.WeekBean> weekBeanList = getWeekBeanList(context, week);
        if(weekBeanList == null || weekBeanList.size() < index) {
            return false;
        }
        weekBeanList.remove(index);
        StorageUtil.writeTask(context, new Gson().toJson(weekTaskBean));
        return true;
    }
}
