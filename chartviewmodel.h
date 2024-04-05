// chartviewmodel.h
#ifndef CHARTVIEWMODEL_H
#define CHARTVIEWMODEL_H

#include <QObject>
#include <QVariantList>

class ChartViewModel : public QObject
{
    Q_OBJECT

public:
    explicit ChartViewModel(QObject *parent = nullptr);

public slots:
    void updateChart(QVariantList values);

signals:
    void chartUpdated(QVariantList values);
};

#endif // CHARTVIEWMODEL_H
