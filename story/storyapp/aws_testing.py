import os
import boto3


def upload_data_to_s3(directory_path):
    bucket_name = 'story21'
    access_key_id = 'AKIAXYKJRRBQSNB7NKG7'
    secret_access_key = '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'

    # Initialize the S3 client
    s3_client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    uploaded_files = {}  # Dictionary to store file paths and corresponding S3 URLs

    try:
        # Upload files and subfolders to S3
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, directory_path)
                relative_dir = os.path.dirname(relative_path)
                
                # Construct S3 key based on relative directory path
                s3_key = os.path.join(relative_dir, file)

                # Create folder structure on S3
                s3_folder_path = os.path.join(os.path.basename(directory_path), relative_dir)
                s3_folder_path = s3_folder_path.replace('\\', '/')  # for Windows compatibility
                s3_client.put_object(Bucket=bucket_name, Key=s3_folder_path + '/')
                
                # Upload file to S3
                s3_object_key = s3_folder_path + '/' + file
                s3_client.upload_file(local_file_path, bucket_name, s3_object_key)
                print(f"{local_file_path} uploaded to S3 as {s3_object_key}.")

                # Set public read ACL for the uploaded object
                s3_client.put_object_acl(
                    ACL='public-read',
                    Bucket=bucket_name,
                    Key=s3_object_key
                )

                # Construct S3 URL
                s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_object_key}"
                uploaded_files[local_file_path] = s3_url

    except Exception as e:
        print(f"An error occurred while uploading data to S3: {e}")
        return None
    
    print(f"All files and folders in {directory_path} uploaded successfully to S3.")
    return uploaded_files
