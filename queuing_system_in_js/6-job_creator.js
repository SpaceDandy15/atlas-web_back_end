import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Job data object
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'This is a test notification',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
