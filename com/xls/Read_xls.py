#coding:utf-8
import  xlrd

def main():

    xlsfile=xlrd.open_workbook("testxls.xls")

    try:
        mysheet=xlsfile.sheet_by_name("GDP预测")

    except:
        print 'no sheet in %s named GDP预测'

        return
    #total rows nd cols
    print '%d rows,%d cols'%(mysheet.nrows,mysheet.ncols)


if __name__ =='__main__':
    main()