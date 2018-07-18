#include <QApplication>
#include "mainwindow.h"
#include "tools.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);    

    Tools open;
    QList<QStringList> dataList;
    if (argc >= 2) dataList = open.getFile(argv[1]);

    MainWindow mainWindow(dataList);
    mainWindow.show();

    return a.exec();
}
