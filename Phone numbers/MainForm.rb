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
		@label1.BackColor = System::Drawing::Color.FromArgb(255, 255, 128)
		@label1.Font = System::Drawing::Font.new("Segoe Script", 12, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.DimGray
		@label1.Location = System::Drawing::Point.new(21, 19)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(356, 399)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Moccasin
		@button1.Font = System::Drawing::Font.new("Lucida Handwriting", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.DimGray
		@button1.Location = System::Drawing::Point.new(514, 19)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(180, 159)
		@button1.TabIndex = 1
		@button1.Text = "List"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		@button2.Font = System::Drawing::Font.new("Lucida Handwriting", 12, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.DimGray
		@button2.Location = System::Drawing::Point.new(514, 254)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(191, 164)
		@button2.TabIndex = 2
		@button2.Text = "Erase"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(837, 438)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Phone numbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.text = "Action City: 715-710-2259 \n Alex's: 715-672-4303 \n Target: 608-754-8331 \n Mall of America: 952-883-8800 \n See's Candies: 630-663-9126"
	end

	def Button2Click(sender, e)
		@label1.text = ""
	end
end

