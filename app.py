
from Layoute.AnalyseDep import analyseDepLayoute
from Layoute.natureCulture import natureCultureLayout
from Layoute.map import mapLayout
from Layoute.MeilleursVentes import MeilleursVentesLayoute
from Layoute.page import pageLayoute

def main():
    navbar , start_date ,end_date ,selectedata =pageLayoute()
    if navbar =="Caracteristique":
        natureCultureLayout(selectedata,start_date,end_date)      
    if navbar =="Map":
        mapLayout(selectedata,start_date,end_date)
    if navbar =="Meilleurs Ventes":
        MeilleursVentesLayoute(selectedata,start_date,end_date)
    if navbar =="Analyse sur un departement":
        analyseDepLayoute(selectedata,start_date,end_date)
        
if __name__=="__main__":
    main()
    
    
        