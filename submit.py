import client
import secrets

# gen = 22
# vector = [-1.5010954938264294e-19, -1.3248818226414269e-11, -3.339128621895449e-14, 1.2606131081640684e-10, -3.929554120060549e-11, 7.698666724127938e-16, -1.0680487326297334e-17, 2.5789446913745724e-06, -9.490322989813028e-07, -9.267311787611333e-10, 3.369559597262585e-10]
# err_sum: [138385043841.74316, 63612618185.63043]
# test: 8th (now 13)

# gen: 95
# vector = [-5.68378280463811e-20, -1.0212769410914117e-11, -9.926695876691298e-15, 7.714704094164429e-11, -9.781636633167851e-11, 3.0681956264921704e-16, 5.932924882340974e-17, 5.28970227753616e-06, -1.296905889933971e-06, -8.063173375044021e-10, 4.5912778251513745e-10] #17

# vector = [-5.415138756263681e-22, -1.2632050632477804e-12, -2.1712350723200247e-13, 7.029232107540644e-11, 6.525271330129899e-12, -1.1773327856827165e-15, 6.234011936224841e-16, 1.4470926460775324e-05, -1.2725116782083933e-06, -4.859761860270188e-09, 5.024168948015435e-10]
# 9th


# vector = [6.006686369117927e-21, -3.8427312619206e-12, -2.9746658602189574e-13, 5.1945199790000246e-11, -2.3437855281121627e-11, -9.028263971973054e-16, 1.3560113043767708e-15, 8.906850601685366e-06, -1.1635560993956466e-06, -3.3979817969805724e-09, 4.6105202996795556e-10]
# 20

# v = [1.9523115277582824e-20, -3.2844100090490717e-12, -9.211755597829879e-14, 2.1605777567497808e-11, -1.3819049781624463e-11, -9.999827050766438e-16, 3.406213044431594e-16, 1.2313584904833184e-05, -6.340507050042589e-07, -4.649795482262576e-09, 2.2370696996819345e-10]

# vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]


# vector = [-4.515427659504844e-23, -2.2893800200251174e-12, -2.8218345707948847e-13, 6.150426951142064e-11, -2.1336142541814116e-10, -
#           4.693350236188929e-16, 1.176442380529682e-16, 9.735898686170397e-06, -7.093349459469169e-07, -9.157052623852781e-09, 4.1945574566498987e-10]

# v = [-1.5010954938264294e-19, -1.3248818226414269e-11, -3.339128621895449e-14, 1.2606131081640684e-10, -3.929554120060549e-11,
#      7.698666724127938e-16, -1.0680487326297334e-17, 2.5789446913745724e-06, -9.490322989813028e-07, -9.267311787611333e-10, 3.369559597262585e-10]
# 13

# v = [-5.415138756263681e-22, -1.2632050632477804e-12, -2.1712350723200247e-13, 7.029232107540644e-11, 6.525271330129899e-12, -1.1773327856827165e-15, 6.234011936224841e-16, 1.4470926460775324e-05, -1.2725116782083933e-06, -4.859761860270188e-09, 5.024168948015435e-10]
# 8

# MAR 15 TESTING


# v = [
#     -7.921948773686077e-20,
#     -7.331640840224322e-12,
#     -3.3285990493734e-14,
#     1.3277327924648254e-10,
#     -2.431670004761979e-11,
#     4.731004451915012e-16,
#     -2.6739261739107158e-17,
#     6.543350708705723e-06,
#     -5.836795122354546e-07,
#     -7.752694169177941e-10,
#     1.8054664562562294e-10
# ]
# "errorTuple": [
#     634391684822.8254,
#     1448994981923.6167
# ]
# 13

############################################

# v = [
#     -1.977264778107763e-22,
#     -6.716378069144415e-13,
#     -1.7339422802505887e-13,
#     9.304756839348557e-11,
#     -9.140959421756749e-10,
#     -6.871096778959524e-16,
#     1.678130311896248e-16,
#     8.143188147977253e-06,
#     -9.033196478772561e-07,
#     -3.5526710339315863e-09,
#     3.38858290832117e-10
# ]
# "errorTuple": [
#     327125751853.4462,
#     170115636539.21088
# ]
# 33

# v = [
#     -2.332435890172733e-22,
#     -6.690160761883427e-13,
#     -1.5246706714119718e-13,
#     7.419922798608777e-11,
#     -9.670823582801899e-10,
#     -4.924076949361555e-16,
#     2.861248814028825e-16,
#     5.735311081191775e-06,
#     -9.11921880436231e-07,
#     -4.392879710445847e-09,
#     3.792015171733036e-10
# ]
# "errorTuple": [
#     333716587579.5349,
#     78437186001.59668
# ]
# 50

# v = [
#     -1.525094177395225e-22,
#     -7.068012796539137e-13,
#     -1.3301696212276854e-13,
#     6.255434048129352e-11,
#     -6.523703665191019e-10,
#     -3.9440311657768443e-16,
#     1.927208281427892e-16,
#     6.407350134663688e-06,
#     -9.226965972428636e-07,
#     -4.049219385607827e-09,
#     3.947611637279757e-10
# ]
# "errorTuple": [
#     264387701342.7392,
#     454645871497.2956
# ]
# 48

# v = [
#     -2.4297624062119703e-22,
#     -4.4109252380568714e-13,
#     -1.7913597661928555e-13,
#     1.4444217717670137e-10,
#     -7.037178244269463e-10,
#     -5.594807366091485e-16,
#     3.2976817114795327e-16,
#     8.72948019196929e-06,
#     -8.46927874707971e-07,
#     -3.815710118018129e-09,
#     3.059779388284509e-10
# ]
# "errorTuple": [
#     456735164996.17126,
#     289241531975.0809
# ]
# 23

v = [
    -2.3820393820408088e-22,
    -6.43631020558006e-13,
    -1.7463690713831118e-13,
    1.0825778497681858e-10,
    -8.461776996329149e-10,
    -5.368698851833086e-16,
    1.943410263863416e-16,
    1.1718121610434156e-05,
    -9.391674420110669e-07,
    -2.2491508426129588e-09,
    3.020041446973123e-10
]
# "errorTuple": [
#     184128098891.82416,
#     202811056977.58615
# ]
# 38

# v = [
#     -1.5577544398604296e-22,
#     -7.051214695499939e-13,
#     -1.018942509914024e-13,
#     7.173553960291644e-11,
#     -1.6786986183967358e-09,
#     -3.521124431010159e-16,
#     1.435770185259481e-16,
#     8.721222422662855e-06,
#     -7.505240464107588e-07,
#     -2.8875438987241216e-09,
#     2.4000433183642053e-10
# ]
# # "errorTuple": [
#     478256386753.21985,
#     365766509452.4127
# ]
# 4
# star

# v = [
#     -1.4095125027542437e-22,
#     -8.660271991043346e-13,
#     -1.3156020665725656e-13,
#     1.0797239316979142e-10,
#     -1.4253730314686626e-09,
#     -5.248329497781932e-16,
#     1.393506327761506e-16,
#     7.148823783093753e-06,
#     -5.133583052805499e-07,
#     -2.7456661051206083e-09,
#     1.8448813957305537e-10
# ]
# "errorTuple": [
#     468900660660.2829,
#     744889480229.1823
# ]
# 38

# v = [
#     -1.5364229047848288e-22,
#     -5.044743520729274e-13,
#     -1.9318017322389622e-13,
#     7.581147176615305e-11,
#     -5.143037984539095e-10,
#     -6.194123514860644e-16,
#     2.1816388544358437e-16,
#     1.0139077653642506e-05,
#     -1.052319450845378e-06,
#     -4.663942443153081e-09,
#     4.259742061379293e-10
# ]
# "errorTuple": [
#     107511395357.17305,
#     230137579979.11456
# ]
# 42

# v = [
#     -1.7924522440137194e-22,
#     -8.310195792333813e-13,
#     -1.9721781263018837e-13,
#     9.988787976672653e-11,
#     -7.351297935728802e-10,
#     -4.780254553253479e-16,
#     1.9331544034891356e-16,
#     1.2420822699203985e-05,
#     -8.647209447747028e-07,
#     -2.819138192332363e-09,
#     2.7077585204255847e-10
# ]
# "errorTuple": [
#     243221435597.90347,
#     246660802373.69293
# ]
# 35

# v = [
#     -1.3521724490618934e-22,
#     -6.679010983646024e-13,
#     -3.107736772223092e-13,
#     1.212236469090347e-10,
#     -3.602621732219087e-10,
#     -3.3044418401567764e-16,
#     1.0474857083272902e-16,
#     9.80688734623162e-06,
#     -6.2782023730171e-07,
#     -1.9888584132289374e-09,
#     1.732247164715421e-10
# ]
# "errorTuple": [
#     313735310736.7511,
#     378017087318.16455
# ]
# 25

# v = [
#     -1.3053000992104165e-22,
#     -2.7509494783164904e-13,
#     -1.9554872258162828e-13,
#     2.544775254431563e-10,
#     -3.2872245938578487e-10,
#     -4.772940768097539e-16,
#     3.618475561841987e-17,
#     5.804369492090331e-06,
#     -6.993570560376594e-07,
#     -8.033207508523684e-10,
#     2.1435797201605704e-10
# ]
# "errorTuple": [
#     320781966518.7172,
#     241797260053.8291
# ]
# 14

# v = [
#     -2.2713028391988447e-22,
#     -3.4483678162334223e-13,
#     -2.0494218607106777e-13,
#     1.2764034904157968e-10,
#     -1.1989658043751296e-09,
#     -8.355619255289446e-16,
#     2.9276255589718027e-16,
#     1.1890601161105223e-05,
#     -8.31901778338822e-07,
#     -1.8253742205187209e-09,
#     2.668360338970868e-10
# ]
# "errorTuple": [
#     259555102764.20532,
#     710074493888.4353
# ]
# 36

# v = [
#     -1.6388487969233095e-22,
#     -7.339289881318214e-13,
#     -1.2515689679009738e-13,
#     5.51244863162438e-11,
#     -3.3058001541761136e-10,
#     -5.476895900131983e-16,
#     3.3938808296366935e-16,
#     6.212689362533583e-06,
#     -1.265343072067611e-06,
#     -4.517097699987032e-09,
#     5.436151681720527e-10
# ]
# "errorTuple": [
#     82489801824.64554,
#     107849918969.55252
# ]
# 47

# v = [
#     -1.43059216007641e-22,
#     -6.041543487328474e-13,
#     -8.26718316701597e-14,
#     4.449950274298683e-11,
#     -3.101439585328232e-10,
#     -5.8416910150076335e-16,
#     3.4734898259467174e-16,
#     8.621208794873587e-06,
#     -1.0503443370529192e-06,
#     -7.406061567331426e-09,
#     4.704573343569235e-10
# ]
# "errorTuple": [
#     444963169710.5397,
#     146528644112.58636
# ]
# 65

# v = [
#     -1.5309321119994053e-22,
#     -6.178679756125158e-13,
#     -1.8708654762905378e-13,
#     4.999118490548556e-11,
#     -6.237083673681213e-10,
#     -7.671435310879953e-16,
#     2.2324692903003925e-16,
#     1.0953477595451773e-05,
#     -1.1819837279183546e-06,
#     -4.745657732425436e-09,
#     4.4975770262991327e-10
# ]
# "errorTuple": [
#     413888124755.80286,
#     275443700769.13367
# ]
# 17

res = client.submit(secrets.KEY, v)
print(res)
