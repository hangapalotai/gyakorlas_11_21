time_now=int(input('Hány óra van most?'))

if time_now<8:
    print('Még nem rendel a doktorúr, sürgős esetben hívja az ügyeletet, vagy ennyi idő múlva keresse a rendelőben:'+str((8-time_now)*60))
if time_now<12:
    print('Ennyi perced van még odaérni:' + str((12-time_now)*60))
if time_now>12:
    print('Ma már nem rendel a doktorúr, keresse holnap reggel, sürgős estben hívja az ügyeletet!')