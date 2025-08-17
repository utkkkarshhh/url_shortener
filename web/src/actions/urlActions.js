
import axios from 'axios';

export const createShortURL = async (longUrl, expirationDate, customAlias, userId) => {
  const requestBody = {
    long_url: longUrl,
    user_id: userId,
  };

  if (expirationDate) {
    requestBody.expiration_date = expirationDate;
  }

  if (customAlias) {
    requestBody.custom_alias = customAlias;
  }

  try {
    const response = await axios.post(`${import.meta.env.VITE_API_BASE_URL}/v1/CreateShortURL`, requestBody, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message || 'Failed to create short URL');
  }
};

export const getLongURL = async (uid) => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/v1/FetchLongURL/${uid}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || error.message || 'Failed to fetch long URL');
  }
};
