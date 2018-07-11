package com.hacra.timetable.adapter;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;

import java.util.List;

/**
 * @name: MyFragmentAdapter
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/19 11:20
 * @comment: MainActivity中viewPaper的适配器
 */

public class MyFragmentAdapter extends FragmentStatePagerAdapter{

    /**
     * fragmentList: 数据源
     */
    private final List<Fragment> fragmentList;

    public MyFragmentAdapter(FragmentManager fm, List<Fragment> fragmentList) {
        super(fm);
        this.fragmentList = fragmentList;
    }

    @Override
    public Fragment getItem(int position) {
        return fragmentList.get(position);
    }

    @Override
    public int getCount() {
        return fragmentList.size();
    }

}
