function getProp(objects, prop) {
    let filteredObjects = [];

    objects.forEach((object) => {
        if (object.hasOwnProperty(prop)) {
            filteredObjects.push(object);
        }
    });
}


function encryptData(msg, key) {
    //encriptar mi data
}