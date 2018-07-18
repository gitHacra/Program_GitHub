#ifndef DIALOGMLOG_H
#define DIALOGMLOG_H

#include <QDialog>

namespace Ui {
class DialogMLog;
}

class DialogMLog : public QDialog
{
    Q_OBJECT

public:
    explicit DialogMLog(QWidget *parent = 0);
    ~DialogMLog();

private:
    Ui::DialogMLog *ui;
};

#endif // DIALOGMLOG_H
