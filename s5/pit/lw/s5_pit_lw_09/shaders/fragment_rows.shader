uniform vec4 color_front;
uniform vec4 color_back;
uniform int cnt;
void main() {
	if (mod(gl_FragCoord.x, cnt * 2) < cnt*1.0)
		gl_FragColor = color_front;
	else
		gl_FragColor = color_back;
}