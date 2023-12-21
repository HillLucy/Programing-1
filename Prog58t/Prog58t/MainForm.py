import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SandyBrown
		self._label1.Font = System.Drawing.Font("Lucida Sans", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(164, 97)
		self._label1.TabIndex = 0
		self._label1.Text = """Purchase Price:

Amount Recieved:

Change Due:"""
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Coral
		self._textBox1.Font = System.Drawing.Font("Myanmar Text", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(183, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(174, 28)
		self._textBox1.TabIndex = 1
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Coral
		self._textBox2.Font = System.Drawing.Font("Myanmar Text", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(183, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(174, 28)
		self._textBox2.TabIndex = 2
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Coral
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Myanmar Text", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(183, 78)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(174, 31)
		self._label2.TabIndex = 3
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SandyBrown
		self._label3.Font = System.Drawing.Font("Lucida Sans", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(23, 268)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(309, 63)
		self._label3.TabIndex = 4
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSkyBlue
		self._button1.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 113)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 102)
		self._button1.TabIndex = 5
		self._button1.Text = "Caluclate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSkyBlue
		self._button2.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(133, 113)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 102)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSkyBlue
		self._button3.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(255, 113)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 102)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SandyBrown
		self._label4.Font = System.Drawing.Font("Lucida Sans", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(23, 331)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(309, 63)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SandyBrown
		self._label5.Font = System.Drawing.Font("Lucida Sans", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(23, 394)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(309, 63)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SandyBrown
		self._label6.Font = System.Drawing.Font("Lucida Sans", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(23, 457)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(309, 63)
		self._label6.TabIndex = 10
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.SandyBrown
		self._label7.Font = System.Drawing.Font("Lucida Sans", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(23, 520)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(309, 63)
		self._label7.TabIndex = 11
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSeaGreen
		self.ClientSize = System.Drawing.Size(370, 633)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		price = float(self._textBox1.Text)
		recieve = float(self._textBox2.Text)
		change = recieve - price
		dollar = math. floor(change)
		q = change - dollar
		quart = q / 0.25
		quarter = math. floor(quart)
		d = q - ( 0.25 * quarter )
		di = d / 0.10
		dime = math. floor(di)
		n = d - ( 0.10 * dime)
		nick = n / 0.05
		nickel = math. floor(nick)
		p = n - ( 0.05 * nickel)
		pen = p / 0.01
		penny = math. floor(pen)
		self._label2.Text = str(change)
		self._label3.Text = "Dollars: " + str(dollar)
		self._label4.Text = "Quarters: " + str(quarter)
		self._label5.Text = "Dimes: " + str(dime)
		self._label6.Text = "Nickels: " + str(nickel)
		self._label7.Text = "Pennies: " + str(penny)

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass