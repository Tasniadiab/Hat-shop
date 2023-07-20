import React, { useState, useEffect } from "react";


function ShoeForm() {
    const [Manufacturer, setManufacturer] = useState("");
    const [model_name, setModelName] = useState("");
    const [color, setColor] = useState("");
    const [picture_url, setPictureUrl] = useState("");
    const [bins, setBins] = useState([]);
    const [bin, setBin] = useState("");


  const handleManufacturerChange = (event) => {
    const value = event.target.value;
    setManufacturer(value);
  };

  const handleModelNameChange = (event) => {
    const value = event.target.value;
    setModelName(value);
  };

  const handleColorChange = (event) => {
    const value = event.target.value;
    setColor(value);
  };

  const handlePictureUrlChange = (event) => {
    const value = event.target.value;
    setPictureUrl(value);
  };

  const handleBinsChange = (event) => {
    const value = event.target.value;
    setBins(value);
  };

  const handleBinChange = (event) => {
    const value = event.target.value;
    setBin(value);
  };

  const fetchData = async () => {

      const url = 'http://localhost:8100/api/bins/';

      const response = await fetch(url);

      if (response.ok) {
          const data = await response.json();
          //ADD LIST OF BINS FOR THE SELECT BUTTON-----------------------------------------
          setBin(data.bin)
      }
  }

  // useEffect() is a hook to make fectch requests to get data:
  useEffect(() => {
      fetchData();
  }, []);

  //SAVE FORM WHEN CLICKED ON "Ceate" BUTTON---------------------------------------------------
  const handleSubmit = async (event) => {
      event.preventDefault();

      // create an empty JSON object
      const data = {};

      data.model_name = model_name;
      data.Manufacturer = Manufacturer;
      data.color = color;
      data.bins = setBins;

      console.log(data);

      //Sends data to the server:
      const shoeUrl = `http://localhost:8080${bins}shoes/`;

      const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
          'Content-Type': 'application/json',
          },
      };

      const response = await fetch(shoeUrl, fetchConfig);

      if (response.ok) {
          const newShoe = await response.json();

          setModelName('');
          setManufacturer('');
          setColor('');
          setBins('');
      }
  }


  return (
  <div className="my-5 container">
    <div className="row">
        <div className="col">
            <div className="card shadow">
                <div className="card-body">
                <form onSubmit={handleSubmit} id="create-shoe-from">
                    <h1 className='card-title'>Looking to organize your shoes?</h1>
                    <p className='mb-3'>Fill out the form below.</p>
                    <p className="mb-3">Tell us more about your shoes!</p>
                    <div className='row'>
                        <div className = 'col'>
                    <div className="form-floating mb-3">
                        <input
                            type="text"
                            name="Manufacturer"
                            placeholder="Manufacturer"
                            value={Manufacturer}
                            onChange={handleManufacturerChange}
                            />
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            type="text"
                            name="modelName"
                            placeholder="Model Name"
                            value={model_name}
                            onChange={handleModelNameChange}
                            />
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            type="text"
                            name="color"
                            placeholder="Color"
                            value={color}
                            onChange={handleColorChange}
                            />
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            type="text"
                            name="picture_url"
                            placeholder="Picture URL"
                            value={picture_url}
                            onChange={handlePictureUrlChange}
                            />
                    </div>
                    <div className="mb-3">
                        <select
                            type="text"
                            name="bins"
                            placeholder="Bins"
                            value={bin}
                            onChange={handleBinsChange}
                        >
                          <option value="">Choose a Bin</option>
                          {bins.map((bin) => {
                            return (
                              <option key={bin.id} value={bin.id}>
                                {bin.id}
                              </option>
                            );
                          })}
                        </select>
                    </div>
                        </div>
                    </div>
                    <button type="submit">Submit</button>
                </form>
                <div className="alert alert-success d-none mb-0" id="success-message">
                            Your Shoes Are Complete.
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

  );
};


export default ShoeForm;
