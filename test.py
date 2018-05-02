def author_data_integ(auth_target=auth_target):
    for w in auth_target[1:]:
        print ("starting: " + w[0])
        auth_dir = '{}{}/'.format(aozora_dir, w[0])
        csv_dir = '{}{}'.format(auth_dir, "csv/")
        files = os.listdir(csv_dir)
        integ_np = np.array([["author", "line"]])
        for file in files:
            if "csv" in file:
                print ("   now at: " + file)
                file_name = csv_dir + file
                pds_data = pds.read_csv(file_name, index_col=0)
                pds_data = pds_data.dropna()
                np_data = np.array(pds_data.ix[:,[0,2]])

                out = [j for j in range(len(np_data)) if '-----------' in str(np_data[j,1])]
                if not out: out = [1]
                hyphen_pos = int(out[len(out) - 1])

                last_20 = len(np_data) - 20

                np_data = np_data[hyphen_pos+1:last_20,:]
                integ_np = np.vstack((integ_np, np_data))

        integ_pds = pds.DataFrame(integ_np[1:,:], columns=integ_np[0,:])
        integ_pds.to_csv(auth_dir + w[0] + '_integ.csv', quoting=csv.QUOTE_ALL)
        print ("finished: " + w[0])

author_data_integ()
