#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let lenght = list.length;
  while (lenght > 0) {
    reversedList.push(list[lenght - 1]);
    lenght--;
  }
  return reversedList;
};
