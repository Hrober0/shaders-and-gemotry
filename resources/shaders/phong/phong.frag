#version 330

in vec3 v_position;
in vec3 v_normal;

out vec4 f_color;

const vec3 light_position = vec3(0.0, 2.0, -10.0);
const vec3 light_ambient = vec3(0.1, 0.1, 0.1);
const vec3 light_diffuse = vec3(1.0, 1.0, 1.0);
const vec3 light_specular = vec3(0.8, 0.8, 0.8);

uniform vec3 material_ambient;
uniform vec3 material_diffuse;
uniform float material_shininess;

uniform vec3 camera_position;

void main()
{
	// Ambient lighting
    vec3 ambient = light_ambient * material_ambient;
    
    // Diffuse lighting
    vec3 N = normalize(v_normal);
    vec3 L = normalize(light_position - v_position);
    float cosNL = clamp(dot(N, L), 0.0, 1.0);
    vec3 diffuse = light_diffuse * material_diffuse * cosNL;
    
    // Specular lighting
    vec3 V = normalize(camera_position - v_position);
    vec3 R = reflect(-L, N);
    float cosRV = pow(clamp(dot(R, V), 0.0, 1.0), material_shininess);
    vec3 specular = light_specular * material_diffuse * cosRV;
    
    // Combine results
    vec3 phong_color = clamp(ambient + diffuse + specular, 0.0, 1.0);
    
    f_color = vec4(phong_color, 1.0);
}
