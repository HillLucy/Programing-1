import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Moccasin
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DarkOrange
		self._button1.Location = System.Drawing.Point(292, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(175, 82)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MistyRose
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.HotPink
		self._label1.Location = System.Drawing.Point(13, 11)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(273, 82)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter Variables:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleGreen
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SeaGreen
		self._button2.Location = System.Drawing.Point(292, 101)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(175, 82)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleTurquoise
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(292, 189)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(175, 82)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightPink
		self._textBox1.ForeColor = System.Drawing.Color.LavenderBlush
		self._textBox1.Location = System.Drawing.Point(180, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightPink
		self._textBox2.ForeColor = System.Drawing.Color.LavenderBlush
		self._textBox2.Location = System.Drawing.Point(180, 46)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LightPink
		self._textBox3.ForeColor = System.Drawing.Color.LavenderBlush
		self._textBox3.Location = System.Drawing.Point(180, 73)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Thistle
		self._label2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.DarkViolet
		self._label2.Location = System.Drawing.Point(13, 113)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(273, 158)
		self._label2.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LemonChiffon
		self.ClientSize = System.Drawing.Size(489, 309)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog 58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		a = float(self._textBox1.Text)
		b = float(self._textBox2.Text)
		c = float(self._textBox3.Text)
		