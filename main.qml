import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 1000
    height: 480
    visible: true
    title: qsTr("KTDL_Group9")
    color: "#E5DDC5"
    Rectangle{
        id: outerRectangle
        width: parent.width/2
        height: parent.height
        color: "#FA7070"
        Button {
            id: runButton
            property int buttonStatus: 1
            width: 300
            height: 100
            text: "Press This"
            font.pixelSize: 24
            anchors.centerIn: parent

            onClicked: {
                text = backendControler.exampleFunction("Some String")
                parent.color = "#FF9800"
            }
        }
    }

    Rectangle{
        width: parent.width/2
        height: parent.height
        anchors.right: parent.right
        BarChart{
            anchors.fill: parent
        }
    }
}
