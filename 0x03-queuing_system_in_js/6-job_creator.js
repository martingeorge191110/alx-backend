import { createQueue } from 'kue';

const jobData = {
  phoneNumber: '01201969696',
  message: 'Hello there!'
};

const queue = createQueue();
const job = queue.create('push_notification_code', jobData);

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });

job.save();
