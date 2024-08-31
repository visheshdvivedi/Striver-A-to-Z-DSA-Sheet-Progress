class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.history = {}
        for sentence, time in zip(sentences, times):
            self.history[sentence] = self.history.get(sentence, 0) + time
        self.current_query = ""
    
    def input(self, c):
        if c == '#':
            if self.current_query:
                self.history[self.current_query] = self.history.get(self.current_query, 0) + 1
            self.current_query = ""
            return []
        else:
            self.current_query += c
            
            suggestions = []
            for sentence in self.history:
                if sentence.startswith(self.current_query):
                    suggestions.append((self.history[sentence], sentence))
                    
            suggestions.sort(key=lambda x: (-x[0], x[1]))
            return [sentence for _, sentence in suggestions[:3]]