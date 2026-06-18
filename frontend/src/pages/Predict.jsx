import { useNavigate } from "react-router-dom";

import PredictionForm from "../components/prediction/PredictionForm";

import api from "../services/api";

function Predict() {
  const navigate = useNavigate();

  const handlePrediction = async (formData) => {
    try {
      const response = await api.post(
        "/predict",
        formData
      );

      navigate("/dashboard", {
        state: response.data,
      });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Predict Machine Failure</h1>

      <PredictionForm
        onSubmit={handlePrediction}
      />
    </div>
  );
}

export default Predict;