package com.hacra.timetable.acitvity;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.WindowManager;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.hacra.timetable.R;
import com.hacra.timetable.model.WeekTaskBean;
import com.hacra.timetable.util.WeekTaskUtil;
import com.suke.widget.SwitchButton;

import cn.qqtheme.framework.picker.TimePicker;

/**
 * @name: NewTaskActivity
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/21 14:58
 * @comment: 添加新任务
 */

public class NewTaskActivity extends AppCompatActivity {

    /**
     * week: 传入的星期下标
     * task: 任务内容
     * h1,m1: 开始时间
     * h2,m2: 结束时间
     * remind: 是否提醒
     * newBack: 取消按钮
     * newTitle: 标题
     * newAdd: 确认按钮
     * newTask: 任务输入框
     * newStartTime: 开始时间
     * newEndTime: 结束时间
     * newRemind: 是否提醒
     */
    private int week;
    private int index;
    private String task;
    private boolean remind;
    private TextView newBack;
    private TextView newTitle;
    private TextView newAdd;
    private EditText newTask;
    private TextView newStartTime;
    private TextView newEndTime;
    private SwitchButton newRemind;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_task);

        initTheme();            // 透明状态栏
        initComponent();        // 初始化组件
        initData();             // 初始化数据

        newBackListener();      // newBack点击监听
        newAddListener();       // newAdd点击监听
        newStartTimeListener(); // newStartTime点击监听
        newEndTimeListener();   // newEndTime点击监听
        newRemindListener();    // newRemind点击监听
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
        newBack = findViewById(R.id.new_back);
        newTitle = findViewById(R.id.new_title);
        newAdd = findViewById(R.id.new_add);
        newTask = findViewById(R.id.new_task);
        newStartTime = findViewById(R.id.new_start_time);
        newEndTime = findViewById(R.id.new_end_time);
        newRemind = findViewById(R.id.new_remind);
    }

    /**
     * 初始化数据
     */
    private void initData() {
        week = getIntent().getIntExtra("week", MainActivity.WEEK);
        if(week < 7) {
            newTitle.setText(String.format("添加任务-%s", MainActivity.WEEK_STR[week]));
            remind = false;
        }
        else {
            index = getIntent().getIntExtra("index", 0);
            WeekTaskBean.WeekBean weekBean = WeekTaskUtil.getWeekBean(NewTaskActivity.this, week % 7, index);
            assert weekBean != null;
            newTitle.setText(String.format("修改任务-%s", MainActivity.WEEK_STR[week % 7]));
            newTask.setText(weekBean.getTask());
            newStartTime.setText(weekBean.getTime().substring(0, 5));
            newEndTime.setText(weekBean.getTime().substring(8));
            newRemind.setChecked(weekBean.getRemind());
            remind = weekBean.getRemind();
        }
    }

    /**
     * newBack点击监听
     */
    private void newBackListener() {
        newBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(NewTaskActivity.this, MainActivity.class);
                intent.putExtra("week", week % 7);
                setResult(0, intent);
                finish();
                overridePendingTransition(R.anim.activity_main_in, R.anim.activity_new1_out);
            }
        });
    }

    /**
     * newAdd点击监听
     * 添加任务
     */
    private void newAddListener() {
        newAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 任务不能为空
                task = newTask.getText().toString().trim();
                if(task.isEmpty() || task == null) {
                    Toast.makeText(NewTaskActivity.this, "任务不能为空", Toast.LENGTH_SHORT).show();
                    return;
                }
                // 结束时间大于等于开始时间
                String h1 = newStartTime.getText().toString().substring(0, 2);
                String m1 = newStartTime.getText().toString().substring(3);
                String h2 = newEndTime.getText().toString().substring(0, 2);
                String m2 = newEndTime.getText().toString().substring(3);
                if(Integer.parseInt(h2) < Integer.parseInt(h1)) {
                    Toast.makeText(NewTaskActivity.this, "时间段错误", Toast.LENGTH_SHORT).show();
                    return;
                }
                else if(Integer.parseInt(h2) == Integer.parseInt(h1) && Integer.parseInt(m2) < Integer.parseInt(m1)) {
                    Toast.makeText(NewTaskActivity.this, "时间段错误", Toast.LENGTH_SHORT).show();
                    return;
                }
                // 生成weekBean对象
                WeekTaskBean.WeekBean weekBean = new WeekTaskBean.WeekBean();
                weekBean.setTask(task);
                weekBean.setTime(String.format("%s:%s - %s:%s", h1, m1, h2, m2));
                weekBean.setRemind(remind);
                // 添加新任务
                if(week < 7) {
                    // 返回标识 - 1：保存成功，2：保存失败，3：时间段重叠
                    switch (WeekTaskUtil.addNewTask(NewTaskActivity.this, week % 7, weekBean)) {
                        case 1:
                            Toast.makeText(NewTaskActivity.this, "保存成功", Toast.LENGTH_SHORT).show();
                            Intent intent = new Intent(NewTaskActivity.this, MainActivity.class);
                            intent.putExtra("week", week);
                            setResult(1, intent);
                            finish();
                            overridePendingTransition(R.anim.activity_main_in, R.anim.activity_new2_out);
                            break;
                        case 2:
                            Toast.makeText(NewTaskActivity.this, "保存失败", Toast.LENGTH_SHORT).show();
                            break;
                        case 3:
                            Toast.makeText(NewTaskActivity.this, "时间段重叠", Toast.LENGTH_SHORT).show();
                            break;
                        default:
                    }
                }
                // 修改任务
                else {
                    // 返回标识 - 1：保存成功，2：保存失败，3：时间段重叠
                    switch (WeekTaskUtil.updateTask(NewTaskActivity.this, week % 7, index, weekBean)) {
                        case 1:
                            Toast.makeText(NewTaskActivity.this, "修改成功", Toast.LENGTH_SHORT).show();
                            Intent intent = new Intent(NewTaskActivity.this, MainActivity.class);
                            intent.putExtra("week", week);
                            startActivity(intent);
                            overridePendingTransition(R.anim.activity_main_in, R.anim.activity_new2_out);
                            break;
                        case 2:
                            Toast.makeText(NewTaskActivity.this, "修改失败", Toast.LENGTH_SHORT).show();
                            break;
                        case 3:
                            Toast.makeText(NewTaskActivity.this, "时间段重叠", Toast.LENGTH_SHORT).show();
                            break;
                        default:
                    }
                }
            }
        });
    }

    /**
     * newStartTime点击监听
     */
    private void newStartTimeListener() {
        newStartTime.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //默认选中当前时间
                TimePicker picker = new TimePicker(NewTaskActivity.this);
                picker.setTopLineVisible(false);
                picker.setOnTimePickListener(new TimePicker.OnTimePickListener() {
                    @Override
                    public void onTimePicked(String hour, String minute) {
                        newStartTime.setText(String.format("%s:%s", hour, minute));
                    }
                });
                picker.show();
            }
        });
    }

    /**
     * newEndTime点击监听
     */
    private void newEndTimeListener() {
        newEndTime.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //默认选中当前时间
                TimePicker picker = new TimePicker(NewTaskActivity.this);
                picker.setTopLineVisible(false);
                picker.setOnTimePickListener(new TimePicker.OnTimePickListener() {
                    @Override
                    public void onTimePicked(String hour, String minute) {
                        newEndTime.setText(String.format("%s:%s", hour, minute));
                    }
                });
                picker.show();
            }
        });
    }

    /**
     * newRemind点击监听
     */
    private void newRemindListener() {
        newRemind.setOnCheckedChangeListener(new SwitchButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(SwitchButton view, boolean isChecked) {
                remind = isChecked;
            }
        });
    }

    /**
     * 重写返回函数
     */
    @Override
    public void onBackPressed() {
        Intent intent = new Intent(NewTaskActivity.this, MainActivity.class);
        intent.putExtra("week", week % 7);
        setResult(0, intent);
        finish();
        overridePendingTransition(R.anim.activity_main_in, R.anim.activity_new1_out);
    }
}
