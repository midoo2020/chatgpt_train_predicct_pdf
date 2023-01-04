# Import the required libraries
import sys
from PyQt5 import QtWidgets, uic ,QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton
import transformers

# Define the main widget
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Load the trained model
        self.model = transformers.GPT2Model.from_pretrained('trained_model.pt')

        # Create the text edit widgets for the input and output
        self.input_text_edit = QTextEdit()
        self.output_text_edit = QTextEdit()

        # Create the "Ask" button
        self.ask_button = QPushButton('Ask')

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_text_edit)
        layout.addWidget(self.output_text_edit)
        layout.addWidget(self.ask_button)
        self.setLayout(layout)

        # Connect the "Ask" button to the ask_question slot
        self.ask_button.clicked.connect(self.ask_question)

    def ask_question(self):
        # Get the input text
        input_text = self.input_text_edit.toPlainText()

        # Convert the input text to a PyTorch tensor
        input_tensor = torch.Tensor(input_text).long().unsqueeze(0)

        # Generate the output text
        output_tensor = self.model(input_tensor, max_length=1024)
        output_text = output_tensor[0]

        # Display the output text word by word
        for word in output_text:
            self.output_text_edit.insertPlainText(word + ' ')


# Create the main application
app = QApplication(sys.argv)

# Create and show the main widget
widget = MainWidget()
widget.show()

# Run the main application loop
sys.exit(app.exec_())
