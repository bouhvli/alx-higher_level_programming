#!/usr/bin/node
const argv = process.argv.slice(2);
const fileSystem = require('fs');
const concat = (fileOne, fileTwo, concatenatedFile) => {
  const contentFileOne = fileSystem.readFileSync(fileOne);
  const contentFileTwo = fileSystem.readFileSync(fileTwo);
  const concatenatContent = contentFileOne + '\n' + contentFileTwo;
  fileSystem.writeFileSync(concatenatedFile, concatenatContent);
};
if (argv.length === 3) {
  const pathFile1 = argv[0];
  const pathFile2 = argv[1];
  const pathFile3 = argv[2];
  concat(pathFile1, pathFile2, pathFile3);
}
