class HeightWidthDuration(object):
    def set_width(self,width:int):
        self.width = width
    
    def set_height(self,height:int):
        self.height = height
    
    def set_hightwidth(self,height:int,width:int):
        self.set_width = width
        self.set_height = height


class ViewingDirection(object):
    def set_viewingDirection(self,viewingDirection):
        """
        left-to-right	The object is displayed from left to right. The default if not specified.
        right-to-left	The object is displayed from right to left.
        top-to-bottom	The object is displayed from the top to the bottom.
        bottom-to-top	The object is displayed from the bottom to the top.
        """
        viewingDirections = ["left-to-right",
        "right-to-left",
        "bottom-to-top",
        "top-to-bottom"]
        if viewingDirection not in viewingDirections:
            ValueError("viewingDirection mu must be one of these values %s" %viewingDirections)
        self.viewingDirection = viewingDirection
