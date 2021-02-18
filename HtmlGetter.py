
if __name__ == '__main__':

    targetPath="https://www.wantedly.com/projects?type=mixed&page=1&occupation_types%5B%5D=jp__engineering&hiring_types%5B%5D=mid_career&hiring_types%5B%5D=newgrad&hiring_types%5B%5D=contract&keywords%5B%5D=%E9%9F%B3%E6%A5%BD"
    import MyFunctions.wantWantedly as ww

    ww.wantedWantedly(targetPath)

    import MyFunctions.targetPageHtmlGetter as tphg

    tphg.targetPageHtmlGetter()




