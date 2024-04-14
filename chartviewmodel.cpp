// chartviewmodel.cpp
#include "chartviewmodel.h"
#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QList>
#include <QDebug>

ChartViewModel::ChartViewModel(QObject *parent) : QObject(parent)
{
}

QVariantList readAndSumLines(const QString& filePath) {
    QVariantList sums;

    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Failed to open file: " << file.errorString();
        return sums;
    }

    QTextStream in(&file);
    QString line;

    // Skip first two lines
    in.readLine();
    in.readLine();

    while (!in.atEnd()) {
        line = in.readLine();
        QStringList tokens = line.split(" ", QString::SkipEmptyParts);

        float sum = 0.0;
        for (const QString& token : tokens) {
            bool ok;
            float value = token.toFloat(&ok);
            if (ok) {
                sum += value;
            } else {
                qDebug() << "Error converting token to float: " << token;
            }
        }

        sums.append(QVariant(sum));
    }

    file.close();

    return sums;
}

QVariantList keepTop5Max(const QVariantList& inputList) {
    QVariantList result;

    // Convert the QVariantList to a QVector of floats
    QVector<float> floatVector;
    floatVector.reserve(inputList.size());
    for (const QVariant& variant : inputList) {
        if (variant.canConvert<float>()) {
            floatVector.append(variant.toFloat());
        } else {
            qDebug() << "Error converting QVariant to float.";
        }
    }

    // Sort the QVector in descending order
    std::sort(floatVector.begin(), floatVector.end(), std::greater<float>());

    // Keep the top 5 maximum values
    int count = qMin(5, floatVector.size());
    for (int i = 0; i < count; ++i) {
        result.append(QVariant(floatVector[i]));
    }

    return result;
}

void ChartViewModel::updateChart(QVariantList values)
{
    // Process the values and update the chart

    QVariantList txtData = readAndSumLines("D:/1 - Study/5 - KTDL_2024/Kafka/Kafka/received_last_minutes.txt");
    QVariantList maxValues = keepTop5Max(txtData);

    qDebug() << maxValues;

    emit chartUpdated(maxValues);
}
