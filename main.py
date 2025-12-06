
class ShapeContext:
    def __init__(self, shape_type, x, y):
        self.shape_type = shape_type
        self.x = x
        self.y = y

    @classmethod
    def create_shape(cls, context):
        if context.shape_type == ShapeType.CIRCLE:
            return Circle(context.x, context.y)
        elif context.shape_type == ShapeType.RECTANGLE:
            return Rectangle(context.x, context.y)


if __name__ == "__main__":
    
