# This will be the place to run the input

import os
# set up for the theano
os.environ["THEANO_FLAGS"] = "device=cpu,floatX=float32"
import sys
import getopt
import matplotlib
matplotlib.use('Agg')

import main.setup.parameters as parameters
# Each of the file below will run another small launch depends on exp type


def script_usage():
    print('--exp_type <type of experiment> \n'
          '--num_res <number of resources> \n'
          '--num_nw <number of visible main work> \n'
          '--simu_len <simulation length> \n'
          '--num_ex <number of examples> \n'
          '--num_seq_per_batch <rough number of samples in one batch update> \n'
          '--eps_max_len <episode maximum length (terminated at the end)> \n'
          '--num_epochs <number of epoch to do the training>\n'
          '--time_horizon <time step into future, screen height> \n'
          '--res_slot <total number of resource slots, screen width> \n'
          '--max_job_len <maximum main job length> \n'
          '--max_job_size <maximum main job resource request> \n'
          '--new_job_rate <main job arrival rate> \n'
          '--dist <discount factor> \n'
          '--lr_rate <learning rate> \n'
          '--ba_size <batch size> \n'
          '--pg_re <parameter file for pg network> \n'
          '--v_re <parameter file for v network> \n'
          '--q_re <parameter file for q network> \n'
          '--out_freq <network output frequency> \n'
          '--ofile <output file name> \n'
          '--log <log file name> \n'
          '--render <plot dynamics> \n'
          '--unseen <generate unseen example> \n')


def main():
    # calling the object
    pa = parameters.Parameters()

    # some options for the type of experiment
    type_exp = 'pg_re'  # 'pg_su' 'pg_su_compact' 'v_su', 'pg_v_re', 'pg_re', q_re', 'test'

    # more var
    pg_resume = None
    v_resume = None
    q_resume = None
    log = None

    render = False

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hi:e:o:", ["exp_type=",
                      "num_res=",
                      "num_nw=",
                      "simu_len=",
                      "num_ex=",
                      "num_seq_per_batch=",
                      "eps_max_len=",
                      "num_epochs=",
                      "time_horizon=",
                      "res_slot=",
                      "max_job_len=",
                      "max_job_size=",
                      "new_job_rate=",
                      "dist=",
                      "lr_rate=",
                      "ba_size=",
                      "pg_re=",
                      "v_re=",
                      "q_re=",
                      "out_freq=",
                      "ofile=",
                      "log=",
                      "render=",
                      "unseen="])

    except getopt.GetoptError:
        print("Something is wrong with input for terminal")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            script_usage()
            sys.exit()
        elif opt in ("-e", "--exp_type"):
            type_exp = arg
        elif opt in ("-n", "--num_res"):
            pa.num_res = int(arg)
        elif opt in ("-w", "--num_nw"):
            pa.num_nw = int(arg)
        elif opt in ("-s", "--simu_len"):
            pa.simu_len = int(arg)
        elif opt in ("-n", "--num_ex"):
            pa.num_ex = int(arg)
        elif opt in ("-sp", "--num_seq_per_batch"):
            pa.num_seq_per_batch = int(arg)
        elif opt in ("-el", "--eps_max_len"):
            pa.episode_max_length = int(arg)
        elif opt in ("-ne", "--num_epochs"):
            pa.num_epochs = int(arg)
        elif opt in ("-t", "--time_horizon"):
            pa.time_horizon = int(arg)
        elif opt in ("-rs", "--res_slot"):
            pa.res_slot = int(arg)
        elif opt in ("-ml", "--max_job_len"):
            pa.max_job_len = int(arg)
        elif opt in ("-ms", "--max_job_size"):
            pa.max_job_size = int(arg)
        elif opt in ("-nr", "--new_job_rate"):
            pa.new_job_rate = float(arg)
        elif opt in ("-d", "--dist"):
            pa.discount = float(arg)
        elif opt in ("-l", "--lr_rate"):
            pa.lr_rate = float(arg)
        elif opt in ("-b", "--ba_size"):
            pa.batch_size = int(arg)
        elif opt in ("-p", "--pg_re"):
            pg_resume = arg
        elif opt in ("-v", "--v_re"):
            v_resume = arg
        elif opt in ("-q", "--q_re"):
            q_resume = arg
        elif opt in ("-f", "--out_freq"):
            pa.output_freq = int(arg)
        elif opt in ("-o", "--ofile"):
            pa.output_filename = arg
        elif opt in ("-lg", "--log"):
            log = arg
        elif opt in ("-r", "--render"):
            render = (arg == 'True')
        elif opt in ("-u", "--unseen"):
            pa.generate_unseen = (arg == 'True')
        else:
            print("type -h for showing help")
            sys.exit()

    pa.compute_dependent_parameters()

    if type_exp == 'pg_su':
        NotImplemented

    else:
        print("Error: unkown experiment type " + str(type_exp))
        exit(1)


if __name__ == '__main__':
    main()