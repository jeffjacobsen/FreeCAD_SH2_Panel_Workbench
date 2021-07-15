# -*- coding: utf-8 -*-
# FreeCAD script for the commands of the basic workbench creation tutorial
# (c) 2017 Felipe Machado

#***************************************************************************
#*   (c) Felipe Machado   2017                                             *
#*   https://github.com/felipe-m/tutorial_freecad_wb                       *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/
import PySide
from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui
import Part
import os

__dir__ = os.path.dirname(__file__)

# FreeCAD Command made with a Python script
def MakeBox(box_len = 1, box_wid = 1, box_hei = 1, box_x = 0, box_y = 0, box_z = 0, box_name='box', box_t=0):
    doc = FreeCAD.ActiveDocument
    box =  doc.addObject("Part::Box",box_name)
    box.Length = FreeCAD.Units.parseQuantity(str(box_len) + 'in')
    box.Width  = FreeCAD.Units.parseQuantity(str(box_wid) + 'in')
    box.Height = FreeCAD.Units.parseQuantity(str(box_hei) + 'in')
    box.ViewObject.Transparency=box_t
    X = FreeCAD.Units.parseQuantity(str(box_x) + 'in')
    Y  = FreeCAD.Units.parseQuantity(str(box_y) + 'in')
    Z = FreeCAD.Units.parseQuantity(str(box_z) + 'in')
    box.Placement = FreeCAD.Placement(FreeCAD.Vector(X,Y,Z),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))

class _Make8ftPanelCmd:

    def Activated(self):
        # what is done when the command is clicked
        MakeBox(48, 5.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(48, 5.5, 1.5, 0, 0, 94.125, "Top_Plate")
        MakeBox(1.5, 5.5, 92.625, 0, 0, 1.5, "Left_Stud")
        MakeBox(1.5, 5.5, 92.625, 15.5, 0, 1.5, "Stud_2")
        MakeBox(1.5, 5.5, 92.625, 31, 0, 1.5, "Stud_3")
        MakeBox(1.5, 5.5, 92.625, 46.5, 0, 1.5, "Right_Stud")
        MakeBox(14, 1.5, 1.75, 1.5, 4, 10, "Botom_Spacer_1")
        MakeBox(14, 1.5, 1.75, 17, 4, 10, "Botom_Spacer_2")
        MakeBox(14, 1.5, 1.75, 32.5, 4, 10, "Botom_Spacer_3")
        MakeBox(48, 0.75, 96, 0, -0.75, -0.375, "Exterior Plywood", 50) 
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '8ft Exterior Panel',
            'ToolTip': 'Create a new 8ft Exterior Panel'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class _Make8ftWindowCmd:

    def Activated(self):
        # what is done when the command is clicked
        MakeBox(48, 5.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(48, 5.5, 1.5, 0, 0, 94.125, "Top_Plate")
        MakeBox(1.5, 5.5, 81.375, 0, 0, 1.5, "Left_Stud")
        MakeBox(1.5, 5.5, 81.375, 3, 0, 1.5, "Stud_2")
        MakeBox(1.5, 5.5, 19.875, 15.5, 0, 1.5, "Cripple_1")
        MakeBox(1.5, 5.5, 19.875, 31, 0, 1.5, "Cripple_2")
        MakeBox(1.5, 5.5, 81.375, 43.5, 0, 1.5, "Stud_3")
        MakeBox(1.5, 5.5, 81.375, 46.5, 0, 1.5, "Right_Stud")
        MakeBox(48, 1.5, 11.25, 0, 0, 82.875, "Header 1")
        MakeBox(48, 1.5, 11.25, 0, 4, 82.875, "Header 2")
        MakeBox(39, 5.5, 1.5, 4.5, 0, 21.375, "Bottom_Frame")
        MakeBox(11, 1.5, 1.75, 4.5, 4, 10, "Botom_Spacer_1")
        MakeBox(14, 1.5, 1.75, 17, 4, 10, "Botom_Spacer_2")
        MakeBox(11, 1.5, 1.75, 32.5, 4, 10, "Botom_Spacer_3")
        MakeBox(48, 0.75, 96, 0, -0.75, -0.375, "Exterior Plywood", 50) 
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '8ft Window Panel',
            'ToolTip': 'Create a new 8ft Window Panel'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class _Make8ftInteriorCmd:

    def Activated(self):
        # what is done when the command is clicked
        MakeBox(48, 3.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(48, 3.5, 1.5, 0, 0, 94.125, "Top_Plate")
        MakeBox(1.5, 3.5, 92.625, 0, 0, 1.5, "Left_Stud")
        MakeBox(1.5, 3.5, 92.625, 15.5, 0, 1.5, "Stud_2")
        MakeBox(1.5, 3.5, 92.625, 31, 0, 1.5, "Stud_3")
        MakeBox(1.5, 3.5, 92.625, 46.5, 0, 1.5, "Right_Stud")
        MakeBox(14, 3.5, 1.5, 1.5, 0, 10, "Botom_Spacer_1")
        MakeBox(14, 3.5, 1.5, 17, 0, 10, "Botom_Spacer_2")
        MakeBox(14, 3.5, 1.5, 32.5, 0, 10, "Botom_Spacer_3") 
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '8ft Interior Panel',
            'ToolTip': 'Create a new 8ft Interior Panel'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class _Make9ftInteriorCmd:

    def Activated(self):
        # what is done when the command is clicked
        MakeBox(48, 3.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(48, 3.5, 1.5, 0, 0, 106.125, "Top_Plate")
        MakeBox(1.5, 3.5, 104.625, 0, 0, 1.5, "Left_Stud")
        MakeBox(1.5, 3.5, 104.625, 15.5, 0, 1.5, "Stud_2")
        MakeBox(1.5, 3.5, 104.625, 31, 0, 1.5, "Stud_3")
        MakeBox(1.5, 3.5, 104.625, 46.5, 0, 1.5, "Right_Stud")
        MakeBox(14, 3.5, 1.5, 1.5, 4, 11.625, "Botom_Spacer_1")
        MakeBox(14, 3.5, 1.5, 17, 4, 11.625, "Botom_Spacer_2")
        MakeBox(14, 3.5, 1.5, 32.5, 4, 11.625, "Botom_Spacer_3") 
        MakeBox(48, 0.375, 96, 0, -0.375, 11.625, "Front Beadboard", 50)
        MakeBox(48, 0.375, 96, 0, 3.5, 11.625, "Back Beadboard", 50)   
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '9ft Interior Panel',
            'ToolTip': 'Create a new 9ft Interior Panel'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class _Make9ftPanelCmd:

    def Activated(self):
        # what is done when the command is clicked
        MakeBox(48, 5.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(48, 5.5, 1.5, 0, 0, 106.125, "Top_Plate")
        MakeBox(1.5, 5.5, 104.625, 0, 0, 1.5, "Left_Stud")
        MakeBox(1.5, 5.5, 104.625, 15.5, 0, 1.5, "Stud_2")
        MakeBox(1.5, 5.5, 104.625, 31, 0, 1.5, "Stud_3")
        MakeBox(1.5, 5.5, 104.625, 46.5, 0, 1.5, "Right_Stud")
        MakeBox(14, 1.5, 1.75, 1.5, 4, 11.625, "Botom_Spacer_1")
        MakeBox(14, 1.5, 1.75, 17, 4, 11.625, "Botom_Spacer_2")
        MakeBox(14, 1.5, 1.75, 32.5, 4, 11.625, "Botom_Spacer_3") 
        MakeBox(14, 1.5, 1.75, 1.5, 0, 95, "Top_Spacer_1")       
        MakeBox(14, 1.5, 1.75, 17, 0, 95, "Top_Spacer_2") 
        MakeBox(14, 1.5, 1.75, 32.5, 0, 95, "Top_Spacer_3")
        MakeBox(48, 0.75, 96, 0, -0.75, -1, "Exterior Plywood", 50)  
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '9ft Exterior Panel',
            'ToolTip': 'Create a new 9ft Exterior Panel'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Make_9ft_Exterior', _Make9ftPanelCmd())
FreeCADGui.addCommand('Make_8ft_Window', _Make8ftWindowCmd())
FreeCADGui.addCommand('Make_8ft_Exterior', _Make8ftPanelCmd())
FreeCADGui.addCommand('Make_8ft_Interior', _Make8ftInteriorCmd())
FreeCADGui.addCommand('Make_8ft_Interior', _Make9ftInteriorCmd())
