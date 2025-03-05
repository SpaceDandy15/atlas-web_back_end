// Define symbols for private attributes
const _brand = Symbol('brand');
const _motor = Symbol('motor');
const _color = Symbol('color');

// Define the Car class
export default class Car {
  constructor(brand, motor, color) {
    // Initialize attributes with Symbols
    this[_brand] = brand;
    this[_motor] = motor;
    this[_color] = color;
  }

  // Getter methods for accessing the private properties
  get brand() {
    return this[_brand];
  }

  get motor() {
    return this[_motor];
  }

  get color() {
    return this[_color];
  }

  // Method to clone the car object
  cloneCar() {
    return new this.constructor(
      this[_brand],
      this[_motor],
      this[_color]
    );
  }
}
