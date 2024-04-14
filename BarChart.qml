import QtQuick 2.15
import QtCharts 2.15

Item {
    width: 400
    height: 300
    id: mainChart

    ChartView {

        title: "Bar series"
        anchors.fill: parent
        legend.alignment: Qt.AlignBottom
        antialiasing: true

        BarSeries {
            id: series
            axisX: BarCategoryAxis { categories: ["2007", "2008", "2009", "2010", "2011"] }
            BarSet {
                id: mainBarSet
                label: "Bob";
                values: [20,40,10,70,30]

                function updateChart(newValues) {
                    values = newValues
                }
            }
        }
    }


    Connections{
        target: chartViewModel
        function onChartUpdated(value) {
            mainBarSet.updateChart(value)
        }
    }

    Timer{
        interval: 2000
        repeat: false
        running: true
        onTriggered: {
            chartViewModel.updateChart([5,4,3,4,5])
            console.log("emit completed")
        }
    }
}
