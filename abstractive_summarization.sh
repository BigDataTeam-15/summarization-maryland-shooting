#Steps after clustering sentences from the big collection and coverting them to json
python2.7 process_data_for_pointer_summrizer/json_to_hash.py -f clustered_newsroom_sentences.json -o try_cluster/data_dir

python2.7 process_data_for_pointer_summrizer/make_datafiles.py try_cluster/data_dir val.bin

mkdir finished_files/log

mkdir finished_files/log/myexperiment

#copy train folder from pretrained model to myexperiment
#replace generated vocab file with vocab file from processed CNN/DailyMail dataset

python pointer-generator/run_summarization.py --mode=decode --data_path=finished_files/chunked/val_* --vocab_path=finished_files/vocab --log_root=finished_files/log/ --exp_name=myexperiment --single_pass=1
