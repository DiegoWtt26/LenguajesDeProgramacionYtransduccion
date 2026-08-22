/*
 * Enunciado del libro:
 * Rewrite the word count program in C. Run some large files through both versions.
 * Is the C version noticeably faster? How much harder was it to debug?
 */
#include <stdio.h>

static int is_ascii_letter(int character)
{
    return (character >= 'a' && character <= 'z') ||
           (character >= 'A' && character <= 'Z');
}

int main(void)
{
    int character;
    int characters = 0;
    int words = 0;
    int lines = 0;
    int inside_word = 0;

    while ((character = getchar()) != EOF) {
        characters++;

        if (character == '\n') {
            lines++;
        }

        if (is_ascii_letter(character)) {
            if (!inside_word) {
                words++;
                inside_word = 1;
            }
        } else {
            inside_word = 0;
        }
    }

    printf("%8d%8d%8d\n", lines, words, characters);
    return 0;
}

/*
 * Compilación:
 *   cc -O2 -o ejercicio_6 ejercicio_6.c
 *
 * Comparación con Flex:
 *   flex fb1-1.l
 *   cc -O2 -o wordcount_flex lex.yy.c -lfl
 *   time ejercicio_6 < archivo_grande.txt
 *   time wordcount_flex < archivo_grande.txt
 *
 * Ambos programas usan la definición del ejemplo: una palabra es una secuencia
 * de letras [a-zA-Z]+. La versión C suele ser algo más difícil de modificar
 * y depurar, mientras que Flex expresa las reglas de forma más directa. En una
 * prueba con archivos grandes, ambos deberían producir exactamente los mismos
 * conteos; la diferencia de velocidad normalmente es pequeña, aunque el C
 * manual puede ser ligeramente más rápido al evitar la capa del scanner generado.
 * La comparación real debe hacerse con los comandos anteriores en el mismo
 * equipo, porque depende del compilador, el sistema y el tamaño del archivo.
 */