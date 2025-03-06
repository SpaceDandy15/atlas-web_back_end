function createInt8TypedArray (length, position, value) {
    if (position < 0 || position >= length) {
        throw new Error('Position outsided range');
}

const buffer = new ArrayBuffer(length);
const dataView = new DataView(buffer);  
dataView.setInt8(postion, value);

return dataView;
}

export default createInt8TypedArray;