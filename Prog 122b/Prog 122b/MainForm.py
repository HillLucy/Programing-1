import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.Font = System.Drawing.Font("Elephant", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(361, 86)
		self._label1.TabIndex = 0
		self._label1.Text = "Rate of pay is 4 dollars an hour"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Tomato
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.MistyRose
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 23
		self._listBox1.Location = System.Drawing.Point(13, 113)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(361, 372)
		self._listBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkRed
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MistyRose
		self._button1.Location = System.Drawing.Point(13, 492)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(108, 116)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkRed
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MistyRose
		self._button2.Location = System.Drawing.Point(139, 491)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 116)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MistyRose
		self._button3.Location = System.Drawing.Point(266, 492)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(108, 116)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Firebrick
		self.ClientSize = System.Drawing.Size(386, 620)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog 122b"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		header = "Hours\t\t Pay"
		self._listBox1.Items.Add(header)
		for num in range(1, 40+1):
			pay = num * 4
			msg = str(num) + "\t\t" + str(round(pay, 2))
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()