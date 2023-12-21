require "mscorlib"
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
		@label1.BackColor = System::Drawing::Color.GreenYellow
		@label1.Font = System::Drawing::Font.new("MS Reference Sans Serif", 20.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(25, 13)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(454, 420)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Lucida Sans Unicode", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(521, 34)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(309, 142)
		@button1.TabIndex = 1
		@button1.Text = "Make Schedule"
		@button1.UseVisualStyleBackColor = true
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Wheat
		@button2.Font = System::Drawing::Font.new("Lucida Sans Unicode", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(521, 252)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(309, 142)
		@button2.TabIndex = 2
		@button2.Text = "Close"
		@button2.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(861, 442)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end
end

