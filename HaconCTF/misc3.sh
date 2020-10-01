p=$(ls './zipv2')
for i in $p 
do
	m=$(ls "./zipv2/$i")
	for l in $m
	do
		cat "./zipv2/$i/$l" 2> /dev/null
	done
done