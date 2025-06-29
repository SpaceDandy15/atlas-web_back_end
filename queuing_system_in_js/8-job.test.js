import { strict as assert } from 'assert';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create queue and enable test mode
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    // Clear the test jobs and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    assert.throws(() => createPushNotificationsJobs({}, queue), {
      name: 'Error',
      message: 'Jobs is not an array',
    });
  });

  it('should create two new jobs to the queue', () => {
    const jobsList = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' },
    ];

    createPushNotificationsJobs(jobsList, queue);

    // Check the length of jobs in the queue
    assert.equal(queue.testMode.jobs.length, 2);

    // Check the data of the first job
    assert.deepEqual(queue.testMode.jobs[0].data, jobsList[0]);
    // Check the data of the second job
    assert.deepEqual(queue.testMode.jobs[1].data, jobsList[1]);
  });
});
