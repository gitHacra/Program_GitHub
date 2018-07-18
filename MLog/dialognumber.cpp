#include "dialognumber.h"
#include "ui_dialognumber.h"

DialogNumber::DialogNumber(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogNumber)
{
    ui->setupUi(this);
    this->setWindowFlags(Qt::Dialog | Qt::WindowCloseButtonHint);
    this->setWindowTitle("统计日志");
}

DialogNumber::~DialogNumber()
{
    delete ui;
}

// 显示统计数据
void DialogNumber::setNumber(int a, int f, int u) {
    int s = a + f + u;
    ui->num_a->setText(QString::number(a));
    ui->num_f->setText(QString::number(f));
    ui->num_u->setText(QString::number(u));
    ui->num_s->setText(QString::number(s));
    if (s == 0) {
        s = 1;
        ui->num_s_2->setText("0.00%");
    }
    else ui->num_s_2->setText("100.00%");
    ui->num_a_2->setText(QString::number(a * 100.0 / s, 'f', 2) + "%");
    ui->num_f_2->setText(QString::number(f * 100.0 / s, 'f', 2) + "%");
    ui->num_u_2->setText(QString::number(u * 100.0 / s, 'f', 2) + "%");
}
