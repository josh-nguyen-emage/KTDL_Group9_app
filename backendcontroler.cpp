#include "backendcontroler.h"
#include "qdebug.h"
#include <QVariantList>
#include <QFile>
#include <QProcess>
#include <QThread>

BackendControler::BackendControler(QObject *parent) : QObject(parent)
{

}

BackendControler::~BackendControler(){}

QVariantList readAndProcessFile(const QString &filePath, int index, bool skipFirstLine) {
    QVariantList resultList;

    // Open the file
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qWarning("Could not open file for reading");
        return resultList;
    }

    // Read and process each line
    QTextStream in(&file);
    in.setCodec("UTF-8");
    QString line;
    if (skipFirstLine){
        line = in.readLine();
    }
    QStringList parts;
    while (!in.atEnd()) {
        line = in.readLine();
        parts = line.split('#');
        if (parts.length() > index) {
            // Append the second substring to the result list
            resultList.append(QVariant(parts[index].trimmed()));
        }
    }

    // Close the file
    file.close();

    return resultList;
}

QVariant readFirstLine(const QString &filePath) {
    // Open the file
    QFile file(filePath);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qWarning("Could not open file for reading");
        return QVariant();
    }

    // Read the first line
    QTextStream in(&file);
    in.setCodec("UTF-8");
    QString firstLine;
    if (!in.atEnd()) {
        firstLine = in.readLine();
    }

    // Close the file
    file.close();

    // Convert the first line to QVariant and return
    return QVariant(firstLine);
}

void runPythonFile3(const QString& pythonName, const QString& argument1, const QString& argument2, const QString& argument3) {
    QProcess *process = new QProcess();
    QString workingDirectory = "D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB";
    QString pythonPath = workingDirectory + "\\" + pythonName;
    // Set working directory
    process->setWorkingDirectory(workingDirectory);

    // Connect the process signals to slots to handle output
    QObject::connect(process, &QProcess::readyReadStandardOutput, [=]() {
        qDebug() << "Python output:" << process->readAllStandardOutput();
    });

    QObject::connect(process, &QProcess::readyReadStandardError, [=]() {
        qDebug() << "Python error:" << process->readAllStandardError();
    });

    // Start the Python script with arguments
    process->start("python", QStringList() << pythonPath << argument1 << argument2 <<argument3);
    qDebug() << (QStringList() << pythonPath << argument1 << argument2);

    // Check if the process started successfully
    if (!process->waitForStarted()) {
        qDebug() << "Failed to start process";
        return;
    }

    // Wait for the process to finish
    if (!process->waitForFinished(-1)) {
        qDebug() << "Failed to finish process";
        return;
    }
}

void runPythonFile(const QString& pythonName, const QString& argument1, const QString& argument2) {
    QProcess *process = new QProcess();
    QString workingDirectory = "D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB";
    QString pythonPath = workingDirectory + "\\" + pythonName;
    // Set working directory
    process->setWorkingDirectory(workingDirectory);

    // Connect the process signals to slots to handle output
    QObject::connect(process, &QProcess::readyReadStandardOutput, [=]() {
        qDebug() << "Python output:" << process->readAllStandardOutput();
    });

    QObject::connect(process, &QProcess::readyReadStandardError, [=]() {
        qDebug() << "Python error:" << process->readAllStandardError();
    });

    // Start the Python script with arguments
    process->start("python", QStringList() << pythonPath << argument1 << argument2);

    qDebug() << (QStringList() << pythonPath << argument1 << argument2);

    // Check if the process started successfully
    if (!process->waitForStarted()) {
        qDebug() << "Failed to start process";
        return;
    }

    // Wait for the process to finish
    if (!process->waitForFinished(-1)) {
        qDebug() << "Failed to finish process";
        return;
    }
}

void runPythonFile(const QString& pythonName, const QString& arguments) {
    QProcess *process = new QProcess();
    QString workingDirectory = "D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB";
    QString pythonPath = workingDirectory + "\\" + pythonName;
    // Set working directory
    process->setWorkingDirectory(workingDirectory);

    // Connect the process signals to slots to handle output
    QObject::connect(process, &QProcess::readyReadStandardOutput, [=]() {
        qDebug() << "Python output:" << process->readAllStandardOutput();
    });

    QObject::connect(process, &QProcess::readyReadStandardError, [=]() {
        qDebug() << "Python error:" << process->readAllStandardError();
    });

    // Start the Python script with arguments
    process->start("python", QStringList() << pythonPath << arguments);
    qDebug() << ( QStringList() << pythonPath << arguments);



    // Check if the process started successfully
    if (!process->waitForStarted()) {
        qDebug() << "Failed to start process";
        return;
    }

    // Wait for the process to finish
    if (!process->waitForFinished(-1)) {
        qDebug() << "Failed to finish process";
        return;
    }
}

void BackendControler::t1_Trigger(const QString& scriptPath)
{
    runPythonFile("ProductSuggestions.py",scriptPath);
    QVariant productName = readFirstLine("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductSuggestions.txt");
    emit t1_userName(productName);
    QVariantList name = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductSuggestions.txt",1,true);
    QVariantList brand = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductSuggestions.txt",2,true);
    QVariantList cate = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductSuggestions.txt",3,true);
    QVariantList rating = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductSuggestions.txt",4,true);
    emit t1_Table(name,brand,cate,rating);
}

void BackendControler::t2_Trigger(const QString& scriptPath)
{
    runPythonFile("CustomerDemand.py",scriptPath);
    QVariantList name = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\CustomerDemand.txt",0,false);
    QVariantList v1 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\CustomerDemand.txt",1,false);
    QVariantList v2 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\CustomerDemand.txt",2,false);
    emit t2_Table(name,v1,v2);
}

void BackendControler::t3_Trigger(const QString& value1, const QString& value2, const QString& value3)
{
    runPythonFile3("InventoryManagment.py",value1,value2,value3);
    QVariant productName = readFirstLine("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\InventoryManagment.txt");
    emit t3_productName(productName);
    QVariantList chart = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\InventoryManagment.txt",0,true);
    emit t3_ChartName(chart);
    chart = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\InventoryManagment.txt",1,true);
    emit t3_ChartV1(chart);
    chart = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\InventoryManagment.txt",2,true);
    emit t3_ChartV2(chart);

    qDebug() << productName;
}

void BackendControler::t4_Trigger(const QString& scriptPath)
{
    runPythonFile("ProductReview.py",scriptPath);
    QVariant productName = readFirstLine("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductReview.txt");
    emit t4_productName(productName);
    QVariantList name = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductReview.txt",0,true);
    QVariantList v1 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductReview.txt",1,true);
    QVariantList v2 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\ProductReview.txt",2,true);
    emit t4_tableView(name,v1,v2);
}

void BackendControler::t5_Trigger(const QString& scriptPath)
{
    runPythonFile("SellerReviews.py",scriptPath);
    QVariantList list1 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\SellerReviews.txt",0,false);
    QVariantList list2 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\SellerReviews.txt",1,false);
    QVariantList list3 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\SellerReviews.txt",2,false);
    QVariantList list4 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\SellerReviews.txt",3,false);

    QVariantList combine;
    combine.append(list1[0]);
    combine.append(list2[0]);
    combine.append(list3[0]);
    combine.append(list4[0]);
    emit t5_chart(combine);
}

QString convertPromotion(QString input){
    QMap<QString, QString> promotionsMap;
    QStringList promotions = {
        "promotions/1-A#Super Sale 1/1 2023",
        "promotions/2-A#Super Sale 2/2 2023",
        "promotions/3-A#Super Sale 3/3 2023",
        "promotions/4-A#Super Sale 4/4 2023",
        "promotions/5-A#Super Sale 5/5 2023",
        "promotions/6-A#Super Sale 6/6 2023",
        "promotions/7-A#Super Sale 7/7 2023",
        "promotions/8-A#Super Sale 8/8 2023",
        "promotions/9-A#Super Sale 9/9 2023",
        "promotions/10-A#Super Sale 10/10 2023",
        "promotions/11-A#Super Sale 11/11 2023",
        "promotions/12-A#Super Sale 12/12 2023",
        "promotions/13-A#Super Sale 1/1 2024",
        "promotions/14-A#Super Sale 2/2 2024",
        "promotions/15-A#Super Sale 3/3 2024",
        "promotions/16-A#Super Sale 4/4 2024"
    };

    // Populate the map with the strings
    for (const QString& promo : promotions) {
        QString key = promo.split('#').last(); // Get the left substring before #
        promotionsMap[key] = promo.split('#').first();
    }

    if (promotionsMap.contains(input)) {
        // Retrieve the corresponding string from the map and return its left substring
        return promotionsMap[input];
    } else {
        // Return an empty string if the input string is not found
        return QString();
    }
}


void BackendControler::t6_Trigger(const QString& value1, const QString& value2)
{
    runPythonFile("PromotionProgram.py", convertPromotion(value2), value1);
    QVariant productName = readFirstLine("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\PromotionProgram.txt");
    emit t6_productName(productName);
    QVariantList list1 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\PromotionProgram.txt",0,true);
    QVariantList list2 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\PromotionProgram.txt",1,true);
    QVariantList list3 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\PromotionProgram.txt",2,true);
    QVariantList list4 = readAndProcessFile("D:\\Download\\KTDL_Group9_app-main\\KTDL_Group9_app-main\\RavenDB\\PromotionProgram.txt",3,true);

    QVariantList combine;
    combine.append(list1[0]);
    combine.append(list2[0]);
    combine.append(list3[0]);
    combine.append(list4[0]);
    emit t6_chart(combine);
}

QString BackendControler::exampleFunction(const QString& scriptPath)
{
    qDebug() << "Trigger" ;
    // --- Tab 1
    QVariant productName = readFirstLine("C:\\Users\\Admin\\Desktop\\3 - study\\ProductSuggestions.txt");
    emit t1_userName(productName);
    QVariantList name = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductSuggestions.txt",1,true);
    QVariantList brand = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductSuggestions.txt",2,true);
    QVariantList cate = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductSuggestions.txt",3,true);
    QVariantList rating = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductSuggestions.txt",4,true);
    emit t1_Table(name,brand,cate,rating);
    // --- Tab 2
    name = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\CustomerDemand.txt",0,false);
    QVariantList v1 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\CustomerDemand.txt",1,false);
    QVariantList v2 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\CustomerDemand.txt",2,false);
    emit t2_Table(name,v1,v2);
    // --- Tab 3
    productName = readFirstLine("C:\\Users\\Admin\\Desktop\\3 - study\\InventoryManagment.txt");
    emit t3_productName(productName);
    QVariantList chart = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\InventoryManagment.txt",0,true);
    emit t3_ChartName(chart);
    chart = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\InventoryManagment.txt",1,true);
    emit t3_ChartV1(chart);
    chart = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\InventoryManagment.txt",2,true);
    emit t3_ChartV2(chart);
    // --- Tab 4
    productName = readFirstLine("C:\\Users\\Admin\\Desktop\\3 - study\\ProductReview.txt");
    emit t4_productName(productName);
    name = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductReview.txt",0,true);
    v1 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductReview.txt",1,true);
    v2 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\ProductReview.txt",2,true);
    emit t4_tableView(name,v1,v2);
    // --- Tab 5
    QVariantList list1 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\SellerReviews.txt",0,false);
    QVariantList list2 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\SellerReviews.txt",1,false);
    QVariantList list3 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\SellerReviews.txt",2,false);
    QVariantList list4 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\SellerReviews.txt",3,false);

    QVariantList combine;
    combine.append(list1[0]);
    combine.append(list2[0]);
    combine.append(list3[0]);
    combine.append(list4[0]);
    emit t5_chart(combine);
    // --- Tab 6
    QVariantList promotionList = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\AllPromotions.txt", 1, false);
    emit allPromotionsUpdated(promotionList);
    productName = readFirstLine("C:\\Users\\Admin\\Desktop\\3 - study\\PromotionProgram.txt");
    emit t6_productName(productName);
    list1 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\PromotionProgram.txt",0,true);
    list2 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\PromotionProgram.txt",1,true);
    list3 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\PromotionProgram.txt",2,true);
    list4 = readAndProcessFile("C:\\Users\\Admin\\Desktop\\3 - study\\PromotionProgram.txt",3,true);

    combine.clear();
    combine.append(list1[0]);
    combine.append(list2[0]);
    combine.append(list3[0]);
    combine.append(list4[0]);
    emit t6_chart(combine);
    // --- --- ---
    return "Everything work, for now";
}
