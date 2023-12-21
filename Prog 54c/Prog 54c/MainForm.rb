require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label2 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::Color.OliveDrab
		@textBox1.Location = System::Drawing::Point.new(115, 49)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(202, 20)
		@textBox1.TabIndex = 0
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.SeaShell
		@label1.Location = System::Drawing::Point.new(12, 46)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 1
		@label1.Text = "Radius:"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.YellowGreen
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.WhiteSmoke
		@button1.Location = System::Drawing::Point.new(643, 23)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(302, 102)
		@button1.TabIndex = 2
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkOliveGreen
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.WhiteSmoke
		@button2.Location = System::Drawing::Point.new(643, 153)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(302, 102)
		@button2.TabIndex = 3
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.ForestGreen
		@button3.Font = System::Drawing::Font.new("Comic Sans MS", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.WhiteSmoke
		@button3.Location = System::Drawing::Point.new(643, 285)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(302, 102)
		@button3.TabIndex = 4
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.FromArgb(192, 0, 0)
		@label2.Font = System::Drawing::Font.new("Comic Sans MS", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(26, 128)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(573, 259)
		@label2.TabIndex = 5
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Tomato
		self.ClientSize = System::Drawing::Size.new(957, 436)
		self.Controls.Add(@label2)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "Prog 54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		Radius = float(@textBox1.Text)
		pi = 3.14159
		a = pi * radius**2
		area = round (a,3)
		@label1.Text = "Area: " + str(area)
	end
end

