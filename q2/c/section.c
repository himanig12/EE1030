struct Point{
	float x;
	float y;
};
struct Point section(float x1, float y1, float x2, float y2, float m, float n)
{
	struct Point p;
	p.x = (n*x1+m*x2)/(m+n);
	p.y = (n*y1+m*y2)/(m+n);
	return p;
}
		
