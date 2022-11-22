ACTIVITAT 1:
Per obtenir els videos he cridat l'script resize.py, d'anteriors labs, i després a l'script VideoUtils he convertit
els videos a tots els formats, i concatenat els 4 videos amb diferents codecs amb un de sol. Aquests videos tenen nom
outputbbb_escala.mp4.

Els videos en format AV1 els he codificat amb un conversor online, ja que el meu portàtil trigava uns 15 minuts per
codificar el video amb menor qualitat. D'aquesta manera m'he estalviat temps, tot i que la crida a ffmpeg funciona.

Un cop generats els videos concatenats no he notat cap diferència significativa, degut a que he codificat els vídeos
amb diferents bitrates (no he tingut temps de canviar-ho). Per tal de poder comparar els resultats, hauria d'haver
programat el mateix bitrate a cada decoder, en comptes d'això, vaig agafar el que funcionava més ràpidament.

El resultat si hagués estat fet amb el mateix bitrate seria que el codec amb més qualitat visual, rang dinàmic i nitidesa
és el AV1, tot i que a altes tases de bits, els resultats no són gaire significatius.

En quant a temps, AV1 suposa, amb diferència un major temps de codificació que la resta, mentre que VP8 i VP9
serien els més ràpids. En el meu cas, ffmpeg ha trigat uns 15-20 minuts en codificar 30s de BBB en AV1, mentre que per
l'H265 i VP9 el resultat l'ha obtingut en 1-2 minuts. Per VP8 en menys d'un minut.


ACTIVITAT 2:
He implementat una interfície senzilla, on cada botó demana el path del video a convertir i genera la conversió al
mateix fitxer on s'ha executat el codi. També té la opció de concatenar els videos del primer exercici per tal
d'estalviar temps executant i codificant els videos (tal com ho fa l'script de VideoUtils). Ho fa agafant els videos en
qualitat 480p, ja que he considerat que tenen la millor relació qualitat/temps de codificació.
A la pestanya About es poden trobar unes petites instruccions de funcionament.