import collections
from time import sleep

from PyQt5.QtWidgets import  *

from NewPlayAgain import *
from QtTable import Ui_MainWindow
from Win import Ui_WinDialog
import numpy as np
import sys

class WinDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_WinDialog()
        self.ui.setupUi(self)
        self.winner = parent.currentPlayer
        if self.winner != "no one":
            self.ui.label.setText(f"The winner is: {self.winner}")
        else:
            self.ui.label.setText(f"Game Over")
        self.ui.pushButton.clicked.connect(self.hide)

class Dialog(QDialog):
    def __init__(self, score, first_player_name,  second_player_name, parent = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.output = "0"
        print(score)
        try :
            self.ui.lblFirstPlayer.setText(f"Player named win {first_player_name}: {score[first_player_name]} times")
        except:
            pass
        try:
            self.ui.lblSecondPlayer.setText(f"Player named win {second_player_name}:  {score[second_player_name]} times")
        except:
            pass
        self.ui.buttonBox.accepted.connect(self.Newaccept)
        self.ui.buttonBox.rejected.connect(self.Newreject)

    def Newaccept(self):
        self.output = '1'
        super(Dialog, self).accept()

    def Newreject(self):
        self.output = '0'
        super(Dialog, self).reject()

    def get_output(self):
       return self.output

class MainWindow(QMainWindow):
    def __init__(self, first_player_name, second_player_name = "second player", parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myarray = board
        self.value = "0"
        self.currentPlayer = first_player_name
        self.second_player_name = second_player_name
        self.first_player_name = first_player_name
        self.win = 0
        self.ui.tableWidget.cellClicked.connect(self.on_click)
        self.tor = 'o'
        self.winner = ''



    def checkValue(self, row, column):
        l = np.array([self.tor, self.tor, self.tor])
        if self.is_winner(l):
            self.winner = self.currentPlayer

            return 1
        if self.game_over_without_win():
            return 2

    def game_over_without_win(self):
        if '' not in self.myarray:
            return True
        else:
            return False
    def get_cell_item(self, row, column):
        return self.myarray[row, column]

    def setValue(self, row, column, value):
        if self.win == 0:
            if self.get_cell_item(row,column) == '':
                value = self.getItem()
                self.tor = value
                item = QTableWidgetItem(value)
                self.ui.tableWidget.setItem(row,column, item)
                self.myarray[row,column] = value
                return True

    def getItem(self):
        if self.tor == 'x':
            self.currentPlayer = self.second_player_name
            return 'o'
        else:
            self.currentPlayer = self.first_player_name
            return 'x'
    def is_winner(self, l):
        for i in range (0, 3):
            if np.all(self.myarray[i] == l) or np.all((self.myarray[:, i]) == (l.reshape(3, 1))):
                return True
        if np.all(self.myarray[(0, 1, 2), (0, 1, 2)] == l) or np.all (self.myarray[(0, 1, 2), (2, 1, 0)] == l):
            return True
        return False

    def on_click(self,row, column):
        if self.setValue(row,column,'x'):
            result = self.checkValue(row,column)
            if result == 1:
                self.win = 1
                self.ui.tableWidget.setEnabled(False)
                win = WinDialog(self)
                win.show()
                return
            if result == 2:
                self.ui.tableWidget.setEnabled(False)
                self.currentPlayer = "no one"
                win = WinDialog(self)
                win.show()
                return



    def clear_board(self):
        self.myarray[:] = ''
        for i in range (0, 3):
            for j in range (0, 3):
                self.ui.tableWidget.setItem(i,j, '')
class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)
    def game_over(self, win, name):
        if win:
            self.score[name]+=1

class BasePlayer:
    def __init__(self, score_keeper):
        self.score = score_keeper
    def game_over(self, win):
        self.score.game_over(win, self.name)

class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper, name, my_tag):
        super().__init__(score_keeper)
        self.name = name
        self.my_tag = my_tag




board = np.chararray((3, 3),unicode=True)
app = QApplication(sys.argv)
newapp = QApplication(sys.argv)
first_player_name = "myName"
score_keeper = Score()
second_player_name = "second player"
h =  HumanPlayer(score_keeper, first_player_name, 'x')
second =  HumanPlayer(score_keeper, second_player_name, 'o')
while True:


    board[:] = ''
    w = MainWindow(first_player_name, second_player_name)
    w.show()
    app.exec_()
    if w.winner == first_player_name:
        h.game_over(True)
    else:
        if w.winner == second_player_name:
            second.game_over(True)

    neww = Dialog(dict(second.score.score) , first_player_name, second_player_name)
    neww.show()
    newapp.exec_()
    if neww.get_output() != "1":
        break;








