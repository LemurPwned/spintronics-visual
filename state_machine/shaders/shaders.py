
VERTEX_SHADER = """
#version 130 

in vec3 position;
in vec3 color;
in vec3 normal;

out vec3 newColor;
out vec3 fragNormal;
out vec3 fragPos;

void main()
{
    fragNormal = normal;   
    fragPos = position;
    gl_Position = gl_ModelViewProjectionMatrix * vec4(position, 1.0f);
    newColor = color;

}
"""
FRAGMENT_SHADER = """
#version 130 
uniform vec3 lightPos;
uniform vec3 lightColor;
uniform float ambientStrength;

in vec3 newColor;
in vec3 fragNormal;
in vec3 fragPos;

out vec4 outColor;

void main()
{    
    if (newColor.x == 0.0 && 
        newColor.y == 0.0 &&
        newColor.z == 0.0){
        discard;
    }
    vec3 norm = normalize(fragNormal);
    vec3 lightDir = normalize(lightPos - fragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 ambient = ambientStrength * lightColor;
    
    vec3 result = (ambient + diffuse)*newColor;
    outColor = vec4(result, 1.0f);    
}
"""

VERTEX_SHADER2 = """
#version 130 
in vec3 position;
in vec3 color;

out vec4 newColor;
void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * vec4(position, 1.0f);
    newColor = vec4(color, 1.0f);
}
"""
FRAGMENT_SHADER2 = """
#version 130 
in vec4 newColor;
out vec4 outColor;
void main()
{
    outColor = newColor;
}
"""

VERTEX_SHADER3 = """
#version 130 

in vec3 position;
in vec3 normal;

out vec3 fragNormal;
out vec3 fragPos;

void main()
{
    fragNormal = normal;   
    fragPos = position;
    gl_Position = gl_ModelViewProjectionMatrix * vec4(position, 1.0f);
}
"""
FRAGMENT_SHADER3 = """
#version 130 
uniform vec3 lightPos;
uniform vec3 lightColor;
uniform float ambientStrength;

uniform vec3 posColor;
uniform vec3 negColor;
uniform vec3 colVec;

in vec3 fragNormal;
in vec3 fragPos;

out vec4 outColor;

void main()
{
    vec3 newColor;
    float newDot = dot(fragPos, colVec);

    if (newDot > 0.0){
        newColor = posColor*newDot + vec3(1-newDot);
    } 
    else {
        newDot *= -1;
        newColor = negColor*newDot + vec3(1-newDot);
    }
    vec3 norm = normalize(fragNormal);
    vec3 lightDir = normalize(lightPos - fragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 ambient = ambientStrength * lightColor;
    
    vec3 result = (ambient + diffuse)*newColor;
    outColor = vec4(result, 1.0f);
}
"""
