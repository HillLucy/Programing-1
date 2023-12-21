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
		self._button1.BackColor = System.Drawing.Color.Chocolate
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(121, 82)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Chocolate
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(149, 13)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(121, 82)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Chocolate
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(285, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(121, 82)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Peru
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 23
		self._listBox1.Location = System.Drawing.Point(13, 102)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(393, 510)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.NavajoWhite
		self.ClientSize = System.Drawing.Size(418, 644)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(-abs(12), 16+1):
			y = (int(num)**6) - (3(int(num)**5)) - (93(int(num)**4)) + (87(int(num)**3)) + (1596(int(num)**2)) - 2800
			msg = str(num) + "\t\t" + str(y)
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.clear()

	def Button3Click(self, sender, e):
		Application.Exit()