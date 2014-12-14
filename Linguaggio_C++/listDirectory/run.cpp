#include <string>
#include <vector>

class Splitter {
		std::vector<std::string> _tokens;
	public:
		typedef std::vector<std::string>::size_type size_type;
	public:
		Splitter ( const std::string& src, const std::string& delim )
		{
			reset ( src, delim );
		}
		std::string& operator[] ( size_type i )
		{
			return _tokens.at ( i );
		}
		size_type size() const
		{
			return _tokens.size();
		}
		void reset ( const std::string& src, const std::string& delim )
		{
			std::vector<std::string> tokens;
			std::string::size_type start = 0;
			std::string::size_type end;
			for ( ; ; ) {
				end = src.find ( delim, start );
				tokens.push_back ( src.substr ( start, end - start ) );
				if ( end == std::string::npos )
					break;
					start = end + delim.size();
				}
				_tokens.swap ( tokens );
		}
};


#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <stdio.h>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <iostream>

int main(int argc, char** argv)
{
	if ( argc < 2 )
	{
		std::cout << "\n Please insert a path from command line. (ex. "<<argv[0]<<" /dir )\n\n";
		exit (EXIT_FAILURE);
	}

	std::cout<<argc<<std::endl;
	DIR *dir;
	struct dirent *entry;

	const std::string line ="start";
	Splitter split ( line, "," );


	if ((dir = opendir(argv[1])) == NULL)
		perror("opendir() error");
		else {
			puts("contents of root:");
			while ((entry = readdir(dir)) != NULL){
				split.reset( entry->d_name, "." );
				std::cout << split.size() << std::endl;
				std::cout << entry->d_name << std::endl;
				for ( Splitter::size_type i = 0; i < split.size(); i++ )
					std::cout<<'|'<< split[i] <<"|\n";
				}
				closedir(dir);
			}

	return 0;
}
