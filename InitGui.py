# -*- coding: utf-8 -*-
# FreeCAD init script of the Basic 4 module,
# simple workbench, 4 commands

#***************************************************************************
#*   (c) Felipe Machado    https://github.com/felipe-m  2017               *
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


class Panels_Workbench (Workbench):
    "Panels workbench object"
    MenuText = "SH2 Panels"
    ToolTip = "Panel workbench"

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        import PanelsGui
        from PySide import QtCore, QtGui
 
        # list of commands, (they are in the imported PanelsGui):
        cmdlist = [ "Make_8ft_Exterior",
                    "Make_8ft_Interior",
                    "Make_9ft_Exterior"]
        self.appendToolbar("Panels", cmdlist)
        self.appendMenu("SH2 Panels", cmdlist)

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# The workbench is added
Gui.addWorkbench(Panels_Workbench())

