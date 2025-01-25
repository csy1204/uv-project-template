class HDFSManager:
    def __init__(self, hdfs_host, hdfs_port, hdfs_user):
        """_summary_

        Args:
            hdfs_host (_type_): _description_
            hdfs_port (_type_): _description_
            hdfs_user (_type_): _description_
        """
        self.hdfs_host = hdfs_host
        self.hdfs_port = hdfs_port
        self.hdfs_user = hdfs_user
        # self.client = Client(f"http://{self.hdfs_host}:{self.hdfs_port}", user=self.hdfs_user)

    def list_files(self, path):
        return self.client.list(path)

    def read_file(self, path):
        with self.client.read(path) as reader:
            return reader.read()

    def write_file(self, path, content):
        with self.client.write(path, overwrite=True) as writer:
            writer.write(content)

    def delete_file(self, path):
        self.client.delete(path)

    def delete_dir(self, path):
        self.client.delete(path, recursive=True)

    def create_dir(self, path):
        self.client.makedirs(path)
