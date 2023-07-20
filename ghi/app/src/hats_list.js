import React, {
    useState,
    useEffect
} from 'react';

function HatList() {
    const [hats, setHats] =  useState([]);
    const getHats = async () => {
        const hatsUrl = `http://localhost:8090/api/hats/`;
        const response =  await fetch(hatsUrl);
        if (response.ok){
            const listHats = await response.json();
            setHats(listHats.hats);
            console.log(listHats)
        }
    };
    useEffect(() => {
        getHats();
    }, []);
    return (
        <>
        <table className='table table-striped'>
            <thead>
                <tr>
                    <th>Style Name</th>
                    <th>Fabric</th>
                    <th>Color</th>
                    <th>Picture</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {hats.map((hat) => {
                    return(
                    <tr key= {hat.id}>
                        <td>{hat.style_name}</td>
                        <td>{hat.fabric}</td>
                        <td>{hat.color}</td>
                        <td><img src={hat.picture_url} width = {300} height = {300}/></td>
                        <td>{hat.location.closet_name}</td>
                    </tr>
                    );
                })}
            </tbody>
        </table>
        </>
    );
}

export default HatList
