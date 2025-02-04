#!/bin/bash

if [ "$#" -ne "2" ]; then
    echo "Usage: $0 <doSubmit> <do4params>"
    exit 0
fi


DOSUBMIT=$1
DO4PARAMS=$2
infolder=output_run2ana_161031_full/ #_datacard/
outfolder=cards_run2ana_161031_full_sig/ #_datacard/
blind=true
#zvvstat=18
zvvstat=0
mkdir -p $outfolder

extraoptions="--do_ues=false" # --do_ggh=false --do_separate_qcdewk=false"

for mass in 110 125 150 200 300 400 500 600
#for mass in 125
do
    mkdir -p $outfolder/$mass
    for mindphicut in 2.31 #1.01 1.21 1.41 1.61 1.81 2.01 2.11 2.21 2.31 2.41 2.51 2.61 2.81
    do
	for minjjcut in 1101 #1401 1601 #901 1001 1101 1201 1301 1401 1501 1601 1701 1801 1901
	do
	    echo "-----------------------------------------------------"
	    echo "---Processing mindphi>$mindphicut and Mjj>$minjjcut"
	    echo "-----------------------------------------------------"
	    OUTNAME=$outfolder/$mass/vbfhinv_${mass}_13TeV_${mindphicut}_${minjjcut}.txt
	    if (( "$DO4PARAMS" == "1" )); then
		OUTNAME=$outfolder/$mass/vbfhinv_${mass}_13TeV_${mindphicut}_${minjjcut}_4params.txt
	    fi
	    if (( "$DOSUBMIT" == "0" )); then
		echo "./bin/makeCountingCard -i $infolder --blind=$blind -o $OUTNAME -m $mass --do_latex true --do_datatop false --zvvstat $zvvstat --mcBkgOnly=true --do_run2=true --do_4params=$DO4PARAMS --minvarXcut=$minjjcut --minvarYcut=$mindphicut --histoToIntegrate=alljetsmetnomu_mindphi:dijet_M $extraoptions | tee $outfolder/$mass/card_${mindphicut}_${minjjcut}.log"
	    else
		./bin/makeCountingCard -i $infolder --blind=$blind -o $OUTNAME -m $mass --do_latex true --do_datatop false --zvvstat $zvvstat --mcBkgOnly=true --do_run2=true --do_4params=$DO4PARAMS --minvarXcut=$minjjcut --minvarYcut=$mindphicut --histoToIntegrate=alljetsmetnomu_mindphi:dijet_M $extraoptions  | tee $outfolder/$mass/card_${mindphicut}_${minjjcut}.log
	    fi
	done
    done
done
