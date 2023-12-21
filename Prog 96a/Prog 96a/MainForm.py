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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orchid
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(232, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 37)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Orchid
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(232, 56)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 37)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orchid
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(232, 99)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 37)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumPurple
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(214, 123)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Kilowatts Used:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(25, 58)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(189, 35)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkOrchid
		self._label2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 223)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(320, 58)
		self._label2.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkOrchid
		self._label3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 281)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(320, 58)
		self._label3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkOrchid
		self._label4.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 397)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(320, 58)
		self._label4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkOrchid
		self._label5.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(12, 455)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(320, 58)
		self._label5.TabIndex = 8
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkOrchid
		self._label6.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(12, 339)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(320, 58)
		self._label6.TabIndex = 9
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkOrchid
		self._label7.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(12, 167)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(320, 56)
		self._label7.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(344, 534)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog 96a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		kilowatt = float(self._textBox1.Text)
		basecharge = kilowatt * 0.0475
		basecharge = round(basecharge, 2)
		surcharge = basecharge * 0.10
		surcharge = round(surcharge, 2)
		citytax = basecharge * 0.03
		citytax = round(citytax, 2)
		total = basecharge + surcharge + citytax
		latefee = (total * 0.04) + total
		latefee = round(latefee, 2)
		self._label7.Text = "Kilowatts Used: " + str(kilowatt)
		self._label2.Text = "Basecharge: $" + str(basecharge)
		self._label3.Text = "Surcharge: $" + str(surcharge)
		self._label6.Text = "City Tax: $" + str(citytax)
		self._label4.Text = "Total: $" + str(total)
		self._label5.Text = "Total After Pay Period: $" + str(latefee)

	def Button2Click(self, sender, e):
		self._label7.Text = "Kilowatts Used: "
		self._label2.Text = "Basecharge: $"
		self._label3.Text = "Surcharge: $"
		self._label6.Text = "City Tax: $"
		self._label4.Text = "Total: $"
		self._label5.Text = "Total After Pay Period: $"

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label5Click(self, sender, e):
		pass