
import os
import torch
import transformers

# Set the directory where the preprocessed data is located
data_dir = 'preprocessed_data'

# Set the device to use for training
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Define the model architecture
model = transformers.GPT2Model.from_pretrained('gpt2').to(device)

# Define the optimizer
optimizer = torch.optim.Adam(model.parameters())

# Define the loss function
loss_fn = torch.nn.CrossEntropyLoss()


num_epochs = 10
# Import the required libraries

# Iterate through the preprocessed data files in the directory
for data_file in os.listdir(data_dir):
    # Load the data from the file
    with open(os.path.join(data_dir, data_file), 'r') as f:
        data = f.read()

    # Convert the data to a PyTorch tensor
    data = torch.Tensor(data).long().to(device)

    # Train the model
    for i in range(num_epochs):
        # Clear the gradients
        optimizer.zero_grad()

        # Forward pass
        output = model(data)

        # Compute the loss
        loss = loss_fn(output, data)

        # Backward pass
        loss.backward()

        # Update the parameters
        optimizer.step()

# Save the trained model
# Save the trained model
torch.save(model.state_dict(), 'trained_model.pt')
