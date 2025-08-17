import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getLongURL } from '../actions/urlActions';

const RedirectPage = () => {
  const { uid } = useParams();
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLongURLAndRedirect = async () => {
      try {
        const data = await getLongURL(uid);
        window.location.href = data.long_url;
      } catch (error) {
        setError(error.message);
      }
    };

    fetchLongURLAndRedirect();
  }, [uid]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return <div>Redirecting...</div>;
};

export default RedirectPage;
