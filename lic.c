#include <stdio.h>
#include <string.h>

int strln(char *c)
{ int l=0;
    while (c[l]!='\0')
    {
        l++;
    }
    return l;
    
}
void PatternMatching(char* text, char* pattern) {
     int m,n;
     
     m = strln(text);
     n = strln(pattern);

    for (int i = 0; i <= m - n; i++) {
        int j;
        for (j = 0; j < n; j++) {
            if (text[i + j] != pattern[j])
                break;
        }

        if (j == n) {
            printf("Pattern found at index %d\n", i);
        }
    }
}

int main() {
    char text[100];
    char pattern[50];
    gets(text);
    printf("%d\n",strln(text));
    gets(pattern);

    PatternMatching(text, pattern);

    return 0;
}
