package com.hacra.timetable.adapter;

import android.content.Context;
import android.support.v4.content.ContextCompat;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.hacra.timetable.R;

import java.util.List;
import java.util.Map;

/**
 * @name: MyBaseAdapter
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/19 15:03
 * @comment: TaskFragment碎片中listView的适配器
 */

public class MyBaseAdapter extends BaseAdapter{

    /**
     * context: 上下文
     * inflater：页面布局
     * dataList: 数据源
     * flag: 两位数[是否更换颜色]
     *       99表示全部字体为默认颜色
     *       其他数字表示任务下标，并将其设置为特定颜色
     */
    private final int flag;
    private final Context context;
    private final LayoutInflater inflater;
    private final List<Map<String, String>> dataList;

    /**
     * 自定义BaseAdapter
     * @param context 当前上下文
     * @param dataList 数据源
     * @param flag 任务标志
     */
    public MyBaseAdapter(Context context, List<Map<String, String>> dataList, int flag) {
        super();
        this.context = context;
        this.inflater = LayoutInflater.from(context);
        this.dataList = dataList;
        this.flag = flag;
    }

    @Override
    public int getCount() {
        return dataList.size();
    }

    @Override
    public Object getItem(int i) {
        return dataList.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        ViewHolder viewHolder;
        if(view == null) {
            viewHolder = new ViewHolder();
            view = inflater.inflate(R.layout.item_task, null);
            viewHolder.itemTime = view.findViewById(R.id.item_time);
            viewHolder.itemTask = view.findViewById(R.id.item_task);
            view.setTag(viewHolder);
        }
        else {
            viewHolder = (ViewHolder) view.getTag();
        }
        Map<String, String> dataMap = dataList.get(i);
        viewHolder.itemTime.setText(dataMap.get("time"));
        viewHolder.itemTask.setText(dataMap.get("task"));
        // 如果为99表示使用默认颜色
        if(flag % 100 == 99) {
            return view;
        }
        // 将当前时间段的任务文字设置为指定颜色
        if(flag % 100 == i) {
            viewHolder.itemTime.setTextColor(ContextCompat.getColor(context, R.color.colorBackground_1));
            viewHolder.itemTask.setTextColor(ContextCompat.getColor(context, R.color.colorBackground_1));
        }
        return view;
    }

    static class ViewHolder {
        TextView itemTime;
        TextView itemTask;
    }
}
