class RatingMixin():
    
    def validate_rating(self):
        return (0 <= self.rating) and (self.rating <= 10)
    
    def normalize_rating(self):
        return self.rating / 10   
    