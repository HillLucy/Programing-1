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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGreen
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkGreen
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(172, 89)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Thistle
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MediumPurple
		self._button2.Location = System.Drawing.Point(213, 13)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(172, 89)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DarkGoldenrod
		self._button3.Location = System.Drawing.Point(410, 14)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(172, 89)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(150, 109)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(432, 30)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Firebrick
		self._label1.Location = System.Drawing.Point(13, 109)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(139, 30)
		self._label1.TabIndex = 4
		self._label1.Text = "Enter a Number:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.PaleTurquoise
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Teal
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(13, 143)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(569, 468)
		self._listBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCoral
		self.ClientSize = System.Drawing.Size(594, 639)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		n = float(self._textbox.Text)
		msgsrt = "The value of" + str(n)
		if n = 0:
			pass
		else n!
		msg = str(n)
			