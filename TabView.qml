import QtQuick 2.15
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

Item {
    TabView {
        anchors.fill: parent

        style: TabViewStyle {
            tab: Rectangle {
                implicitWidth: 1500/6 // Adjust width as needed
                implicitHeight: 50 // Adjust height as needed
                color: styleData.selected ? "#35374B" : "#344955"
                border.color: "black"
                Text {
                    id: text
                    anchors.centerIn: parent
                    text: styleData.title
                    font.pixelSize: 20
                    color: styleData.selected ? "white" : "#76ABAE"
                }
            }
        }

        Tab {
            title: "Gợi ý sản phẩm"
            Tab_1_ProductSuggestions{
                anchors.fill: parent
            }
        }
        Tab {
            title: "Nhu cầu tiêu dùng"
            Tab_2_CustomerDemand{
                anchors.fill: parent
            }
        }
        Tab {
            title: "Quản lý hàng tồn"
            Tab_3_InventoryManagment{
                anchors.fill: parent
            }
        }
        Tab {
            title: "Đánh giá sản phẩm"
            Tab_4_ProductReview{
                anchors.fill: parent
            }
        }
        Tab {
            title: "Đánh giá nhà bán hàng"
            Tab_5_SellerReviews{
                anchors.fill: parent
            }
        }
        Tab {
            title: "Chương trình khuyến mãi"
            Tab_6_PromotionProgram{
                anchors.fill: parent
            }
        }
    }
}
