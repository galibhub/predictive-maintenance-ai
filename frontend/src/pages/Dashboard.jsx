import { useLocation } from "react-router-dom";

function Dashboard() {
  const { state } = useLocation();

  if (!state) {
    return (
      <h2>
        No prediction data found.
      </h2>
    );
  }

  return (
    <div>
      <h1>Prediction Result</h1>

      <p>
        Prediction:
        {state.prediction}
      </p>

      <p>
        Probability:
        {state.probability}%
      </p>

      <p>
        Risk Level:
        {state.risk_level}
      </p>

      <p>
        Health Score:
        {state.health_score}
      </p>
    </div>
  );
}

export default Dashboard;