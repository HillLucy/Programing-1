﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightSteelBlue
		@label1.Font = System::Drawing::Font.new("Bradley Hand ITC", 27.75, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.White
		@label1.Location = System::Drawing::Point.new(275, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(296, 429)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DarkSeaGreen
		@button1.Font = System::Drawing::Font.new("MV Boli", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.White
		@button1.Location = System::Drawing::Point.new(58, 98)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(146, 255)
		@button1.TabIndex = 1
		@button1.Text = "Name"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkSeaGreen
		@button2.Font = System::Drawing::Font.new("MV Boli", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.White
		@button2.Location = System::Drawing::Point.new(644, 98)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(151, 263)
		@button2.TabIndex = 2
		@button2.Text = "Erase"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Thistle
		self.ClientSize = System::Drawing::Size.new(846, 447)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Your Name"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.text = "Lucy \n Ellen \n Marie \n Hill"
	end

	def Button2Click(sender, e)
		@label1.text = ""
	end
end

