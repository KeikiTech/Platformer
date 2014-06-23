# Axes
side_up = 0
side_down = 1
side_left = 2
side_right = 3

class Physics:
    def __init__(self):
        self._collideables = []
    
    def add_collideable(self, collideable):
        self._collideables.append(collideable)
    
    def handle_collisions(self):
        for i, a in enumerate(self._collideables):
            for b in self._collideables[i+1:]:
                if a.position.x < b.position.x+b.width and a.position.x+a.width > b.position.x and \
                a.position.y < b.position.y+b.height and a.position.y+a.height > b.position.y:
                    # Only notify if they haven't already been notified
                    if a not in b.colliding:
                        side_a = self._get_collision_side(a, b)
                        side_b = self._get_collision_side(b, a)
                        result_a = a.on_collision_begin(b, side_a)
                        result_b = b.on_collision_begin(a, side_b)
                        if result_a and result_b:
                            a.colliding.add(b)
                            b.colliding.add(a)
                            if a.stationary:
                                side = self._resolve_collision(b, a)
                            else:
                                side = self._resolve_collision(a, b)
                    else:
                        # Already been notified, but still resolve collisions
                        if a.stationary:
                            side = self._resolve_collision(b, a)
                        else:
                            side = self._resolve_collision(a, b)
                # Not colliding, remove from list if they're not still "touching"
                elif not (a.position.x <= b.position.x+b.width and a.position.x+a.width >= b.position.x and \
                a.position.y <= b.position.y+b.height and a.position.y+a.height >= b.position.y):
                    if a in b.colliding:
                        # No longer colliding
                        a.colliding.remove(b)
                        b.colliding.remove(a)
                        a.on_collision_end(b)
                        b.on_collision_end(a)

    def _get_collision_side(self, a, b):
        if a.position.x <= b.position.x:
            x_side = side_right
            xOverlap = b.position.x - (a.position.x + a.width)
        elif a.position.x > b.position.x:
            x_side = side_left
            xOverlap = (b.position.x + b.width) - a.position.x

        if a.position.y <= b.position.y:
            y_side = side_down
            yOverlap = b.position.y - (a.position.y + a.height)
        elif a.position.y > b.position.y:
            y_side = side_up
            yOverlap = (b.position.y + b.height) - a.position.y

        if abs(xOverlap) < abs(yOverlap):
            return x_side
        elif abs(xOverlap) > abs(yOverlap):
            return y_side
    
    def _resolve_collision(self, a, b):
        xOverlap = 0.0
        yOverlap = 0.0

        if a.position.x <= b.position.x:
            xOverlap = b.position.x - (a.position.x + a.width)
        elif a.position.x > b.position.x:
            xOverlap = (b.position.x + b.width) - a.position.x

        if a.position.y <= b.position.y:
            yOverlap = b.position.y - (a.position.y + a.height)
        elif a.position.y > b.position.y:
            yOverlap = (b.position.y + b.height) - a.position.y

        if abs(xOverlap) < abs(yOverlap):
            a.position.x = a.position.x + xOverlap
        elif abs(xOverlap) > abs(yOverlap):
            a.position.y = a.position.y + yOverlap
