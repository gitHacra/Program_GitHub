#ifndef TOOLS_H
#define TOOLS_H

#include <QString>

class Tools
{
public:
    static QString mLogFileUrl;
    Tools();
    QList<QStringList> getFile(QString url);
};

#endif // TOOLS_H
