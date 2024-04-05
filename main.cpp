#include <QApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <backendcontroler.h>
#include <chartviewmodel.h>
#include <ravendbconnector.h>


int main(int argc, char *argv[])
{
    QApplication  app(argc, argv);

    QQmlApplicationEngine engine;
    BackendControler backendControler;
    ChartViewModel chartViewModel;

    engine.rootContext()->setContextProperty("backendControler", &backendControler);
    engine.rootContext()->setContextProperty("chartViewModel", &chartViewModel);

    const QUrl url(QStringLiteral("qrc:/main.qml"));
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    return app.exec();
}
