// chartviewmodel.cpp
#include "chartviewmodel.h"

ChartViewModel::ChartViewModel(QObject *parent) : QObject(parent)
{
}

void ChartViewModel::updateChart(QVariantList values)
{
    // Process the values and update the chart
    emit chartUpdated(values);
}
