This project takes a screenshot of url address

Requirements:

- Install Docker from https://docs.docker.com/desktop/windows/install/
- The script uses two arguments: url & path
  - url -> address for the screenshot - mandatory
  - path -> path to write the file to - Default is on "results/"


As a standalone script the user can run a simple  
python command using url flag:

python main.py --url="https://example.com"

RUN:

To run the project:

- Clone the project to your machine: git clone https://github.com/yakir11244/projects.git
- Build the image: docker build -t name_of_container /dir/path
- Run the container: docker run -v local_absolute_path:/app/results -e URL=https://google.com -it screenshot