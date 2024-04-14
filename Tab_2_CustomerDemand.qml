import QtQuick 2.15
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.15

Rectangle {
    width: 400
    height: 300

    ColumnLayout {
        anchors.fill: parent

        // Dropdown selection
        ComboBox {
            id: comboBox
            Layout.fillWidth: true
            model: ["1/2023", "2/2023", "3/2023", "4/2023", "1/2024"]
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            onCurrentIndexChanged: {
                console.log("Selected option:", currentText)
                backendControler.t2_Trigger(currentText)
            }
            implicitHeight: 50

            Connections{
                target: backendControler
                function onT2_Table(name, sale, ratio) {
                    // Clear all current elements from the TableView
                    tableView.model.clear();

                    // Add input data to the TableView
                    for (var i = 0; i < name.length; i++) {
                        var newElement = {
                            category: name[i],
                            soldQuantity: sale[i],
                            totalQuantity: ratio[i]
                        };
                        tableView.model.append(newElement);
                    }
                }
            }
        }

        // Table view
        TableView {
            id: tableView
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: ListModel {

            }

            TableViewColumn {
                role: "category"
                title: "Category"
                width: tableView.width * 0.7 // Adjust width as needed
            }

            TableViewColumn {
                role: "soldQuantity"
                title: "Tổng lượng bán ra"
                width: tableView.width * 0.2 // Adjust width as needed
            }

            TableViewColumn {
                role: "totalQuantity"
                title: "Tỉ lệ bán ra"
                width: tableView.width * 0.1 // Adjust width as needed
            }
            itemDelegate: Item {
                height: 50
                Text {
                    x: 10
                  anchors.verticalCenter: parent.verticalCenter
                  color: "black"
                  elide: styleData.elideMode
                  text: styleData.value
                  font.pixelSize: 18
                }
             }

            rowDelegate: Rectangle {
               height: 30
               SystemPalette {
                  id: myPalette;
                  colorGroup: SystemPalette.Active
               }
               color: {
                  var baseColor = styleData.alternate?myPalette.alternateBase:myPalette.base
                  return styleData.selected?myPalette.highlight:baseColor
               }
            }

            headerDelegate: Rectangle {
                height: textItem.implicitHeight * 1.2
                width: textItem.implicitWidth
                color: "lightgrey"
                Text {
                    id: textItem
                    anchors.fill: parent
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: styleData.textAlignment
                    anchors.leftMargin: 12
                    text: styleData.value
                    elide: Text.ElideRight
                    color: "black"
                    font.pixelSize: 18
                    renderType: Text.NativeRendering

                }
                Rectangle {
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 1
                    anchors.topMargin: 1
                    width: 1
                    color: "black"
                    border.color: "black"
                }
                Rectangle {
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: 1
                    color: "black"
                    border.color: "black"
                }
            }
        }

    }
}
