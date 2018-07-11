package com.hacra.timetable.fragment;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.ListView;

import com.hacra.timetable.R;
import com.hacra.timetable.acitvity.ViewTaskActivity;
import com.hacra.timetable.util.TaskFragmentUtil;

/**
 * @name: TaskFragmentA
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/18 20:00
 * @comment: 当前碎片为周三界面
 */

public class TaskFragmentC extends Fragment{

    /**
     * WEEK_INT: 当前为周一
     * view: 界面布局
     * emptyImage: 没有任务
     * listView: 任务列表
     */
    private static final int WEEK_INT = 2;
    private View view;
    private ImageView emptyImage;
    private ListView listView;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        view = inflater.inflate(R.layout.fragment_task, container, false);

        initComponent();    // 初始化组件

        loadAdapter();      // listView加载适配器
        listViewListener(); // listView点击监听

        return view;
    }

    /**
     * 初始化组件
     */
    private void initComponent() {
        emptyImage = view.findViewById(R.id.week_empty);
        listView = view.findViewById(R.id.week_listview);
    }

    /**
     * listView加载适配器
     * 如果没有数据，则显示emptyImage
     */
    private void loadAdapter() {
        if(TaskFragmentUtil.loadAdapter(getActivity(), listView, WEEK_INT)) {
            listView.setVisibility(View.VISIBLE);
            emptyImage.setVisibility(View.GONE);
        }
        else {
            emptyImage.setVisibility(View.VISIBLE);
            listView.setVisibility(View.GONE);
        }
    }

    /**
     * listView点击监听
     * 跳转到详情页面
     */
    private void listViewListener() {
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent intent = new Intent(getActivity(), ViewTaskActivity.class);
                intent.putExtra("week", WEEK_INT);
                intent.putExtra("index", i);
                startActivity(intent);
                getActivity().overridePendingTransition(R.anim.activity_view_in, R.anim.activity_main_out);
            }
        });
    }
}
