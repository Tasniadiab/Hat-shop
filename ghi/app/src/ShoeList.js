import React, {
    useState,
    useEffect
} from 'react';

function ShoeList() {
    const [shoes, setShoes] = useState([]);
    const getShoes = async () => {
        const shoesUrl = `http://localhost:8080/api/shoes/`;
        const response = await fetch(shoesUrl);
        if (response.ok) {
            const listShoes = await response.json();
            setShoes(listShoes.shoes);
            console.log(listShoes)
        }
    };

    useEffect(() => {
        getShoes();
    }, []);

    return (
        <>
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Manufacturer</th>
                    <th>Model Name</th>
                    <th>Color</th>
                    <th>Picture</th>
                    <th>Bin</th>
                </tr>
            </thead>
            <tbody>
                {shoes.map((shoe) =>{
                    return (
                    <tr key={shoe.id}>
                        <td>{ shoe.Manufacturer }</td>
                        <td>{ shoe.model_name }</td>
                        <td>{ shoe.color }</td>
                        <td><img src={ shoe.picture_url } width={300} height={300} /></td>
                        <td>{shoe.bin.bin_number}</td>
                    </tr>
                    );
                })}
            </tbody>
        </table>
        </>
    );
}

export default ShoeList
