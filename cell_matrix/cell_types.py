class CellTypeRegistry:
    def __init__(self):
        self.types = {}
        self.total_hotness = 0
    
    def add_type(self, name, color, hotness=0):
        """
        Register a new cell type with a color and hotness value.
        
        :param name: Unique identifier for the cell type
        :param color: Color name in English
        :param hotness: Relative probability of appearing during random generation
                      (higher = more likely)
        """
        self.types[name] = {
            'color': color,
            'hotness': hotness
        }
        
        # Update total hotness
        self.total_hotness = sum(t['hotness'] for t in self.types.values())
    
    def get_color(self, name):
        """
        Convert color name to RGB tuple.
        Uses a predefined color mapping.
        """
        if name not in self.types:
            return (100, 100, 100)  # Default gray for unknown types
            
        color_name = self.types[name]['color']
        
        color_map = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (128, 0, 128),
            'orange': (255, 165, 0),
            'gray': (128, 128, 128),
            'pink': (255, 192, 203),
            'brown': (165, 42, 42),
            'cyan': (0, 255, 255),
            'magenta': (255, 0, 255)
        }
        
        return color_map.get(color_name.lower(), (100, 100, 100))
    
    def get_types(self):
        """
        Return all registered types.
        """
        return list(self.types.keys())
        
    def get_random_type_probabilities(self):
        """
        Calculate probability distribution for random cell generation
        based on hotness values.
        
        Returns a dictionary mapping type names to probabilities (0-1).
        """
        if self.total_hotness == 0:
            return {}
            
        return {
            name: info['hotness'] / self.total_hotness
            for name, info in self.types.items()
            if info['hotness'] > 0
        }
        
    def get_random_type(self):
        """
        Select a random cell type based on hotness distribution.
        Returns "empty" if no types have hotness > 0.
        """
        import random
        
        if self.total_hotness == 0:
            return "empty"
            
        # Get all types with hotness > 0
        hot_types = [(name, info['hotness']) 
                     for name, info in self.types.items() 
                     if info['hotness'] > 0]
        
        if not hot_types:
            return "empty"
            
        # Calculate cumulative probabilities
        cumulative = 0
        cum_probs = []
        
        for name, hotness in hot_types:
            cumulative += hotness / self.total_hotness
            cum_probs.append((name, cumulative))
        
        # Generate random number and find corresponding type
        r = random.random()
        
        for name, threshold in cum_probs:
            if r <= threshold:
                return name
                
        return cum_probs[-1][0]  # Fallback to last type
