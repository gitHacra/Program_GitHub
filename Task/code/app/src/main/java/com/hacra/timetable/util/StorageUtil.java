package com.hacra.timetable.util;

import android.content.Context;

import java.io.FileInputStream;
import java.io.FileOutputStream;

import static android.content.Context.MODE_PRIVATE;

/**
 * @name: StorageUtil
 * @author: Hacra
 * @email: 2199887379@qq.com
 * @date: 2017/11/21 14:32
 * @comment: 读写任务
 */

class StorageUtil {

    private static final String FILE = "task.json";

    /**
     * 写入任务JSON字符串
     * @return JSON字符串
     */
    static String readTask(Context context) {
        try {
            FileInputStream inStream = context.openFileInput(FILE);
            byte[] temp = new byte[1024];
            StringBuilder sb = new StringBuilder("");
            int len;
            while ((len = inStream.read(temp)) > 0){
                sb.append(new String(temp, 0, len));
            }
            inStream.close();
            return sb.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 读取任务JSON字符串
     * @param json 任务JSON字符串
     * @return 1:保存成功，2:保存失败
     */
    static int writeTask(Context context, String json){
        if(json == null) {
            return 2;
        }
        try {
            FileOutputStream fos = context.openFileOutput(FILE, MODE_PRIVATE);
            fos.write(json.getBytes());
            fos.close();
            return 1;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return 2;
    }
}
