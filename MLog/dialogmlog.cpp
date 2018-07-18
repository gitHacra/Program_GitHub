#include "dialogmlog.h"
#include "ui_dialogmlog.h"

DialogMLog::DialogMLog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogMLog)
{
    ui->setupUi(this);
    this->setWindowFlags(Qt::Dialog | Qt::WindowCloseButtonHint);
    this->setWindowTitle("关于MLog");
}

DialogMLog::~DialogMLog()
{
    delete ui;
}
