class Physics:
    def __init__(self):
        self._collideables = []
    
    def add_collideable(self, collideable):
        self._collideables.append(collideable)
    
    def handle_collisions(self):
        for i, a in enumerate(self._collideables):
            for b in self._collideables[i+1:]:
                if a.position.x <= b.position.x+b.width and a.position.x+a.width >= b.position.x and \
                a.position.y <= b.position.y+b.height and a.position.y+a.height >= b.position.y:
                    result_a = a.on_collision_begin(b)
                    result_b = b.on_collision_begin(a)
                    if result_a and result_b:
                        a.colliding.add(b)
                        b.colliding.add(a)
                        if a.stationary:
                            self._resolve_collision(b, a)
                        else:
                            self._resolve_collision(a, b)
                else:
                    if a in b.colliding:
                        # No longer colliding
                        a.colliding.remove(b)
                        b.colliding.remove(a)
                        a.on_collision_end(b)
                        b.on_collision_end(a)
    
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