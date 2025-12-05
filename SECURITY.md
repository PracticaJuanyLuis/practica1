# Política de Seguridad

## Reporte de vulnerabilidades

Si encuentras una vulnerabilidad en el código o configuración del proyecto:

1. No publiques el problema en Issues de forma pública.
2. Contacta con el equipo del proyecto o el profesorado.
3. Incluye pasos claros para reproducir la vulnerabilidad.

## Gestión de secretos

- Nunca comprometer credenciales dentro del repositorio.
- Si se usan variables de entorno, crear un archivo `.env.example` sin datos sensibles.
- Utilizar GitHub Secrets para tokens o información privada si fuera necesario.

## Dependencias

- Las dependencias se gestionan con `requirements.txt`.
- Se recomienda revisar y actualizar librerías vulnerables cuando sea necesario.
