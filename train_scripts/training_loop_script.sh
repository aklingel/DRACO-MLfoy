#!/bin/bash
#TODO: Check whether necessary to delete best_epoch.csv!
#_v3 kl_use_exact  = True but no fixed prior
#_v4 kl_use_exact  = True AND fixed prior by setting non trainable


name=BNN
output1=Variational_QT_BNN_training_
output2=Variational_BNN_training_

epochs=4000

# cd /home/ycung/Desktop/DRACO-MLfoy/train_scripts/
# layers=("50" "100" "200" "250" "300" "50,50" "50,50,50")
# for i in "${!layers[@]}"; do
#     python train_template_bnn.py -o $output1"${layers[$i]}"_v4 -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n "$name" -p --printroc --binary --signal ttH -e $epochs -q --layers ${layers[$i]}
#     python train_template_bnn.py -o $output2"${layers[$i]}"_v4 -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n "$name" -p --printroc --binary --signal ttH -e $epochs --layers ${layers[$i]}
# done

# name=BNN
# output1=QT_BNN_training_
# output2=BNN_training_
# epochs=4000
iteration=100

# cd /home/ycung/Desktop/DRACO-MLfoy/train_scripts/

for ((i=0; i<$iteration; i+=1)); do
    python train_template_bnn.py -o $output1"$i" -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n "$name" -p --printroc --binary --signal ttH -e $epochs -q
    python train_template_bnn.py -o $output2"$i" -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n "$name" -p --printroc --binary --signal ttH -e $epochs
done

# #ANN
# name=binary_crossentropy_Adam
# output1=QT_ANN_training_
# output2=ANN_training_
# epochs=4000
# iteration=200

# #BNN
# names=('BNN_L2_5050' 'BNN_L3_505050')
# epochs=4000

# cd /home/ycung/Desktop/DRACO-MLfoy/train_scripts/
# # for name in "${names[@]}"; do
# python train_template_bnn.py -o QT_BNN_BNN_L2_5050_training -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n BNN -p --printroc --log --binary --signal ttH -e "$epochs" -q --layers 50,50
# python train_template_bnn.py -o BNN_L2_5050_training_ -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n BNN -p --printroc --binary --signal ttH -e "$epochs" --layers 50,50
# python train_template_bnn.py -o QT_BNN_BNN_L3_505050_training -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n BNN -p --printroc --log --binary --signal ttH -e "$epochs" -q --layers 50,50,50
# python train_template_bnn.py -o BNN_L3_505050_training_ -i /local/scratch/ssd/nshadskiy/2017_nominal -c ge4j_ge3t -v allVariables_2017_bnn -n BNN -p --printroc --binary --signal ttH -e "$epochs" --layers 50,50,50
# # done
