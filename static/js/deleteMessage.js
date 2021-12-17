/**
 * This is a script
 * for delete the message
 * in the interface.
 */

// during 3 seconds
setTimeout(() => {
  const messages_view = document.querySelector('.messages-view');
  const messsge = document.getElementById('message');
  messages_view.remove(message);
  
}, 3000);