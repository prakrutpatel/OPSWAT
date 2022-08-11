import hash
import sys
import json
import requests
import os


filename = str(sys.argv[2])
filepath = str(os.path.abspath(filename))
hash_value = hash.hash_function(filepath)     #Calculate hash value of the file using hash.py

apikey = str(sys.argv[1])   #API KEY set while building the script

hash_check_headers = {
    'apikey': apikey,
}


try:
    #Retrieve scan reports by looking up the file's sha256 hash value
    hash_check_response = requests.request('GET', f'https://api.metadefender.com/v4/hash/{hash_value}', headers=hash_check_headers)

except requests.exceptions.RequestException as err:
    raise Exception(err)

else:

    #If hash lookup came back with hash not found message then proceed to upload the file for scan
    if hash_check_response.status_code == 404:
        
        post_headers = {
        'apikey': apikey,
        'filename': filename,
        }

        #Getting the raw binary of the file and encoding(Boundary, content-type, etc) it so that it can be uploaded as Multipart/form-data.
        files = {'file': open(filepath, 'rb')}
        body, content_type = requests.models.RequestEncodingMixin._encode_files(files, {})
        post_headers['Content-Type'] = content_type
        
        
        try:
            post_response = requests.request('POST','https://api.metadefender.com/v4/file', headers=post_headers, data=body)
        
        except requests.exceptions.RequestException as err:
            raise Exception(err)
        
        else:
            
            #If post was successful then proceed with the process
            if post_response.status_code == 200:
                
                data_id = json.loads(post_response.text)['data_id']    #Retreive data_id from the curl response

                progress_headers = {
                'apikey': apikey,
                }

                while True:
                    #Repeatedly pull on the "data_id" to retrieve results
                    try:
                        progress_response = requests.request('GET',f'https://api.metadefender.com/v4/file/{data_id}', headers=progress_headers)
                    
                    except requests.exceptions.RequestException as err:
                        raise Exception(err)
                    
                    else:
                        hash_check = json.loads(progress_response.text)
                        process_percent = hash_check['scan_results']['progress_percentage']
                        if(process_percent == 100):     #Stop the loop when all scan are finished running and results are available
                            break
                
                # Print in the results in desired format
                print('filename: ', hash_check['file_info']['display_name'])
                print('overall_status: ', hash_check['scan_results']['scan_all_result_a'])
                scan_level1 = hash_check['scan_results']['scan_details']
                
                for provider in scan_level1:
                    print('engine: ', str(provider))
                    print('threat_found: ', str(scan_level1[provider]['threat_found']))
                    print('scan_result: ', str(scan_level1[provider]['scan_result_i']))
                    print('def_time: ', str(scan_level1[provider]['def_time']))
            
            
            
            # If post was unsuccessful raise an exception and display the error
            else:
                raise Exception('Error {}'.format(json.loads(post_response.text)['error']['messages'][0]))

    
    
    #If hash lookup was successful then display the results in the correct format
    elif hash_check_response.status_code == 200: 
        true_hash = json.loads(hash_check_response.text)
        print('filename: ', true_hash['file_info']['display_name'])
        print('overall_status: ', true_hash['scan_results']['scan_all_result_a'])
        scan_level1 = true_hash['scan_results']['scan_details']
        for provider in scan_level1:
            print('engine: ', str(provider))
            print('threat_found: ', str(scan_level1[provider]['threat_found']))
            print('scan_result: ', str(scan_level1[provider]['scan_result_i']))
            print('def_time: ', str(scan_level1[provider]['def_time']))
    
    
    
    #If an status code was thrown while performing hash lookup then print the error code and the reason thrown
    else: 
        print("Error {} occured".format(hash_check_response.status_code))
        print("Response:", f'{hash_check_response.reason} - {json.loads(hash_check_response.text)["error"]["messages"][0]}')