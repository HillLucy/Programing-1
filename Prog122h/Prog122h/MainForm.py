import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LemonChiffon
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Olive
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 113)
		self._button1.TabIndex = 0
		self._button1.Text = "List"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LemonChiffon
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Olive
		self._button2.Location = System.Drawing.Point(371, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 113)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LemonChiffon
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Olive
		self._button3.Location = System.Drawing.Point(693, 13)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 113)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 18
		self._listBox1.Location = System.Drawing.Point(13, 169)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(837, 364)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gold
		self.ClientSize = System.Drawing.Size(863, 573)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number \t\t Square \t\t Square Root \t\t Cube \t\t Fourth Root"
		for num in range(1, 20+1):
			column1 = num ** 2.0
			column1 = round(column1, 4)
			column2 = math.sqrt(num)
			column2 = round(column2, 4)
			column3 = num ** 3.0
			column3 = round(column3, 4)
			column4 = num ** (1.0 / 4)
			column4 = round(column4, 4)
			msg = str(num) + "\t\t" + str(column1) + "\t\t" + str(column2) + "\t\t\t" + str(column3) + "\t\t" + str(column4)
			self._listBox1.Items.Add(header)
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()