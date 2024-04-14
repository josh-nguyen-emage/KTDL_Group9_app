import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 1500
    height: 800
    visible: true
    title: qsTr("KTDL_Group9")
    color: "#35374B"
    Rectangle{
        id: outerRectangle
        width: parent.width
        height: parent.height
        color: "#35374B"
        TabView{
            anchors.fill: parent
        }

        // Timer{
        //     interval: 1000
        //     repeat: true
        //     running: true
        //     onTriggered: {
        //         backendControler.exampleFunction("abc")
        //     }
        // }

    }
}
