import  MyFunctions.ElementInspector as ei


import MyFunctions.Janomer as mjnm

if __name__ == '__main__':
    ei.getElementsFromHtml()
    ei.sortCsvData()


    mjnm.getAllTokenAndSave()
    mjnm.RemoveEnter()

    mjnm.searchModernTech()