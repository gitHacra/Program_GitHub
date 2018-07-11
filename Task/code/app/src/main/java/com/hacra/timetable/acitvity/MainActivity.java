package com.hacra.timetable.acitvity;

import android.content.Intent;
import android.support.v4.app.Fragment;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.TextView;

import com.hacra.timetable.R;
import com.hacra.timetable.adapter.MyFragmentAdapter;
import com.hacra.timetable.fragment.TaskFragmentA;
import com.hacra.timetable.fragment.TaskFragmentB;
import com.hacra.timetable.fragment.TaskFragmentC;
import com.hacra.timetable.fragment.TaskFragmentD;
import com.hacra.timetable.fragment.TaskFragmentE;
import com.hacra.timetable.fragment.TaskFragmentF;
import com.hacra.timetable.fragment.TaskFragmentG;


import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

/**
 * @name: MainActivity
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/18 17:02
 * @comment:
 */

public class MainActivity extends AppCompatActivity {

    /**
     * WEEK: 当前星期几[0~6]
     * TIME: 当前时间，以分钟为单位
     * WEEK_STR: 星期列表
     * mainTitle: 顶部标题
     * viewPager: 滑动视图
     * weekCurrent: 返回当前星期按钮
     */
    public static int WEEK;
    public static int TIME;
    public static final String[] WEEK_STR = {"周一", "周二", "周三", "周四", "周五", "周六", "周日"};
    private static List<Fragment> fragmentList;
    private TextView mainTitle;
    private TextView newTask;
    private ViewPager viewPager;
    private TextView weekCurrent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initTheme();            // 透明状态栏
        initComponent();        // 初始化组件

        loadAdapter(7);  // viewPager加载适配器
        initCurrentItem();       // viewPager起始显示页面

        newTaskListener();      // newTask点击监听
        viewPagerListener();    // viewPager滑动监听
        weekCurrentListener();  // weekCurrent点击监听
    }

    /**
     * 透明状态栏
     */
    private void initTheme() {
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_TRANSLUCENT_STATUS);
    }

    /**
     * 初始化组件
     */
    private void initComponent() {
        mainTitle = findViewById(R.id.main_title);
        newTask = findViewById(R.id.main_new);
        viewPager = findViewById(R.id.week_viewpager);
        weekCurrent = findViewById(R.id.week_current);
    }

    /**
     * viewPager加载适配器
     */
    private void loadAdapter(int position) {
        MyFragmentAdapter fragmentAdapter = new MyFragmentAdapter(getSupportFragmentManager(), getFragmentList(position));
        viewPager.setAdapter(fragmentAdapter);
    }

    /**
     * 获取当前星期几
     * viewPager起始显示页面
     */
    private void initCurrentItem() {
        Calendar calendar = Calendar.getInstance();
        TIME = calendar.get(Calendar.HOUR_OF_DAY) * 60 + calendar.get(Calendar.MINUTE);
        WEEK = calendar.get(Calendar.DAY_OF_WEEK) - 2;
        if (WEEK < 0) {
            WEEK = 6;
        }
        setMainTitle(WEEK);
        viewPager.setCurrentItem(WEEK);
    }

    /**
     * newTask点击监听
     * 跳转到添加新任务页面
     */
    private void newTaskListener() {
        newTask.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, NewTaskActivity.class);
                intent.putExtra("week", viewPager.getCurrentItem());
                startActivityForResult(intent, 0);
                overridePendingTransition(R.anim.activity_new_in, R.anim.activity_main_out);
            }
        });
    }

    /**
     * viewPager滑动监听
     * 改变背景颜色
     */
    private void viewPagerListener() {
        viewPager.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }

            @Override
            public void onPageSelected(int position) {
                setMainTitle(position);
            }

            @Override
            public void onPageScrollStateChanged(int state) {

            }
        });
    }

    /**
     * weekCurrent点击监听
     * 返回到当前星期页面
     */
    private void weekCurrentListener() {
        weekCurrent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewPager.setCurrentItem(WEEK);
            }
        });
    }

    /**
     * 为viewPager创建碎片列表数据源
     * 依次为周一至周日
     *
     * @return 碎片列表
     */
    private List<Fragment> getFragmentList(int position) {
        if (position == 7) {
            fragmentList = new ArrayList<>();
            fragmentList.add(new TaskFragmentA());
            fragmentList.add(new TaskFragmentB());
            fragmentList.add(new TaskFragmentC());
            fragmentList.add(new TaskFragmentD());
            fragmentList.add(new TaskFragmentE());
            fragmentList.add(new TaskFragmentF());
            fragmentList.add(new TaskFragmentG());
            return fragmentList;
        } else {
            switch (position) {
                case 0:
                    fragmentList.set(0, new TaskFragmentA());
                    break;
                case 1:
                    fragmentList.set(1, new TaskFragmentB());
                    break;
                case 2:
                    fragmentList.set(2, new TaskFragmentC());
                    break;
                case 3:
                    fragmentList.set(3, new TaskFragmentD());
                    break;
                case 4:
                    fragmentList.set(4, new TaskFragmentE());
                    break;
                case 5:
                    fragmentList.set(5, new TaskFragmentF());
                    break;
                default:
                    fragmentList.set(6, new TaskFragmentG());
            }
            return fragmentList;
        }
    }

    /**
     * 根据页面下标判断是否显示返回当前星期按钮
     * 根据页面下标设置当前页面的标题
     *
     * @param position 滑动页面下标[0~6]
     */
    private void setMainTitle(int position) {
        // 根据页面下标判断是否显示返回当前星期按钮
        if (WEEK == position) {
            weekCurrent.setVisibility(View.GONE);
        } else {
            weekCurrent.setVisibility(View.VISIBLE);
        }
        // 根据页面下标设置当前页面的标题
        mainTitle.setText(WEEK_STR[position]);
    }

    /**
     * 获取返回值
     * 显示离开时的界面
     */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 0) {
            // 没有添加数据
            if (resultCode == 0) {
                // 显示离开时的界面
                viewPager.setCurrentItem(data.getIntExtra("week", WEEK));
            }
            // 成功添加数据
            else if (resultCode == 1) {
                int index = data.getIntExtra("week", WEEK);
                // 重新加载适配器
                loadAdapter(index);
                // 显示离开时的界面
                viewPager.setCurrentItem(index);
            }
        }
    }

    /**
     * 修改任务后，再次跳转到此页面，更新数据
     */
    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        int week = getIntent().getIntExtra("week", 0);
        if(week >= 7) {
            week %= 7;
            loadAdapter(week);
            viewPager.setCurrentItem(week);
        }
    }

    /**
     * 按返回键时不退出程序保留在后台
     */
    @Override
    public void onBackPressed() {
        moveTaskToBack(false);
    }
}
