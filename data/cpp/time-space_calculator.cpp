#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define r 11
#define c 4
#define printVel 1 // add the velocity to output

int main(int argc, char const *argv[]) {

  float t, s, Dt, Ds, Dp, Df;

  int samples;
  ifstream inFile;
  ofstream ofFile;

  string fileName;

  inFile.open("input.txt");

  if(!inFile) {
    std::cout << "inFile not found!" << '\n';
    return -1;
  }

  std::cout << "getting matrix data..." << '\n';
  inFile >> samples;

  float matrix[r][c + 1];

  for (size_t k = 0; k < samples; k++) {
    // read one data sample
    for (size_t i = 0; i < r; i++) {
      for (size_t j = 0; j < c; j++){
        inFile >> matrix[i][j];
        std::cout << matrix[i][j] << ' ';
      }
      std::cout << '\n';
    }

    std::cout << "processing data..." << '\n';
    Df = matrix[10][0] - matrix[0][0];
    Dp = matrix[10][1] - matrix[0][1];
    Dt = matrix[10][2] - matrix[0][2];
    Ds = matrix[0][3] - matrix[10][3];
    std::cout << Dt << ' ' << Ds << ' ' << Dp << ' ' << Df << "\n\n";

    //time
    for (size_t i = 1; i < r - 1; i++) {
      matrix[i][2] = matrix[0][2] + Dt/Df * (matrix[i][0] - matrix[0][0]);
      //std::cout << matrix[i][2] << '\n';
    }
    //std::cout << '\n';

    //space
    for (size_t i = 1; i < r - 1; i++) {
      matrix[i][3] = matrix[0][3] - Ds/Dp * (matrix[i][1] - matrix[0][1]);
      //std::cout << matrix[i][3] << '\n';
    }
    //std::cout << '\n';

    if(printVel){
      //output the data
      fileName.append("output");
      fileName.append(to_string(k));
      fileName.append(".csv");
      ofFile.open(fileName);
      ofFile << "frame,pixel,t,s,v" << '\n';

      //calculate velocity
      matrix[0][c] = 0; // v(0) = 0
      for (size_t i = 1; i < r; i++) {
        matrix[i][c] = (matrix[i - 1][3] - matrix[i][3])/(matrix[i][2] - matrix[i - 1][2]);
      }

      for (size_t i = 0; i < r; i++) {
        for (size_t j = 0; j < c + 1; j++){
          if(j != c)
            ofFile << matrix[i][j] << ',';
          else
            ofFile << matrix[i][j] << ' ';
          std::cout << matrix[i][j] << ' ';
        }
        ofFile << '\n';
        std::cout << '\n';
      }
      fileName.clear();
      ofFile.close();
      std::cout << "\n\n";
    }

    else{
      //output the data
      fileName.append("output");
      fileName.append(to_string(k));
      fileName.append(".csv");
      ofFile.open(fileName);
      ofFile << "frame,pixel,t,s" << '\n';
      for (size_t i = 0; i < r; i++) {
        for (size_t j = 0; j < c; j++){
          if(j != c - 1)
            ofFile << matrix[i][j] << ',';
          else
            ofFile << matrix[i][j] << ' ';
          std::cout << matrix[i][j] << ' ';
        }
        ofFile << '\n';
        std::cout << '\n';
      }
      fileName.clear();
      ofFile.close();
      std::cout << "\n\n";
    }
  }

  std::cout << "done..." << '\n';
  return 0;
}
