#Otomasyon
import sys
import typing
from PyQt5 import QtCore, QtWidgets as qtw
from PyQt5.QtWidgets import QWidget,QTableWidgetItem
from ogrencikayit import Ui_MainWindow


class Uygulama(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()  #Oluşturduğumuz label,buton vs eklentileri çağırabilmek için kullanırız.
        self.ui.setupUi(self)  ##??

        self.ui.dogumyeri.addItems(["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"])
        self.ui.bolum.addItems(["Hemşirelik","Tıp","Mühendsilik"])
        self.ui.kayitekle.clicked.connect(self.kayitekle)
        self.ui.kayitsil.clicked.connect(self.kayitsil)
    def kayitekle(self):
        ad=self.ui.ad.text()
        soyad=self.ui.soyad.text()
        tc=self.ui.tc.text()

        cinsiyetgrup=self.ui.cinsiyet.findChildren(qtw.QRadioButton) #cinsiyetgrup isminde bir değişken oluşturyudk.
        for i in cinsiyetgrup: # for döngüsü ile seçili olanı bylmak istiyoruz. 
            if i.isChecked(): # Eğer seçili var ise onun textini getirmesini istiyoruz.
                cins=i.text()
        eturu=self.ui.egitimturu.findChildren(qtw.QRadioButton)
        for i in eturu:
            if i.isChecked():
                etur=i.text()
        dogumyer=self.ui.dogumyeri.currentText() ##comboboxtan güncel yazılı olan değeri alırız.
        bolumu=self.ui.bolum.currentText()
        dtarih=self.ui.dogumtarihi.selectedDate()
        ydtarih=dtarih.toString("dd-MM-yyyy")

        
       ##  print(ad,soyad,tc,cins,etur,dogumyer,bolumu,ydtarih)

        satırsayisi=self.ui.kaytekrani.rowCount()-1 ##ò toplamda kaç satırımız var ise onun indeks numarasını verir.
        
        self.ui.kaytekrani.setItem(satırsayisi,0,QTableWidgetItem(ad))
        self.ui.kaytekrani.setItem(satırsayisi,1,QTableWidgetItem(soyad))
        self.ui.kaytekrani.setItem(satırsayisi,2,QTableWidgetItem(tc))
        self.ui.kaytekrani.setItem(satırsayisi,3,QTableWidgetItem(cins))
        self.ui.kaytekrani.setItem(satırsayisi,4,QTableWidgetItem(etur))
        self.ui.kaytekrani.setItem(satırsayisi,5,QTableWidgetItem(dogumyer))
        self.ui.kaytekrani.setItem(satırsayisi,6,QTableWidgetItem(bolumu))
        self.ui.kaytekrani.setItem(satırsayisi,7,QTableWidgetItem(ydtarih))

        self.ui.kaytekrani.insertRow(satırsayisi+1) # satır sayısnı bir arttıracak ve satır ekleyecek.
        # daha sorna üsttei kodda satır sayısını 2-1=1 olacak ve o indekse ekleme yapacak. 
    def kayitsil(self):
        secili=self.ui.kaytekrani.currentRow()
        self.ui.kaytekrani.removeRow(secili)




 


def app():  # Ana iskelet, tasarımın açılması için yazarız.
    app=qtw.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec_())
app()

