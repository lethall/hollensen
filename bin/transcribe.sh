cp studio/wav/$1.wav .
whisper-mps --file-name $1.wav --model-name medium.en
bin/extract.py $1
rm $1.wav output.json
