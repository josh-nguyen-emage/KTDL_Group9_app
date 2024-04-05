#include "backendcontroler.h"

BackendControler::BackendControler(QObject *parent) : QObject(parent)
{

}

BackendControler::~BackendControler(){}

QString BackendControler::exampleFunction(const QString& scriptPath)
{
    return "Everything work, for now";
}
