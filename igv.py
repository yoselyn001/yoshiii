# Tasa de IGV en Perú (18%)
IGV_RATE = 0.18

def calcular_igv(precio_sin_igv):
    """
    Calcula el IGV y el precio final con IGV incluido.

    Parámetros:
    - precio_sin_igv: float, precio sin IGV.

    Retorna:
    - Una tupla con el IGV calculado y el precio final con IGV.
    """
    igv = precio_sin_igv * IGV_RATE
    precio_con_igv = precio_sin_igv + igv
    return igv, precio_con_igv

# Ejemplo de uso
precio_sin_igv = 100.0  # Puedes cambiar este valor
igv, precio_final = calcular_igv(precio_sin_igv)

print(f"Precio sin IGV: S/ {precio_sin_igv}")
print(f"IGV (18%): S/ {igv}")
print(f"Precio con IGV: S/ {precio_final}")