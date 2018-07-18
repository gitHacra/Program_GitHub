#include <regex>
#include <QLabel>
#include <QFile>
#include <QDebug>
#include <QTextStream>
#include <QFileDialog>
#include <QMessageBox>
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QList<QStringList> dataList, QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    // 设置图标
    this->setWindowIcon(QIcon("mlog.ico"));
    this->setWindowTitle("MLog");
    // 设置状态栏
    QLabel *label = new QLabel("完成");
    ui->statusBar->addWidget(label);
    ui->statusBar->setVisible(false);
    // 设置行变色
    ui->tableWidget->setAlternatingRowColors(true);
    // 设置列宽
    ui->tableWidget->setColumnWidth(0, 100);
    ui->tableWidget->setColumnWidth(1, 70);
    ui->tableWidget->setColumnWidth(2, 460);
    ui->tableWidget->setColumnWidth(3, 110);
    ui->tableWidget->setColumnWidth(4, 250);
    ui->tableWidget->setColumnWidth(5, 100);
    // 去除虚线边框
    ui->tableWidget->setFocusPolicy(Qt::NoFocus);
    // 设置字体
    ui->tableWidget->verticalHeader()->setFont(QFont("宋体", 12));
    // 取消高亮
    ui->tableWidget->horizontalHeader()->setHighlightSections(false);
    ui->tableWidget->verticalHeader()->setHighlightSections(false);

    // 显示文件
    if (dataList.size() == 0) return;
    ui->tableWidget->setRowCount(dataList.size());
    isSave = false;
    this->setWindowTitle(Tools::mLogFileUrl+ "* - MLog");
    for (int i = 0; i < dataList.size(); i++) {
        ui->tableWidget->setItem(i, 0, new QTableWidgetItem(dataList[i][0]));
        ui->tableWidget->setItem(i, 1, new QTableWidgetItem(dataList[i][1]));
        ui->tableWidget->setItem(i, 2, new QTableWidgetItem(dataList[i][2]));
        ui->tableWidget->setItem(i, 3, new QTableWidgetItem(dataList[i][3]));
        ui->tableWidget->setItem(i, 4, new QTableWidgetItem(dataList[i][4]));
        ui->tableWidget->setItem(i, 5, new QTableWidgetItem(dataList[i][5]));
    }
    MainWindow::on_save_file_triggered();
}

MainWindow::~MainWindow()
{
    delete ui;
}

// 添加行
void MainWindow::on_insert_row_triggered()
{
    if (ui->tableWidget->item(0, 0) == NULL || ui->tableWidget->item(0, 0)->text() != "") {
        ui->tableWidget->insertRow(0);
        ui->tableWidget->setRowHeight(0, 30);
        ui->tableWidget->setItem(0, 0, new QTableWidgetItem(""));
        ui->tableWidget->setItem(0, 1, new QTableWidgetItem(""));
        ui->tableWidget->setItem(0, 2, new QTableWidgetItem(""));
        ui->tableWidget->setItem(0, 3, new QTableWidgetItem(""));
        ui->tableWidget->setItem(0, 4, new QTableWidgetItem(""));
        ui->tableWidget->setItem(0, 5, new QTableWidgetItem(""));
    }
}

// 删除行
void MainWindow::on_delete_row_triggered()
{
    // 只有没有版本号就删除
    if (ui->tableWidget->item(0, 0) != NULL && ui->tableWidget->item(0, 0)->text() == "") {
        ui->tableWidget->removeRow(0);
    }
}

// 格式检测
void MainWindow::on_tableWidget_cellChanged(int row, int column)
{
    isSave = false;
    if (Tools::mLogFileUrl == "") this->setWindowTitle("newFile* - MLog");
    else this->setWindowTitle(Tools::mLogFileUrl + "* - MLog");
    if (ui->tableWidget->item(row, column)->text() == "") return;
    // 版本号
    if (column == 0) {
        std::regex repPattern("[0-9]+[.][0-9]+[.][0-9]+",std::regex_constants::extended);
        std::smatch  rerResult;
        std::string strValue = ui->tableWidget->item(row, column)->text().toStdString();
        if (!std::regex_match(strValue, rerResult, repPattern)) {
            ui->tableWidget->setItem(row, column, new QTableWidgetItem(""));
            ui->statusBar->showMessage("版本号格式错误", 3000);
        }
        ui->tableWidget->item(row, column)->setTextAlignment(Qt::AlignCenter);
    }
    // 类型
    else if (column == 1) {
        QString type = ui->tableWidget->item(row, column)->text();
        if (type == "A") ui->tableWidget->item(row, column)->setTextColor(QColor(51, 163, 255));
        else if (type == "F") ui->tableWidget->item(row, column)->setTextColor(QColor(173, 51, 255));
        else if (type == "U") ui->tableWidget->item(row, column)->setTextColor(QColor(255, 150, 51));
        else {
            ui->tableWidget->setItem(row, column, new QTableWidgetItem(""));
            ui->statusBar->showMessage("类型格式错误", 3000);
        }
        ui->tableWidget->item(row, column)->setTextAlignment(Qt::AlignCenter);
    }
    // 日期
    else if (column == 3) {
        std::regex repPattern("[0-9]{4}[-][0-9]{2}[-][0-9]{2}",std::regex_constants::extended);
        std::smatch  rerResult;
        std::string strValue = ui->tableWidget->item(row, column)->text().toStdString();
        if (!std::regex_match(strValue, rerResult, repPattern)) {
            ui->tableWidget->setItem(row, column, new QTableWidgetItem(""));
            ui->statusBar->showMessage("日期格式错误", 3000);
        }
        ui->tableWidget->item(row, column)->setTextAlignment(Qt::AlignCenter);
    }
    // 作者
    else if (column == 5) {
        ui->tableWidget->item(row, column)->setTextAlignment(Qt::AlignCenter);
    }
}


// 打开文件
void MainWindow::on_open_file_triggered()
{
    if (!isSave) {
        QMessageBox::StandardButton rb = QMessageBox::information(NULL, "MLog", "是否保存更改信息?\t\t\t\t\t\t", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        if (rb == QMessageBox::Yes) MainWindow::on_save_file_triggered();
    }
    QString filename = QFileDialog::getOpenFileName(this, "Open Document", "", "Document files (*.mlog)");
    if (!filename.isNull()) {
        QList<QStringList> dataList = tools->getFile(filename);
        if (dataList.size() == 0) return;
        isSave = false;
        this->setWindowTitle(Tools::mLogFileUrl + "* - MLog");
        ui->tableWidget->setRowCount(dataList.size());
        for (int i = 0; i < dataList.size(); i++) {
            ui->tableWidget->setItem(i, 0, new QTableWidgetItem(dataList[i][0]));
            ui->tableWidget->setItem(i, 1, new QTableWidgetItem(dataList[i][1]));
            ui->tableWidget->setItem(i, 2, new QTableWidgetItem(dataList[i][2]));
            ui->tableWidget->setItem(i, 3, new QTableWidgetItem(dataList[i][3]));
            ui->tableWidget->setItem(i, 4, new QTableWidgetItem(dataList[i][4]));
            ui->tableWidget->setItem(i, 5, new QTableWidgetItem(dataList[i][5]));
        }
    }
    MainWindow::on_save_file_triggered();
}

// 保存文件
void MainWindow::on_save_file_triggered()
{
    if (isSave) return;
    QStringList dataList;
    int rows = ui->tableWidget->rowCount();
    for (int i = 0; i < rows; i++) {
        QString data;
        for (int j = 0; j < 5; j++) {
            data += (ui->tableWidget->item(i, j)->text() + "&&");
        }
        data += ui->tableWidget->item(i, 5)->text();
        dataList.append(data);
    }
    if (Tools::mLogFileUrl == "") {
        QString name = Tools::mLogFileUrl == "" ? "newFile" : Tools::mLogFileUrl;
        QString fileName = QFileDialog::getSaveFileName(this, "Open Config", name, "Config Files (*.mlog)");
        if (fileName.isNull()) return;
        else Tools::mLogFileUrl = fileName;
    }
    QFile file(Tools::mLogFileUrl);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text)) return;
    QTextStream out(&file);
    out.setCodec("utf-8");
    for (int i = 0; i < dataList.size(); i++) {
        out << dataList[i] << "\n";
    }
    isSave = true;
    this->setWindowTitle(Tools::mLogFileUrl + " - MLog");
    ui->statusBar->showMessage("保存成功", 3000);
}

// 新建文件
void MainWindow::on_new_file_triggered()
{
    if (!isSave) {
        QMessageBox::StandardButton rb = QMessageBox::information(NULL, "MLog", "是否保存更改信息?\t\t\t\t\t\t", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        if (rb == QMessageBox::Yes) MainWindow::on_save_file_triggered();
    }
    Tools::mLogFileUrl = "";
    ui->tableWidget->clearContents();
    ui->tableWidget->setRowCount(0);
    this->setWindowTitle("newFile* - MLog");
    MainWindow::on_insert_row_triggered();
}

// 关闭文件
void MainWindow::on_close_file_triggered()
{
    if (!isSave) {
        QMessageBox::StandardButton rb = QMessageBox::information(NULL, "MLog", "是否保存更改信息?\t\t\t\t\t\t", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        if (rb == QMessageBox::Yes) MainWindow::on_save_file_triggered();
    }
    Tools::mLogFileUrl = "";
    ui->tableWidget->clearContents();
    ui->tableWidget->setRowCount(0);
    isSave = true;
    windowTitle = "";
    this->setWindowTitle("MLog");
}

// 退出程序
void MainWindow::closeEvent(QCloseEvent *event) {
    if (!isSave) {
        QMessageBox::StandardButton rb = QMessageBox::information(NULL, "MLog", "是否保存更改信息?\t\t\t\t\t\t", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        if (rb == QMessageBox::Yes) MainWindow::on_save_file_triggered();
    }
}

// 关于MLog
void MainWindow::on_about_MLog_triggered()
{
    dialogMLog = new DialogMLog(this);
    dialogMLog->show();
}

// 默认窗口大小
void MainWindow::on_resize_MLog_triggered()
{
    this->resize(1160, 720);
    ui->tableWidget->setColumnWidth(0, 100);
    ui->tableWidget->setColumnWidth(1, 70);
    ui->tableWidget->setColumnWidth(2, 460);
    ui->tableWidget->setColumnWidth(3, 110);
    ui->tableWidget->setColumnWidth(4, 250);
    ui->tableWidget->setColumnWidth(5, 100);
}

// 统计日志
void MainWindow::on_count_MLog_triggered()
{
    int a = 0, f = 0, u = 0;
    for (int i = 0; i < ui->tableWidget->rowCount(); i++) {
        QString type = ui->tableWidget->item(i, 1)->text();
        if (type == "A") a += 1;
        else if (type == "F") f += 1;
        else if (type == "U") u += 1;
    }
    dialogNumber = new DialogNumber(this);
    dialogNumber->setNumber(a, f, u);
    dialogNumber->show();
}

// 是否显示状态栏
void MainWindow::on_statusbar_view_triggered()
{
    if (ui->statusbar_view->text() == "显示状态栏(E)") {
        ui->statusBar->setVisible(true);
        ui->statusbar_view->setText("隐藏状态栏(E)");
    }
    else {
        ui->statusBar->setVisible(false);
        ui->statusbar_view->setText("显示状态栏(E)");
    }
}
