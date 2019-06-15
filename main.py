from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow,QTextEdit,QAction,QFileDialog,QApplication)
(Ui_MainWindow, QMainWindow) = uic.loadUiType('ParserUI.ui')
import web_scraping as scr
import analysis as anls
import parsing as pars
from networkx import *
import sys
import ToCSV as csv

#главный модуль. Здесь реализовано взаимодействие графического интерфейса с остальными модулями,
#реализован вывод запрошенной информации в поле для вывода, реализована проверка соединения с вк и авторизация,
#Программа была написана весной 2018. Весь функционал программы последний раз тестировался в июне 2018 года. В данный момент некоторые функции программы вероятно нуждаются в обновлении в связи
#с периодическим обновлением самого API VK разработчиками социальной сети и обновлениями пакетов
#Также для работы программы обязательно нужен токен вк для разработчика
#всю информацию по API VK можно найти по ссылке https://vk.com/dev/groups  , там же можно получить токен для работы с API

log1 = ''
pass1 = ''
user1 = '1'
group1 = '1'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #=========CONNECT panel options========================
        self.ui.butOk.clicked.connect(self.connectOK)
        self.ui.butFile.clicked.connect(self.showDialog)
        self.ui.history.setText('Программа запущена\nAPI доступен')
        global conON
        conON=False
        #=========USER panel options========================
        self.ui.butIDOk1.clicked.connect(self.userOK)
        self.ui.butInfo1.clicked.connect(self.userInfo)
        self.ui.butGr.clicked.connect(self.userGroups)
        self.ui.butFrien.clicked.connect(self.userFriends)
        self.ui.bPR1.clicked.connect(self.GetPR)
        self.ui.bGraph1.clicked.connect(self.DrawGraph)
        self.ui.butNetw1.clicked.connect(self.BuildNetworkUser)
        self.ui.bTriad1.clicked.connect(self.GetTriad)
        self.ui.bClust1.clicked.connect(self.GetClust)
        self.ui.bDom1.clicked.connect(self.GetDom)
        self.ui.bAnalys1.clicked.connect(self.GetAnalysis)
        #=========GROUP panel options========================
        self.ui.butIDOk2.clicked.connect(self.groupOK)
        self.ui.butInfo2.clicked.connect(self.groupInfo)
        self.ui.butUsers.clicked.connect(self.groupMembers)
        self.ui.butLike.clicked.connect(self.groupLikes)
        self.ui.butComm.clicked.connect(self.groupComms)
        self.ui.bPR2.clicked.connect(self.GetPR)
        self.ui.bGraph2.clicked.connect(self.DrawGraph)
        self.ui.butNetw2.clicked.connect(self.BuildNetworkGroup)
        self.ui.bTriad2.clicked.connect(self.GetTriad)
        self.ui.bClust2.clicked.connect(self.GetClust)
        self.ui.bDom2.clicked.connect(self.GetDom)
        self.ui.bAnalys2.clicked.connect(self.GetAnalysis)
        # =========FIELD panel options========================
        self.ui.bClear.clicked.connect(self.ClearField)
        self.ui.bExit.clicked.connect(self.ExitProg)
        self.ui.bSave.clicked.connect(self.SaveProg)
    #====================================================================================
    #=================================PANEL==============================================
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(fname, 'r')
        self.ui.edFile.setText(fname)
        setHistory(self, 'Открыт файл '+fname)
        global dataL
        with f:
            data = f.read()
        dataL = data.split()
        data = set(dataL)
        f.close()
        print(type(data))
        csv.UserInfoCSV(data)

    def connectOK(self):
        if ((str(self.ui.edLog.displayText()) != str('')) and (str(self.ui.edPass.displayText()) != str(''))):
            log1 = self.ui.edLog.displayText()
            pass1 = self.ui.edPass.displayText()
            setHistory(self, "Успешная авторизация " + log1)
            self.ui.lStat.setText("Статус: успешно")
            scr.OpenFirefox(log1, pass1)
            global conON
            conON=True
        else:
            self.ui.lStat.setText("Статус: неверные логин или пароль")
            setHistory(self, "Авторизация не удалась")
    #==================================================================================================================================
    #=========================================USER=====================================================================================
    def userOK(self):
        if (str(self.ui.edID1.displayText()) !=str('')):
            global user1
            self.ui.textField.setText('')
            user1 = self.ui.edID1.displayText()
            setHistory(self, 'ID получен')
            setHistory(self, 'ID пользователя: ' + user1)
        else:
            setHistory(self, 'Введен несуществующий ID')

    def userInfo(self):
        setHistory(self, 'Парсинг инфо пользователя')
        self.ui.textField.setText('')
        setText(self, pars.userInfo(user1))

    def userGroups(self):
        setHistory(self, 'Парсинг групп пользователя')
        self.ui.textField.setText('')
        setText(self, pars.userGr(user1))

    def userFriends(self):
        global conON
        if (conON == True):
            setHistory(self, 'Парсинг друзей')
            self.ui.textField.setText('')
            setText(self, 'ID пользователя\t\tИмя пользователя\n\n')
            (fio, id) = scr.GetFriends(user1)
            for i in range(len(fio)):
                stroka = str(id[i]) + "        \t" + str(fio[i]) + '\n'
                setText(self, stroka)
        else:
            setHistory(self, 'Отсутствует авторизация')
    # ================================================================================================================================
    # ======================GROUP=====================================================================================================
    def groupOK(self):
        if (str(self.ui.edID2.displayText()) != str('')):
            self.ui.textField.setText('')
            global group1
            group1 = self.ui.edID2.displayText()
            setHistory(self, 'ID получен')
            setHistory(self, 'ID cообщества: ' + group1)
        else:
            setHistory(self, 'Введен несуществующий ID')

    def groupInfo(self):
        setHistory(self, 'Парсинг инфо группы')
        self.ui.textField.setText('')
        setText(self, pars.groupInfo(group1))

    def groupMembers(self):
        global conON
        if (conON == True):
            setHistory(self, 'Парсинг участников сообщества')
            self.ui.textField.setText('')
            setText(self, 'ID пользователя\t\tИмя пользователя\n\n')
            (fio, id) = scr.GetMembers(group1)
            for i in range(len(fio)):
                stroka = str(id[i]) + "\t\t" + str(fio[i]) + '\n'
                setText(self, stroka)
        else:
            setHistory(self, 'Отсутствует авторизация')

    def groupComms(self):
        setHistory(self, 'Парсинг комментариев')
        self.ui.textField.setText('')
        (dictID, maxPost) = pars.GetComments(group1)
        setText(self, 'ID поста\tКомментарии\n\n')
        for i in range(len(maxPost)):
            stroka = (str(maxPost[i][0]) + ':\t     ', maxPost[i][1])
            setText(self, stroka)
            setText(self, '\n')
        setText(self, '\n\nID пользователя\tКомментарии\n\n')
        for i in range(len(dictID)):
            stroka = (str(dictID[i][0]) + ':\t     ', dictID[i][1])
            setText(self, stroka)
            setText(self, '\n')

    def groupLikes(self):
        setHistory(self, 'Парсиснг лайков')
        self.ui.textField.setText('')
        (dictID, maxPost) = pars.GetLikes(group1)
        setText(self, 'ID поста\tЛайки\n\n')
        for i in range(len(maxPost)):
            stroka = (str(maxPost[i][0]) + ':\t     ', maxPost[i][1])
            setText(self, stroka)
            setText(self, '\n')
        setText(self, '\n\nID пользователя\tЛайки\n\n')
        for i in range(len(dictID)):
            stroka = (str(dictID[i][0]) + ':\t     ', dictID[i][1])
            setText(self, stroka)
            setText(self, '\n')
    #===================================================================================================================================
    #======================ANALYSIS=====================================================================================================
    def DrawGraph(self):
        setHistory(self, 'Визуализация графа')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        anls.DrawG(gr)
    def GetPR(self):
        setHistory(self, 'Вычисление PageRank')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        setText(self, anls.getPagerank(gr))
    def GetAnalysis(self):
        setHistory(self, 'Анализ графа')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        setText(self, anls.GetGraphInfo(gr))
    def GetTriad(self):
        setHistory(self, 'Вычисление триадического закрытия')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        setText(self, anls.getTrian(gr))
    def GetClust(self):
        setHistory(self, 'Вычисление коэффициентов кластеризации')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        setText(self, anls.getClustering(gr))
    def GetDom(self):
        setHistory(self, 'Вычисление доминантного множества')
        self.ui.textField.setText('')
        gr = nx.read_edgelist("Edges.txt", nodetype=int)
        setText(self, anls.getDominant(gr))
    # ==================================================================================================================================
    # ======================NETWORK=====================================================================================================
    def BuildNetworkUser(self):
        pars.GetNetworkUser(user1)
        setHistory(self, 'Сеть построена')
        self.ui.textField.setText('')
        edges = []
        file = open('Edges.txt', 'rt')
        for i in file:
            edges.append(i)
        setText(self, 'Ребра графа\n\n')
        for i in edges:
            setText(self, i)
        file.close()

    def BuildNetworkGroup(self):
        pars.GetNetworkGroup(group1)
        setHistory(self, 'Сеть построена')
        self.ui.textField.setText('')
        edges = []
        file = open('Edges.txt', 'rt')
        for i in file:
            edges.append(i)
        setText(self, 'Ребра графа\n\n')
        for i in edges:
            setText(self, i)
        file.close()
    # =======================================================================================================================================
    # =============DOP FUNCTIONS=============================================================================================================
    def SaveProg(self):
        file = open('Save File.txt', 'wt')
        file.write(self.ui.textField.toPlainText())
        file.close()
        setHistory(self, 'Сохранение выполнено в Save File.txt')
    def ClearField(self):
        self.ui.textField.setText('')
    def ExitProg(self):
        sys.exit()
def setText(self, stroka):
    if (type(stroka) == tuple):
        stroka = ' '.join(map(str, stroka))
    stroka = (self.ui.textField.toPlainText()) + stroka
    self.ui.textField.setText(stroka)
def setHistory(self, stroka):
    stroka = (self.ui.history.toPlainText()) + '\n' + stroka
    self.ui.history.setText(stroka)
#==============================================================================================================================
#======================MAIN====================================================================================================
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('JustParser')
    w = MainWindow()
    w.setWindowTitle('JustParser')
    pal = w.palette()
    pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Background,
                 QtGui.QBrush(QtGui.QPixmap("Menu theme.png")))
    w.setPalette(pal)
    w.show()
    sys.exit(app.exec_())
