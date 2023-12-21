import System.Drawing
import System.Windows.Forms

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
		self._button1.BackColor = System.Drawing.Color.PapayaWhip
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 96)
		self._button1.TabIndex = 0
		self._button1.Text = "List"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.BlanchedAlmond
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(161, 13)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 96)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Wheat
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(306, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 96)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Honeydew
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 127)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(408, 511)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(433, 645)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122i1"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listbox1.Items.Clear()

	def Button1Click(self, sender, e):
		header = "Number \t\t Cube Root \t\t Cube"
		for num in range(-abs(25), 25+1):
			cubert = int(num) ** (1.0 / 3)
			cubed = int(num) ** 3
			msg = str(num) + "\t\t" + str(cubert) + "\t\t" + str(cubed)
			self._listBox1.Items.Add(msg)