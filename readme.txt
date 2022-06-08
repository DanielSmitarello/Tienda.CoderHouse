Bienvenidos a Codertrónica...

La tienda de hardware ideal...

El proyecto esta basado en la idea de simular una tienda virtual limitada en funciones (no funcionan botones como la compra de productos, el cart, etc...)

1. Luego de crear el proyecto se procedió a crear la app "electrónica".

2. Dentro de la app se crearon los modelos en models.py
    class Pc_Notebooks(models.Model):
    class Perifericos(models.Model):
    class Monitores(models.Model):

3. Luego se realizó la carga de las vistas en views.py
    def index #página de inicio
    def pc_notebooks #página de los productos
    def perifericos #página de los productos
    def screen #página de los productos
    def create_product_monitores #página para crear los productos por formulario en el front
    def create_product_pcnotebooks #página para crear los productos por formulario en el front
    def create_product_perifericos #página para crear los productos por formulario en el front
    def search_product #página para la busqueda de los productos por marca

4. Se crearon los correspondientes templates.

5. En settings.py se modificaron las rutas del BASE/DIR para el TEMPLATE. Luego se registró la APP 'electrónica'.

6. Por último se registraron las URL en la carpeta tienda.
