# -*- coding: iso-8859-15 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: gTurbSim.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid

# Custom source
from base4wdr import *

# Window functions

ID_TEXT = 10000
ID_BUTTON = 10001
ID_TEXTCTRL = 10002
ID_RADIOBUTTON = 10003
ID_COMBO = 10004

def main( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.BoxSizer( wx.HORIZONTAL )
    
    item2 = wx.BoxSizer( wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Welcome to the TurbSim GUI!", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetFont( wx.Font( 14, wx.ROMAN, wx.NORMAL, wx.BOLD ) )
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item4 = wx.BoxSizer( wx.HORIZONTAL )
    
    item5 = wx.Button( parent, ID_BUTTON, "Run TurbSim", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "btn_run" )
    item4.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = mTextCtrl( parent, ID_TEXTCTRL, "1", wx.DefaultPosition, [60,-1], 0 )
    item6.SetName( "inp_iterations" )
    item4.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "iteration(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = wx.RadioButton( parent, ID_RADIOBUTTON, "Use pyTurbSim", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetValue( True )
    item8.SetName( "rdo_pyturbsim" )
    item2.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.RadioButton( parent, ID_RADIOBUTTON, "Use TurbSim", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "rdo_turbsim" )
    item2.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.Add( item2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item11 = wx.StaticBox( parent, -1, "Configuration" )
    item10 = wx.StaticBoxSizer( item11, wx.VERTICAL )
    
    item12 = wx.BoxSizer( wx.HORIZONTAL )
    
    item13 = wx.StaticText( parent, ID_TEXT, "Current File:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = mComboBox( parent, ID_COMBO, "", wx.DefaultPosition, [260,-1], 
        ["-- Default Wind Config --","-- Default IEC (Wind) Config --","-- Default Tidal (Hydro) Config --","-- Default River (Hydro) Config --"] , wx.CB_DROPDOWN )
    item14.SetName( "inp_inputfile" )
    item12.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.Button( parent, ID_BUTTON, "...", wx.DefaultPosition, [33,-1], 0 )
    item15.SetName( "btn_inputfile" )
    item12.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10.Add( item12, 0, wx.ALIGN_CENTER, 5 )

    item1.Add( item10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANEL = 10005

def GridSetup( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.BoxSizer( wx.HORIZONTAL )
    parent.ColSplit00 = item1
    
    item2 = wx.BoxSizer( wx.VERTICAL )
    
    item3 = wx.BoxSizer( wx.HORIZONTAL )
    
    item5 = wx.StaticBox( parent, -1, "Y-grid parameters" )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    parent.TopVsizer = item4
    
    item6 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item7 = wx.StaticText( parent, ID_TEXT, "Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item8.SetName( "inp_width" )
    item6.Add( item8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "N-points:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "inp_ny" )
    item6.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "DY:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item12.SetName( "inp_dy" )
    item6.Add( item12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item4.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.StaticBox( parent, -1, "Z-grid parameters" )
    item13 = wx.StaticBoxSizer( item14, wx.VERTICAL )
    
    item15 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item16 = wx.StaticText( parent, ID_TEXT, "Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item17.SetName( "inp_height" )
    item15.Add( item17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18 = wx.StaticText( parent, ID_TEXT, "N-points:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item19.SetName( "inp_nz" )
    item15.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20 = wx.StaticText( parent, ID_TEXT, "DZ:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "inp_dz" )
    item15.Add( item21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item13.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL, 15 )

    item22 = wx.BoxSizer( wx.HORIZONTAL )
    
    item24 = wx.StaticBox( parent, -1, "Time parameters" )
    item23 = wx.StaticBoxSizer( item24, wx.VERTICAL )
    
    item25 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item26 = wx.StaticText( parent, ID_TEXT, "Simulation Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item27 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item27.SetName( "inp_time" )
    item25.Add( item27, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item28 = wx.StaticText( parent, ID_TEXT, "N-timesteps", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item28, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item29 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item29.SetName( "inp_nt" )
    item25.Add( item29, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item30 = wx.StaticText( parent, ID_TEXT, "DT:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item30, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item31 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item31.SetName( "inp_dt" )
    item25.Add( item31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item23.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22.Add( item23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item33 = wx.StaticText( parent, ID_TEXT, "Hub Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item32.Add( item33, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item34 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item34.SetName( "inp_hubheight" )
    item32.Add( item34, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22.Add( item32, 0, wx.ALL, 5 )

    item2.Add( item22, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item35 = wx.BoxSizer( wx.VERTICAL )
    
    item36 = wx.Panel( parent, ID_PANEL, wx.DefaultPosition, [180,230], 0 )
    item36.SetName( "pnl_grid" )
    item35.Add( item36, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 30 )

    item1.Add( item35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item37 = wx.BoxSizer( wx.HORIZONTAL )
    
    item38 = wx.Button( parent, ID_BUTTON, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item38.SetName( "btn_cancel" )
    item37.Add( item38, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item39 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.SetName( "btn_ok" )
    item37.Add( item39, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item37, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CHOICE = 10006
ID_LINE = 10007
ID_CHECKBOX = 10008

def turbSetup( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.BoxSizer( wx.HORIZONTAL )
    
    item2 = wx.BoxSizer( wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Select turbulence model:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["SMOOTH","IECKAI","IECVKM","GP_LLJ","NWTCUP","WF_UPW","WF_07D","WF_14D","TIDAL","RIVER"] , 0 )
    item4.SetName( "cho_turbmodel" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.StaticBox( parent, -1, "Base Parameters" )
    item6 = wx.StaticBoxSizer( item7, wx.VERTICAL )
    
    item8 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "u*", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "inp_ustar" )
    item8.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Ri", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item12 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item12.SetName( "inp_Ri" )
    item8.Add( item12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "Z0", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item14.SetName( "inp_z0" )
    item8.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "ZI", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item16 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item16.SetName( "inp_zi" )
    item8.Add( item16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item6.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.StaticBox( parent, -1, "Reynold's Stress" )
    item17 = wx.StaticBoxSizer( item18, wx.VERTICAL )
    
    item19 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item20 = wx.StaticText( parent, ID_TEXT, "u'w'", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "inp_upwp" )
    item19.Add( item21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22 = wx.StaticText( parent, ID_TEXT, "v'w'", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item23 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item23.SetName( "inp_vpwp" )
    item19.Add( item23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item24 = wx.StaticText( parent, ID_TEXT, "u'v'", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item25 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item25.SetName( "inp_upvp" )
    item19.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item17.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.Add( item17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item26 = wx.BoxSizer( wx.VERTICAL )
    
    item28 = wx.StaticBox( parent, -1, "IEC parameters" )
    item27 = wx.StaticBoxSizer( item28, wx.VERTICAL )
    
    item29 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item30 = wx.StaticText( parent, ID_TEXT, "IEC Wind Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item30, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item31 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["NTM","ETM","EWM1","EWM50"] , 0 )
    item31.SetName( "cho_iecwindtype" )
    item29.Add( item31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = wx.StaticText( parent, ID_TEXT, "Turbine Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item32, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item33 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["1","2","3","--"] , 0 )
    item33.SetName( "cho_iecclass" )
    item29.Add( item33, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item34 = wx.StaticText( parent, ID_TEXT, "Turbulence Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item34.SetToolTip( wx.ToolTip("Only used for extreme IEC windtypes.") )
    item29.Add( item34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item35 = mComboBox( parent, ID_COMBO, "", wx.DefaultPosition, [100,-1], 
        ["A","B","C"] , wx.CB_DROPDOWN )
    item35.SetName( "inp_iecturbc" )
    item29.Add( item35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item36 = wx.StaticText( parent, ID_TEXT, "ETMc:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item36, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item37 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item37.SetName( "inp_etmc" )
    item29.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item38 = wx.StaticText( parent, ID_TEXT, "IEC Standard:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item29.Add( item38, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item39 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["1","1-ED2","1-ED3","2","3"] , 0 )
    item39.SetName( "cho_iecstandard" )
    item29.Add( item39, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item27.Add( item29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item26.Add( item27, 0, wx.ALL, 5 )

    item41 = wx.StaticBox( parent, -1, "Coherence parameters" )
    item40 = wx.StaticBoxSizer( item41, wx.VERTICAL )
    
    item42 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item43 = wx.StaticText( parent, ID_TEXT, "CohExp", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item43, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item44 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item44.SetName( "inp_cohexp" )
    item42.Add( item44, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item42.Add( [ 4, 20 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item42.Add( [ 20, 20 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item45 = wx.StaticText( parent, ID_TEXT, "U: a)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item45, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item46 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item46.SetName( "inp_cohUa" )
    item42.Add( item46, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item47 = wx.StaticText( parent, ID_TEXT, "b)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item47, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item48 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item48.SetName( "inp_cohUb" )
    item42.Add( item48, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item49 = wx.StaticText( parent, ID_TEXT, "V: a)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item49, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item50 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item50.SetName( "inp_cohVa" )
    item42.Add( item50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item51 = wx.StaticText( parent, ID_TEXT, "b)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item51, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item52 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item52.SetName( "inp_cohVb" )
    item42.Add( item52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item53 = wx.StaticText( parent, ID_TEXT, "W: a)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item53, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item54 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item54.SetName( "inp_cohWa" )
    item42.Add( item54, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item55 = wx.StaticText( parent, ID_TEXT, "b)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item55, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item56 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [70,-1], 0 )
    item56.SetName( "inp_cohWb" )
    item42.Add( item56, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item40.Add( item42, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item26.Add( item40, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item26, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item57 = wx.BoxSizer( wx.HORIZONTAL )
    
    item58 = mCheckBox( parent, ID_CHECKBOX, "Add KH Billows", wx.DefaultPosition, wx.DefaultSize, 0 )
    item58.SetName( "inp_addkh" )
    item57.Add( item58, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item59 = wx.Button( parent, ID_BUTTON, "settings...", wx.DefaultPosition, wx.DefaultSize, 0 )
    item59.SetName( "btn_khconfig" )
    item57.Add( item59, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item57, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item60 = wx.BoxSizer( wx.HORIZONTAL )
    
    item61 = wx.Button( parent, ID_BUTTON, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item61.SetName( "btn_cancel" )
    item60.Add( item61, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item62 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item62.SetDefault()
    item62.SetName( "btn_ok" )
    item60.Add( item62, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item60, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def profSetup( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.BoxSizer( wx.HORIZONTAL )
    
    item2 = wx.BoxSizer( wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Select the profile model:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["JET","LOG","POWER","IEC","H2O Log"] , 0 )
    item4.SetName( "cho_profmodel" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Profile parameters:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = wx.StaticText( parent, ID_TEXT, "Ref. Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item9.SetName( "inp_refheight" )
    item7.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Ref. Velocity:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item11.SetName( "inp_refvel" )
    item7.Add( item11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "u*", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item13 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item13.SetName( "inp_ustar" )
    item7.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Power-Law Exp.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item15.SetName( "inp_plexp" )
    item7.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item16 = wx.StaticText( parent, ID_TEXT, "Jet Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item17.SetName( "inp_zjet" )
    item7.Add( item17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18 = wx.StaticText( parent, ID_TEXT, "H Flow Ang:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item19.SetName( "inp_hflowang" )
    item7.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20 = wx.StaticText( parent, ID_TEXT, "V Flow Ang:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item21.SetName( "inp_vflowang" )
    item7.Add( item21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22 = wx.Panel( parent, ID_PANEL, wx.DefaultPosition, [200,310], 0 )
    item22.SetName( "pnl_profile" )
    item1.Add( item22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER, 5 )

    item23 = wx.BoxSizer( wx.HORIZONTAL )
    
    item24 = wx.Button( parent, ID_BUTTON, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetName( "btn_cancel" )
    item23.Add( item24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item25 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetName( "btn_ok" )
    item23.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item23, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def kh_billows( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Event File Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [200,-1], 0 )
    item3.SetName( "inp_eventpath" )
    item1.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "EventFile:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = mChoice( parent, ID_CHOICE, wx.DefaultPosition, [100,-1], 
        ["Random","LES","DNS"] , 0 )
    item5.SetName( "cho_eventfile" )
    item1.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Randomize:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = mCheckBox( parent, ID_CHECKBOX, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetName( "inp_randomize" )
    item1.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Distance Scale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item9.SetName( "inp_distscl" )
    item1.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Hub Center Vertical:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item11.SetName( "inp_ctlz" )
    item1.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Hub Center Lateral:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item13 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item13.SetName( "inp_ctly" )
    item1.Add( item13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Start Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item15.SetName( "inp_ctt" )
    item1.Add( item15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item16 = wx.BoxSizer( wx.HORIZONTAL )
    
    item17 = wx.Button( parent, ID_BUTTON, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item17.SetName( "btn_cancel" )
    item16.Add( item17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetDefault()
    item18.SetName( "btn_ok" )
    item16.Add( item18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def dlg_settings( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Full-field output files" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = mCheckBox( parent, ID_CHECKBOX, "TurbSim/AeroDyn form (.bts)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetName( "inp_wradff" )
    item1.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = mCheckBox( parent, ID_CHECKBOX, "BLADED/AeroDyn form (.wnd)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "inp_wrblff" )
    item1.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = mCheckBox( parent, ID_CHECKBOX, "Formatted (readable) form (.u,.v,.w)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "inp_wrfmtff" )
    item1.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.StaticBox( parent, -1, "Hub-Height output files" )
    item6 = wx.StaticBoxSizer( item7, wx.VERTICAL )
    
    item8 = mCheckBox( parent, ID_CHECKBOX, "time-series (.hh)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "inp_wradhh" )
    item6.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = mCheckBox( parent, ID_CHECKBOX, "Parameters in binary form (.bin)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "inp_wrbhhtp" )
    item6.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = mCheckBox( parent, ID_CHECKBOX, "Parameters in formatted form (.dat)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetName( "inp_wrfhhtp" )
    item6.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.StaticBox( parent, -1, "miscellaneous" )
    item11 = wx.StaticBoxSizer( item12, wx.VERTICAL )
    
    item13 = wx.BoxSizer( wx.HORIZONTAL )
    
    item14 = wx.StaticText( parent, ID_TEXT, "Random Seed:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = mTextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [130,-1], 0 )
    item15.SetName( "inp_randseed" )
    item13.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11.Add( item13, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item16 = mCheckBox( parent, ID_CHECKBOX, "Output tower time-series (.twr)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.SetName( "inp_wradtwr" )
    item11.Add( item16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = mCheckBox( parent, ID_CHECKBOX, "Turbine rotates clockwise?", wx.DefaultPosition, wx.DefaultSize, 0 )
    item17.SetName( "inp_clockwise" )
    item11.Add( item17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.BoxSizer( wx.HORIZONTAL )
    
    item19 = wx.StaticText( parent, ID_TEXT, "Scale IEC turbulence models?", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20 = mChoiceBin( parent, ID_CHOICE, wx.DefaultPosition, [70,-1], 
        ["No","Hub","All"] , 0 )
    item20.SetName( "cho_scaleiec" )
    item18.Add( item20, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11.Add( item18, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.BoxSizer( wx.HORIZONTAL )
    
    item22 = wx.StaticText( parent, ID_TEXT, "TurbSim path:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item21.Add( item22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item23 = wx.TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [150,-1], 0 )
    item23.SetName( "inp_turbsim_exec" )
    item21.Add( item23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11.Add( item21, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item24 = wx.BoxSizer( wx.HORIZONTAL )
    
    item25 = wx.Button( parent, ID_BUTTON, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetName( "btn_cancel" )
    item24.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item26 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.SetDefault()
    item26.SetName( "btn_ok" )
    item24.Add( item26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item24, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

ID_SAVE = 20005
ID_SAVEAS = 20004
ID_LOAD = 20003
ID_MENU = 10009
ID_Settings = 20101
ID_ConfigGrid = 20102
ID_ConfigProf = 20103
ID_ConfigTurb = 20104

def MyMenuBarFunc():
    item0 = wx.MenuBar()
    
    item1 = wx.Menu()
    item1.Append( ID_SAVE, "Save", "" )
    item1.Append( ID_SAVEAS, "Save As...", "" )
    item1.Append( ID_LOAD, "Load File...", "" )
    item1.AppendSeparator()
    item1.Append( wx.ID_ABOUT, "About", "" )
    item1.Append( wx.ID_EXIT, "Quit", "" )
    item0.Append( item1, "File" )
    
    item2 = wx.Menu()
    item2.Append( ID_Settings, "Settings...", "" )
    item2.Append( ID_ConfigGrid, "Grid...", "" )
    item2.Append( ID_ConfigProf, "Profile...", "" )
    item2.Append( ID_ConfigTurb, "Turbulence...", "" )
    item0.Append( item2, "Configure" )
    
    return item0

# Toolbar functions


def MyToolBarFunc( parent ):
    parent.SetMargins( [2,2] )
    
    
    parent.Realize()

# Bitmap functions


# End of generated file
