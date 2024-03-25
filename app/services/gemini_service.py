from vertexai.preview.generative_models import GenerativeModel

class GeminiService:
    def __init__(self):
        self.gemini_pro_model = GenerativeModel("gemini-1.5-pro")

    def generate_content(self, query):
        model_response = self.gemini_pro_model.generate_content(query)
        return model_response.candidates[0].content.parts[0].text