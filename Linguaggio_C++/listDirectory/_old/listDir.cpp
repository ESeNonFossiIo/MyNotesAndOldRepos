#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, elems);
	return elems;
}

int main() {
	DIR *dir;
	struct dirent *entry;
	std::vector<std::string> elems;

	if ((dir = opendir("/")) == NULL)
		perror("opendir() error");
		else {
			puts("contents of root:");
			while ((entry = readdir(dir)) != NULL)
				split(entry->d_name,'.');
				printf("  %s\n", entry->d_name);
				closedir(dir);
			}
		}

// #include <dirent.h>
// #include <stdio.h>
//
// int main(void)
// {
// 	DIR           *dirp;
// 	struct dirent *directory;
//
// 	dirp = opendir("/Users/esenonfossiio/git/script/Linguaggio_C++/listDirectory");
// 	if (dirp)
// 	{
// 		while ((directory = readdir(dirp)) != NULL)
// 		{
// 			printf("%s\n", directory->d_name);
// 		}
//
// 		closedir(dirp);
// 	}
//
// 	return(0);
// }
