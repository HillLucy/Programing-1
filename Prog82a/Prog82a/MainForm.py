import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Khaki
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(223, 60)
		self._label1.TabIndex = 0
		self._label1.Text = "Speed Limit:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Khaki
		self._label2.Font = System.Drawing.Font("Comic Sans MS", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 85)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(223, 60)
		self._label2.TabIndex = 1
		self._label2.Text = "Vehicle Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(243, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(264, 34)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(243, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(264, 34)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Yellow
		self._label3.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.DarkGoldenrod
		self._label3.Location = System.Drawing.Point(13, 176)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(494, 135)
		self._label3.TabIndex = 4
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Goldenrod
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(13, 345)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(148, 128)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(195, 345)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(148, 128)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Goldenrod
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(376, 345)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(148, 128)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gold
		self.ClientSize = System.Drawing.Size(536, 638)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		speedlim = float(self._textBox1.Text)
		speedcar = float(self._textBox2.Text)
		fi = 20 + ( 5 * ( speedcar - speedlim))
		fine = round(fi, 10)
		self._label3.Text = "Fine: $" + str(fine)

	def Button2Click(self, sender, e):
		self._label3.Text = "Fine: "

	def Button3Click(self, sender, e):
		Application.Exit()