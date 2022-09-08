from transformers import BlenderbotForConditionalGeneration
# Download 
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
model.save_pretrained('blenderbot_model')
