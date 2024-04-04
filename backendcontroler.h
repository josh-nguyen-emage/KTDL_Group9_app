#ifndef BACKENDCONTROLER_H
#define BACKENDCONTROLER_H

#include <QObject>

class BackendControler : public QObject
{
    Q_OBJECT
public:
    explicit BackendControler(QObject *parent = nullptr);
    ~BackendControler();

    Q_INVOKABLE QString exampleFunction(const QString& scriptPath);
};

#endif // BACKENDCONTROLER_H
