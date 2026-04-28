import sqlite3

conexion = sqlite3.connect('universidad.db')

# ── Crear tablas ──────────────────────────────────────────────
conexion.execute('''
CREATE TABLE IF NOT EXISTS aula (
    id          INTEGER PRIMARY KEY,
    descripcion TEXT    NOT NULL,
    horas       INTEGER NOT NULL
)''')

conexion.execute('''
CREATE TABLE IF NOT EXISTS universitario (
    id               INTEGER PRIMARY KEY,
    nombre           TEXT NOT NULL,
    apellidos        TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
)''')

conexion.execute('''
CREATE TABLE IF NOT EXISTS matriculacion (
    id                  INTEGER PRIMARY KEY,
    fecha_matriculacion DATE    NOT NULL,
    curso_id            INTEGER NOT NULL,
    universitario_id    INTEGER NOT NULL,
    FOREIGN KEY (curso_id)         REFERENCES aula(id),
    FOREIGN KEY (universitario_id) REFERENCES universitario(id)
)''')

# ── Insertar datos ────────────────────────────────────────────
conexion.execute('''
INSERT INTO aula (descripcion, horas)
VALUES ('Programacion(Python)-I', 25)
''')

conexion.execute('''
INSERT INTO aula (descripcion, horas)
VALUES ('Programacion-Web(HTML, CSS, JavaScript)-I', 30)
''')

conexion.execute('''
INSERT INTO universitario (nombre, apellidos, fecha_nacimiento)
VALUES ('Caleb', 'Acarapi', '1999-09-09')
''')

conexion.execute('''
INSERT INTO matriculacion (fecha_matriculacion, curso_id, universitario_id)
VALUES ('2024-02-01', 1, 1)
''')

conexion.execute('''
INSERT INTO matriculacion (fecha_matriculacion, curso_id, universitario_id)
VALUES ('2024-02-01', 2, 1)
''')

conexion.commit()

# ── Mostrar tabla: aula ───────────────────────────────────────
print("=" * 50)
print(f"{'TABLA: AULA':^50}")
print("=" * 50)
print(f"{'ID':<5} {'DESCRIPCION':<35} {'HORAS':<6}")
print("-" * 50)
for fila in conexion.execute('SELECT * FROM aula'):
    print(f"{fila[0]:<5} {fila[1]:<35} {fila[2]:<6}")

# ── Mostrar tabla: universitario ──────────────────────────────
print("\n" + "=" * 55)
print(f"{'TABLA: UNIVERSITARIO':^55}")
print("=" * 55)
print(f"{'ID':<5} {'NOMBRE':<15} {'APELLIDOS':<15} {'NACIMIENTO':<12}")
print("-" * 55)
for fila in conexion.execute('SELECT * FROM universitario'):
    print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<15} {fila[3]:<12}")

# ── Mostrar tabla: matriculacion ─────────────────────────────t
