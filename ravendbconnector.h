#ifndef RAVENDBCONNECTOR_H
#define RAVENDBCONNECTOR_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkReply>

class RavenDBConnector : public QObject
{
    Q_OBJECT
public:
    explicit RavenDBConnector(QObject *parent = nullptr);
    void fetchData(const QString &documentId);

private slots:
    void onFinished(QNetworkReply *reply);

private:
    QNetworkAccessManager *manager;
};

#endif // RAVENDBCONNECTOR_H
