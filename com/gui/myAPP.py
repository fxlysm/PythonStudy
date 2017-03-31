#coding:utf-8
import wx

app =wx.App()
fram =wx.Frame(None,title ='Simeple Editor',size=(410,335))

loadButton=wx.Button(fram,label='open',pos=(225,5),size=(80,25))
SveButton=wx.Button(fram,label='save',pos=(315,5),size=(80,25))
filename =wx.TextCtrl(fram,pos=(5,5),size =(210,25))
contents =wx.TextCtrl(fram,pos=(5,35),size =(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)

fram.Show()
app.MainLoop()