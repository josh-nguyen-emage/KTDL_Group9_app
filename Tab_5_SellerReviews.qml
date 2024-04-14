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
            Layout.preferredHeight: 50
            // Text box
            TextField {
                id: textField
                Layout.fillWidth: true
                placeholderText: "Enter Seller ID"
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.pixelSize: 18
                Layout.preferredHeight: 50
            }
            TextField {
                id: sellerName
                Layout.fillWidth: true
                placeholderText: "seller name"
                readOnly: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.pixelSize: 18
                Layout.preferredHeight: 50
            }
            Connections{
                target: backendControler
                function onT5_chart(values){
                    sellerName.text = values[0]
                    bar1.values = [values[1],values[2], values[3]]
                }
            }

            Button{
                Layout.preferredWidth: 100
                text: "Query"
                onClicked: {
                    backendControler.t5_Trigger(textField.text)
                }
            }
        }


        ChartView {
            id: chart
            legend.visible: true
            Layout.fillWidth: true
            Layout.fillHeight: true

            BarSeries {
                name: "Sales"
                axisX: BarCategoryAxis {
                    categories: ["Giao hàng", "Phản hồi của gian hàng", "Tỷ lệ giao hàng đúng hẹn"]
                }
                BarSet {
                    id: bar1
                    label: "Chất lượng"
                    values: [20,50,100]
                }
            }
        }
    }
}
