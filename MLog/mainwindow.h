#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTableWidgetItem>
#include <QCloseEvent>
#include "tools.h"
#include "dialognumber.h"
#include "dialogmlog.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QList<QStringList> dataList, QWidget *parent = 0);
    void closeEvent(QCloseEvent *event);
    ~MainWindow();

private slots:
    void on_insert_row_triggered();

    void on_delete_row_triggered();

    void on_tableWidget_cellChanged(int row, int column);

    void on_open_file_triggered();

    void on_save_file_triggered();

    void on_new_file_triggered();

    void on_close_file_triggered();

    void on_about_MLog_triggered();

    void on_resize_MLog_triggered();

    void on_count_MLog_triggered();

    void on_statusbar_view_triggered();

private:
    Ui::MainWindow *ui;
    bool isSave = true;
    QString windowTitle;
    Tools *tools;
    DialogNumber *dialogNumber;
    DialogMLog * dialogMLog;
};

#endif // MAINWINDOW_H
