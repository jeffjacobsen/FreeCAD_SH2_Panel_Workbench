# -*- coding: utf-8 -*-
# FreeCAD script to create modules for Seed Home v2
# https://wiki.opensourceecology.org/wiki/Seed_Home_v2
#
# 2021 - Modified from https://github.com/felipe-m/tutorial_freecad_wb
#
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

def MakePanel(stud_width, stud_len, panel_width, stud_2_pos, stud_3_pos):
    MakeBox(panel_width, stud_width, 1.5, 0, 0, 0, "Bottom_Plate")
    MakeBox(panel_width, stud_width, 1.5, 0, 0, stud_len + 1.5, "Top_Plate")
    MakeBox(1.5, stud_width, stud_len, 0, 0, 1.5, "Left_Stud")
    if (stud_2_pos > 0):
        MakeBox(1.5, stud_width, stud_len, stud_2_pos, 0, 1.5, "Stud_2")
    if (stud_3_pos > 0):
        MakeBox(1.5, stud_width, stud_len, stud_3_pos, 0, 1.5, "Stud_3")
    MakeBox(1.5, stud_width, stud_len, 46.5, 0, 1.5, "Right_Stud")

def MakeBasicPanel(stud_width = 5.5, stud_len = 92.625):
    MakePanel(stud_width, stud_len, 48, 15.5, 31)

def MakeStep(step = 0):
    stepno = str(step)
    x = 10.5 * step
    z = 7.75 * step
    MakeBox(11.25, 42.125, 1.5, x, 0, z+3.375, "Step_" + stepno)
    MakeBox(11.25, 42.125, 1.5, x+1.125, 0, z+1.875, "Step_" + stepno + '_Base')
    MakeBox(32, 1.5, 3.5, x+1.125, 0, z-1.625, "Step_" + stepno + '_Support1')
    MakeBox(32, 1.5, 3.5, x+1.125, 40.6252, z-1.625, "Step_" + stepno + '_Support2')
    MakeBox(0.375, 42.125, 7.25, x+0.75, 0, z-3.875, "Step_" + stepno + '_Front')

class _MakeStairsCmd:

    def Activated(self):
        for step in range(1,15):
            MakeStep(step)
        MakeBox(0.375, 42.125, 7.25, 15*10.5+0.75, 0, 15*7.75-3.875, "Top_Front")
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': 'Stairs',
            'ToolTip': 'Create Stairs'}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class _Make8ftPanelCmd:

    def Activated(self):
        MakeBasicPanel(5.5, 92.625)
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
        MakePanel(5.5, 81.375, 48, 3 ,43.5)
        MakeBox(48, 5.5, 1.5, 0, 0, 0, "Bottom_Plate")
        MakeBox(1.5, 5.5, 19.875, 15.5, 0, 1.5, "Cripple_1")
        MakeBox(1.5, 5.5, 19.875, 31, 0, 1.5, "Cripple_2")
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
        return not FreeCAD.ActiveDocument is None

class _Make8ftInteriorCmd:

    def Activated(self):
        MakeBasicPanel(3.5, 92.625)
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
        return not FreeCAD.ActiveDocument is None

class _Make9ftInteriorCmd:

    def Activated(self):
        #stud length is 1.5 higher than normal
        MakeBasicPanel(3.5, 107.625)
        MakeBox(14, 3.5, 1.5, 1.5, 0, 13.125, "Botom_Spacer_1")
        MakeBox(14, 3.5, 1.5, 17, 0, 13.125, "Botom_Spacer_2")
        MakeBox(14, 3.5, 1.5, 32.5, 0, 13.125, "Botom_Spacer_3")
        MakeBox(48, 0.375, 96, 0, -0.375, 13.125, "Front Beadboard", 50)
        MakeBox(48, 0.375, 96, 0, 3.5, 13.125, "Back Beadboard", 50)
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '9ft 2x4 Interior Panel',
            'ToolTip': 'Create a new 9ft 2x4 Interior Panel'}

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class _Make9ftWideInteriorCmd:

    def Activated(self):
        #stud length is 1.5 higher than normal
        MakeBasicPanel(5.5, 106.125)
        MakeBox(14, 5.5, 1.5, 1.5, 0, 13.125, "Botom_Spacer_1")
        MakeBox(14, 5.5, 1.5, 17, 0, 13.125, "Botom_Spacer_2")
        MakeBox(14, 5.5, 1.5, 32.5, 0, 13.125, "Botom_Spacer_3")
        MakeBox(48, 0.375, 96, 0, -0.375, 13.125, "Front Beadboard", 50)
        MakeBox(48, 0.375, 96, 0, 5.5, 13.125, "Back Beadboard", 50)
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")


    def GetResources(self):
        # icon and command information
        return {
            'Pixmap': __dir__ + '/icons/makebox_cmd.svg',
            'MenuText': '9ft 2x6 Interior Panel',
            'ToolTip': 'Create a new 9ft 2x6 Interior Panel'}

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None


class _Make9ftPanelCmd:

    def Activated(self):
        MakeBasicPanel(5.5, 104.625)
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
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Make_9ft_Exterior', _Make9ftPanelCmd())
FreeCADGui.addCommand('Make_9ft_Wide_Interior', _Make9ftWideInteriorCmd())
FreeCADGui.addCommand('Make_9ft_Interior', _Make9ftInteriorCmd())
FreeCADGui.addCommand('Make_8ft_Window', _Make8ftWindowCmd())
FreeCADGui.addCommand('Make_8ft_Exterior', _Make8ftPanelCmd())
FreeCADGui.addCommand('Make_8ft_Interior', _Make8ftInteriorCmd())
FreeCADGui.addCommand('Make_Stairs', _MakeStairsCmd())
