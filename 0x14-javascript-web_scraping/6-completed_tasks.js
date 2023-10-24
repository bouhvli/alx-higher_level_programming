#!/usr/bin/node
const req = require('request');
req(process.argv[2], (error, _response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasksDone = {};
    const res = JSON.parse(body);
    let idx = 0;
    while (idx < res.length) {
      const userId = res[idx].userId;
      const completed = res[idx].completed;
      if (completed && !tasksDone[userId]) {
        tasksDone[userId] = 0;
      }
      if (completed) {
        ++tasksDone[userId];
      }
      idx += 1;
    }
    console.log(tasksDone);
  }
});
