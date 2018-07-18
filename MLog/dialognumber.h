#ifndef DIALOGNUMBER_H
#define DIALOGNUMBER_H

#include <QDialog>

namespace Ui {
class DialogNumber;
}

class DialogNumber : public QDialog
{
    Q_OBJECT

public:
    explicit DialogNumber(QWidget *parent = 0);
    void setNumber(int a, int f, int u);
    ~DialogNumber();

private:
    Ui::DialogNumber *ui;
};

#endif // DIALOGNUMBER_H
