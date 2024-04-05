#include "RavenDBConnector.h"
#include <QNetworkRequest>
#include <QUrl>
#include <QJsonObject>
#include <QObject>
#include <QJsonDocument>
#include <QDebug>

RavenDBConnector::RavenDBConnector(QObject *parent) : QObject(parent)
{
    manager = new QNetworkAccessManager(this);
    connect(manager, &QNetworkAccessManager::finished, this, &RavenDBConnector::onFinished);
}

void RavenDBConnector::fetchData(const QString &documentId)
{
    //todo: thinh change the link
    QUrl url("http://your-ravendb-instance/databases/your-database/docs/" + documentId);
    QNetworkRequest request(url);
    // Set any necessary headers here, for example, authorization headers
    // request.setRawHeader("Authorization", "YourAuthHeader");
    manager->get(request);
}

void RavenDBConnector::onFinished(QNetworkReply *reply)
{
    if (reply->error() == QNetworkReply::NoError) {
        QByteArray response_data = reply->readAll();
        // Process the JSON data, for example:
        QJsonDocument jsonDoc = QJsonDocument::fromJson(response_data);
        QJsonObject jsonObject = jsonDoc.object();
        qDebug() << "Document fetched successfully:" << jsonObject;
        // Extract data from jsonObject as needed
    } else {
        qDebug() << "Error fetching document:" << reply->errorString();
    }
    reply->deleteLater();
}
