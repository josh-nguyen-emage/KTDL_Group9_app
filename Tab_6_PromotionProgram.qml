import QtQuick 2.15
import QtCharts 2.3
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    width: 600
    height: 400

    ColumnLayout {
        anchors.fill: parent
        RowLayout{
            Layout.fillWidth: true

            // Text box
            TextField {
                id: textField
                Layout.fillWidth: true
                placeholderText: "Enter Product id"
                text: "products/1839-A"
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.pixelSize: 18
                Layout.preferredHeight: 50
            }

            // Text box
            TextField {
                id: productName
                Layout.fillWidth: true
                text: "Product name"
                readOnly: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.pixelSize: 18
                Layout.preferredHeight: 50
            }

            ComboBox {
                id: comboBox
                Layout.fillWidth: true
                model: [
                    "Super Sale 1/1 2023",
                    "Super Sale 2/2 2023",
                    "Super Sale 3/3 2023",
                    "Super Sale 4/4 2023",
                    "Super Sale 5/5 2023",
                    "Super Sale 6/6 2023",
                    "Super Sale 7/7 2023",
                    "Super Sale 8/8 2023",
                    "Super Sale 9/9 2023",
                    "Super Sale 10/10 2023",
                    "Super Sale 11/11 2023",
                    "Super Sale 12/12 2023",
                    "Super Sale 1/1 2024",
                    "Super Sale 2/2 2024",
                    "Super Sale 3/3 2024",
                    "Super Sale 4/4 2024",
                    ]
                currentIndex: 0 // Initial selection
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                onCurrentIndexChanged: {
                    // Handle selection changed event
                    console.log("Selected option:", currentText)

                }

                Connections{
                    target: backendControler
                    function onAllPromotionsUpdated(values){
                        comboBox.model = values
                    }

                    function onT6_chart(values){
                        bar1.values = [values[0], values[1]]
                        bar2.values = [values[2], values[3]]
                    }
                    function onT6_productName(values){
                        bar1.label = values
                        productName.text = values
                    }
                }
            }

            Button{
                Layout.preferredWidth: 100
                text: "Query"
                onClicked: {
                    backendControler.t6_Trigger(textField.text,comboBox.currentText)
                }
            }
        }

        RowLayout{
            Layout.fillWidth: true
            ChartView {
                legend.visible: true
                Layout.fillWidth: true
                Layout.fillHeight: true

                BarSeries {
                    axisX: BarCategoryAxis {
                        categories: ["Toàn tháng", "Trong khuyến mãi"]
                    }
                    BarSet {
                        id: bar1
                        label: "Product Name"
                        values: [60, 25]
                    }
                }
            }

            ChartView {
                legend.visible: true
                Layout.fillWidth: true
                Layout.fillHeight: true

                BarSeries {
                    axisX: BarCategoryAxis {
                        categories: ["Toàn tháng", "Trong khuyến mãi"]
                    }
                    BarSet {
                        id: bar2
                        label: "Tất cả"
                        values: [100, 60000]
                    }
                }
            }
        }
    }
}
