import { useState } from "react";

function PredictionForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    company_name: "",
    machine_id: "",
    machine_type: "M",
    air_temperature: "",
    process_temperature: "",
    rotational_speed: "",
    torque: "",
    tool_wear: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      ...formData,
      air_temperature: Number(formData.air_temperature),
      process_temperature: Number(formData.process_temperature),
      rotational_speed: Number(formData.rotational_speed),
      torque: Number(formData.torque),
      tool_wear: Number(formData.tool_wear),
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="company_name"
        placeholder="Company Name"
        onChange={handleChange}
      />

      <input
        name="machine_id"
        placeholder="Machine ID"
        onChange={handleChange}
      />

      <select
        name="machine_type"
        onChange={handleChange}
      >
        <option value="L">L</option>
        <option value="M">M</option>
        <option value="H">H</option>
      </select>

      <input
        name="air_temperature"
        placeholder="Air Temp (°C)"
        onChange={handleChange}
      />

      <input
        name="process_temperature"
        placeholder="Process Temp (°C)"
        onChange={handleChange}
      />

      <input
        name="rotational_speed"
        placeholder="RPM"
        onChange={handleChange}
      />

      <input
        name="torque"
        placeholder="Torque"
        onChange={handleChange}
      />

      <input
        name="tool_wear"
        placeholder="Tool Wear"
        onChange={handleChange}
      />

      <button type="submit">
        Predict
      </button>
    </form>
  );
}

export default PredictionForm;