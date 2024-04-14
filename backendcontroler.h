#ifndef BACKENDCONTROLER_H
#define BACKENDCONTROLER_H

#include <QObject>
#include <QVariantList>

class BackendControler : public QObject
{
    Q_OBJECT
public:
    explicit BackendControler(QObject *parent = nullptr);
    ~BackendControler();

    Q_INVOKABLE QString exampleFunction(const QString& scriptPath);

    Q_INVOKABLE void t1_Trigger(const QString& value);
    Q_INVOKABLE void t2_Trigger(const QString& value);
    Q_INVOKABLE void t3_Trigger(const QString& value1, const QString& value2, const QString& value3);
    Q_INVOKABLE void t4_Trigger(const QString& value);
    Q_INVOKABLE void t5_Trigger(const QString& value);
    Q_INVOKABLE void t6_Trigger(const QString& value1, const QString& value2);

signals:

    void t1_userName(QVariant values);
    void t1_Table(QVariantList name, QVariantList brand, QVariantList cate, QVariantList rating);

    void t2_Table(QVariantList name, QVariantList sale, QVariantList ratio);

    void t3_productName(QVariant values);
    void t3_ChartName(QVariantList values);
    void t3_ChartV1(QVariantList values);
    void t3_ChartV2(QVariantList values);

    void t4_productName(QVariant values);
    void t4_tableView(QVariantList name,QVariantList v1,QVariantList v2);

    void t5_chart(QVariantList values);

    void allPromotionsUpdated(QVariantList values);
    void t6_productName(QVariant values);
    void t6_chart(QVariantList values);
};

#endif // BACKENDCONTROLER_H
