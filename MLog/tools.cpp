#include <QFile>
#include <QTextStream>
#include "tools.h"

QString Tools::mLogFileUrl = "";

Tools::Tools()
{

}

// 获取文件
QList<QStringList> Tools::getFile(QString url) {
    // "F:/Program_Log/wx/order.mlog"
    QList<QStringList> dataList;
    if (url.right(5) != ".mlog")  return dataList;
    Tools::mLogFileUrl = url;
    QFile file(url);
    if(!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return dataList;
    }
    QTextStream text(&file);
    text.setCodec("utf-8");
    while(!text.atEnd()) {
        QString str = text.readLine();
        str.replace("\n", "");
        QStringList list = str.split("&&");
        if (list.length() != 6) {
            dataList.clear();
            return dataList;
        }
        dataList.append(list);
    }
    return dataList;
}

