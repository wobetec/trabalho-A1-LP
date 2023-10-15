import base64
from io import BytesIO


def get_image_to_flask(plt) -> str:
    """
    Transforma a figura do matplotlib em uma sequência de bytes para ser usada no Flask e retorna a tag imagem já com esses bytes

    Parametros:

    Returns:
        image (str): Tag imagem com os bytes da figura

    """
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
