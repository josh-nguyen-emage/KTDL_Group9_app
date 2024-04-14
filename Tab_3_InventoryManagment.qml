import QtQuick 2.15
import QtCharts 2.3
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    width: 600
    height: 400

    ColumnLayout {
        anchors.fill: parent

        // Text box
        Rectangle {
            Layout.fillWidth: true
            height: 50
            color: "lightgray"
            radius: 5

            RowLayout {
                anchors.fill: parent
                spacing: 5
                TextInput {
                    id: productIdInput
                    Layout.fillWidth: true
                    text: "products/184-A"
                }
                TextField {
                    id: productName
                    Layout.fillHeight: true
                    Layout.preferredWidth: 600
                    readOnly: true // make the TextField read-only
                    text: "Product Name"
                    font.pixelSize: 18
                    Layout.alignment: Qt.AlignVCenter
                    Connections{
                        target: backendControler
                        function onT3_productName(values){
                            productName.text = values
                        }
                    }
                }
                ComboBox {
                    id: startTimeComboBox
                    width: 500
                    model: [
                        "1/2023", "2/2023", "3/2023", "4/2023",
                        "5/2023", "6/2023", "7/2023", "8/2023",
                        "9/2023", "10/2023", "11/2023", "12/2023",
                        "1/2024", "2/2024", "3/2024", "4/2024"
                    ]
                    currentIndex: 0 // Initial selection
                    onCurrentIndexChanged: {
                        console.log("Selected start time:", currentText)
                    }
                }
                ComboBox {
                    id: endTimeComboBox
                    width: 500
                    model: [
                        "1/2023", "2/2023", "3/2023", "4/2023",
                        "5/2023", "6/2023", "7/2023", "8/2023",
                        "9/2023", "10/2023", "11/2023", "12/2023",
                        "1/2024", "2/2024", "3/2024", "4/2024"
                    ]
                    currentIndex: 0 // Initial selection
                    onCurrentIndexChanged: {
                        console.log("Selected end time:", currentText)
                    }
                }
                Button{
                    width: 100
                    Layout.fillHeight: true
                    text: "Query"
                    onClicked: {
                        // backendControler.t3_Trigger(productIdInput.text + '" "' + startTimeComboBox.currentText + '" "' + endTimeComboBox.currentText)

                        backendControler.t3_Trigger(productIdInput.text,startTimeComboBox.currentText,endTimeComboBox.currentText)
                    }
                }
            }
        }

        ChartView {
            id: chart
            Layout.fillWidth: true
            Layout.fillHeight: true
            legend.visible: true

            Connections{
                target: backendControler
                function onT3_ChartV1(values){
                    barSet1.values = values
                }
                function onT3_ChartName(values){
                    categoriesName.categories = values
                }
                function onT3_ChartV2(values){
                    barSet2.values = values
                }
            }

            BarSeries {
                name: "Sales"
                axisX: BarCategoryAxis {
                    id: categoriesName
                    categories: ["month 1", "month 2", "month 3", "month 4", "month 5"]
                }
                BarSet {
                    id: barSet1
                    label: "Selling"
                    values: [10, 15, 25, 12, 18]

                }
            }

            BarSeries {
                name: "Storage"
                BarSet {
                    id: barSet2
                    label: "Inventory "
                    values: [5, 7, 10, 8, 12]
                }
            }
        }
    }


}
