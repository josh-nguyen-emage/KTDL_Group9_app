import QtQuick 2.15
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.15

Rectangle {
    width: 400
    height: 300

    ColumnLayout {
        anchors.fill: parent

        RowLayout {
            Layout.fillWidth: true
            Layout.preferredHeight: 10

            TextField {
                id: inputField
                Layout.fillHeight: true
                Layout.preferredWidth: 750
                placeholderText: "Category ID"
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.pixelSize: 18
                onTextChanged: {
                    // Handle text changed event
                    console.log("Input text changed:", text)
                }
            }

            TextField {
                id: productName
                Layout.fillHeight: true
                Layout.preferredWidth: 650
                readOnly: true // make the TextField read-only
                text: "Product Name"
                font.pixelSize: 18
                Layout.alignment: Qt.AlignVCenter

                Connections{
                    target: backendControler
                    function onT4_productName(values){
                        productName.text = values
                    }
                }
            }

            Button{
                Layout.fillHeight: true
                Layout.fillWidth: true
                text: "Query"
                onClicked: {
                    backendControler.t4_Trigger(inputField.text)
                }
            }
        }

        // Table view
        TableView {
            id: tableView
            Layout.fillWidth: true
            Layout.fillHeight: true
            Connections{
                target: backendControler
                function onT4_tableView(name, v1, v2) {
                    // Clear all current elements from the TableView
                    tableView.model.clear();

                    // Add input data to the TableView
                    for (var i = 0; i < name.length; i++) {
                        var newElement = {
                            productName: name[i],
                            numberOfReviews: v1[i],
                            averageRating: v2[i]
                        };
                        tableView.model.append(newElement);
                    }
                }
            }
            model: ListModel {
            }

            TableViewColumn {
                role: "productName"
                title: "Tên sản phẩm"
                width: tableView.width * 0.8 // Adjust width as needed
            }

            TableViewColumn {
                role: "numberOfReviews"
                title: "Số lượt đánh giá"
                width: tableView.width * 0.1 // Adjust width as needed
            }

            TableViewColumn {
                role: "averageRating"
                title: "Điểm trung bình"
                width: tableView.width * 0.1 // Adjust width as needed
            }
            itemDelegate: Item {
                height: 50
                width: parent.width
                Text {
                  x: 10
                  anchors.verticalCenter: parent.verticalCenter
                  color: "black"
                  elide: styleData.elideMode
                  text: styleData.value
                  font.pixelSize: 18
                  clip: true
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
