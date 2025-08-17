import React, { useState } from 'react';
import { createShortURL } from '../actions/urlActions';
import Toast from './Toast';

const URLShortenerForm = () => {
  const [longUrl, setLongUrl] = useState('');
  const [expirationDate, setExpirationDate] = useState('');
  const [customAlias, setCustomAlias] = useState('');
  const [userId, setUserId] = useState('');
  const [toast, setToast] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setToast(null);

    try {
      const data = await createShortURL(longUrl, expirationDate, customAlias, parseInt(userId));
      setToast({ message: `Short URL created: ${data.data.short_url}`, type: 'success' });
    } catch (error) {
      setToast({ message: error.message, type: 'error' });
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Long URL:</label>
          <input type="text" value={longUrl} onChange={(e) => setLongUrl(e.target.value)} required />
        </div>
        <div>
          <label>Expiration Date:</label>
          <input type="datetime-local" value={expirationDate} onChange={(e) => setExpirationDate(e.target.value)} required />
        </div>
        <div>
          <label>Custom Alias (Optional):</label>
          <input type="text" value={customAlias} onChange={(e) => setCustomAlias(e.target.value)} />
        </div>
        <div>
          <label>User ID:</label>
          <input type="number" value={userId} onChange={(e) => setUserId(e.target.value)} required />
        </div>
        <button type="submit">Create Short URL</button>
      </form>
      {toast && <Toast message={toast.message} type={toast.type} onClose={() => setToast(null)} />}
    </div>
  );
};

export default URLShortenerForm;
