package com.hacra.timetable.acitvity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.WindowManager;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.hacra.timetable.R;
import com.hacra.timetable.model.WeekTaskBean;
import com.hacra.timetable.util.WeekTaskUtil;

/**
 * @name: ViewTaskActivity
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/22 20:57
 * @comment:
 */

public class ViewTaskActivity extends AppCompatActivity {

    /**
     * week: 星期下标
     * index: 任务下标
     * viewBack: 返回上一页
     * viewTask: 任务内容
     * viewTime: 任务时间
     * viewEdit: 编辑任务
     * viewDelete: 删除任务
     */
    private int week;
    private int index;
    private TextView viewBack;
    private TextView viewTask;
    private TextView viewTime;
    private ImageView viewEdit;
    private ImageView viewDelete;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_task);

        initTheme();            // 透明状态栏
        initComponent();        // 初始化组件
        initData();             // 初始化数据

        viewBackListener();     // viewBack点击监听
        viewEditListener();     // viewEdit点击监听
        viewDeleteListener();   // viewDelete点击监听
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
        viewBack = findViewById(R.id.view_back);
        viewTask = findViewById(R.id.view_task);
        viewTime = findViewById(R.id.view_time);
        viewEdit = findViewById(R.id.view_edit);
        viewDelete = findViewById(R.id.view_delete);
    }

    /**
     * 初始化数据
     */
    private void initData() {
        week = getIntent().getIntExtra("week", MainActivity.WEEK);
        index = getIntent().getIntExtra("index", 0);
        WeekTaskBean.WeekBean weekBean = WeekTaskUtil.getWeekBean(this, week, index);
        if (weekBean == null) {
            viewTask.setText("任务加载失败");
        } else {
            viewTask.setText(weekBean.getTask());
            viewTime.setText(String.format("%s %s", MainActivity.WEEK_STR[week], weekBean.getTime()));
        }
    }

    /**
     * viewBack点击监听
     */
    private void viewBackListener() {
        viewBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(ViewTaskActivity.this, MainActivity.class);
                intent.putExtra("index", week);
                setResult(1, intent);
                finish();
                overridePendingTransition(R.anim.activity_main_in, R.anim.activity_view_out);
            }
        });
    }

    /**
     * viewEdit点击监听
     * 跳转到NewTaskActivity
     */
    private void viewEditListener() {
        viewEdit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(ViewTaskActivity.this, NewTaskActivity.class);
                intent.putExtra("week", week + 7);
                intent.putExtra("index", index);
                startActivity(intent);
                overridePendingTransition(R.anim.activity_new_in, R.anim.activity_main_out);
            }
        });
    }

    /**
     * viewDelete点击监听
     * 跳转到MainActivity
     */
    private void viewDeleteListener() {
        viewDelete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showDialog();
            }
        });
    }

    /**
     * 删除任务提示对话框
     */
    private void showDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(ViewTaskActivity.this);
        builder.setMessage("确定删除此任务吗？\n");
        builder.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (WeekTaskUtil.removeTask(ViewTaskActivity.this, week, index)) {
                    Toast.makeText(ViewTaskActivity.this, "删除成功", Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(ViewTaskActivity.this, MainActivity.class);
                    intent.putExtra("week", week + 7);
                    startActivity(intent);
                    overridePendingTransition(R.anim.activity_main_in, R.anim.activity_view_out);
                }
                else {
                    Toast.makeText(ViewTaskActivity.this, "删除失败", Toast.LENGTH_SHORT).show();
                }
            }
        });
        builder.setNegativeButton("取消", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.dismiss();
            }
        });
        AlertDialog  dialog = builder.create();
        dialog.show();
        dialog.getButton(AlertDialog.BUTTON_POSITIVE).setTextColor(ContextCompat.getColor(ViewTaskActivity.this, R.color.colorBackground_1));
        dialog.getButton(AlertDialog.BUTTON_NEGATIVE).setTextColor(ContextCompat.getColor(ViewTaskActivity.this, R.color.colorText_4));
    }

    /**
     * 重写返回函数
     */
    @Override
    public void onBackPressed() {
        Intent intent = new Intent(ViewTaskActivity.this, MainActivity.class);
        intent.putExtra("index", week);
        setResult(1, intent);
        finish();
        overridePendingTransition(R.anim.activity_main_in, R.anim.activity_view_out);
    }

}
