require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(118, 52)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(128, 20)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(118, 78)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(128, 20)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(118, 130)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(128, 20)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(118, 104)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(128, 20)
		@textBox4.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightCoral
		@label1.Font = System::Drawing::Font.new("Comic Sans MS", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Gold
		@label1.Location = System::Drawing::Point.new(13, 74)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 50)
		@label1.TabIndex = 4
		@label1.Text = "Integers:"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.LightCoral
		@label2.Font = System::Drawing::Font.new("Elephant", 21.7499981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(513, 48)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(345, 118)
		@label2.TabIndex = 5
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::Color.LightCoral
		@label3.Font = System::Drawing::Font.new("Elephant", 21.7499981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(513, 230)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(345, 118)
		@label3.TabIndex = 6
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Coral
		@button1.Font = System::Drawing::Font.new("Comic Sans MS", 15.75, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Gold
		@button1.Location = System::Drawing::Point.new(57, 189)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(350, 65)
		@button1.TabIndex = 7
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DarkSeaGreen
		@button2.Font = System::Drawing::Font.new("Comic Sans MS", 15.75, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Gold
		@button2.Location = System::Drawing::Point.new(57, 280)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(350, 65)
		@button2.TabIndex = 8
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.CadetBlue
		@button3.Font = System::Drawing::Font.new("Comic Sans MS", 15.75, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.Gold
		@button3.Location = System::Drawing::Point.new(57, 366)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(350, 65)
		@button3.TabIndex = 9
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.IndianRed
		self.ClientSize = System::Drawing::Size.new(955, 443)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "Prog 54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		one = int(@textBox1.Text)
		two = int(@textBox2.Text)
		three = int(@textBox3.Text)
		four = int(@textBox4.Text)
		sum = one + two + three + four
		ave = one + two + three + four / 4.0
		@label2.Text = "Sum: " + str(sum)
		@label3.text = "Average: " = str(ave)
	end
end

