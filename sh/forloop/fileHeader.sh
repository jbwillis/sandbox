#! /bin/bash

FILES=*.[ch]
for filename in $FILES; do
	echo -ne "/* $filename \n * \n * Project: Space Invaders \n * Authors: Jacob Willis and Evan Jones\n * Course: ECEN 427\n * Date Started: 3-Oct-2018\n */\n\n" > $filename 
done
