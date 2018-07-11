package com.hacra.timetable.model;

import java.util.List;

/**
 * @name: WeekTaskBean
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/20 22:28
 * @comment: 单个星期的任务模型
 */

public class WeekTaskBean {

    private List<WeekBean> week1;
    private List<WeekBean> week2;
    private List<WeekBean> week3;
    private List<WeekBean> week4;
    private List<WeekBean> week5;
    private List<WeekBean> week6;
    private List<WeekBean> week7;

    public List<WeekBean> getWeek1() {
        return week1;
    }

    public void setWeek1(List<WeekBean> week1) {
        this.week1 = week1;
    }

    public List<WeekBean> getWeek2() {
        return week2;
    }

    public void setWeek2(List<WeekBean> week2) {
        this.week2 = week2;
    }

    public List<WeekBean> getWeek3() {
        return week3;
    }

    public void setWeek3(List<WeekBean> week3) {
        this.week3 = week3;
    }

    public List<WeekBean> getWeek4() {
        return week4;
    }

    public void setWeek4(List<WeekBean> week4) {
        this.week4 = week4;
    }

    public List<WeekBean> getWeek5() {
        return week5;
    }

    public void setWeek5(List<WeekBean> week5) {
        this.week5 = week5;
    }

    public List<WeekBean> getWeek6() {
        return week6;
    }

    public void setWeek6(List<WeekBean> week6) {
        this.week6 = week6;
    }

    public List<WeekBean> getWeek7() {
        return week7;
    }

    public void setWeek7(List<WeekBean> week7) {
        this.week7 = week7;
    }

    public static class WeekBean {

        private String time;
        private String task;
        private boolean remind;

        public String getTime() {
            return time;
        }

        public void setTime(String time) {
            this.time = time;
        }

        public String getTask() {
            return task;
        }

        public void setTask(String task) {
            this.task = task;
        }

        public boolean getRemind() {
            return remind;
        }

        public void setRemind(boolean remind) {
            this.remind = remind;
        }
    }

}
