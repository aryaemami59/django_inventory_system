// const editButton = document.querySelector(".edit-button");
// const generateButton = document.querySelector(".generate-button");
const itemNumberInput = document.querySelector(".item-number-input");
const itemNumberEdit = [...document.querySelectorAll(".item-number")];
const itemCount = [...document.querySelectorAll(".item-count")];
function inputEventHandler() {
  event.currentTarget.value = this.value.replace(/[^0-9]/gi, "");
}
itemNumberInput.addEventListener("input", inputEventHandler);
itemNumberEdit?.forEach(e => {
  e.addEventListener("input", inputEventHandler);
  const img = e.parentElement.querySelector(".barcode");
  // const data = {};
  JsBarcode(img, img.getAttribute("data-item-number"), { height: 50, width: 1.3, fontSize: 15, background: "" });
  // JsBarcode(data, img.getAttribute("data-item-number"), { height: 50, width: 1.3, fontSize: 15, background: "" });
  // const blob = new Blob
  // JsBarcode(data, "text");
  // console.dir(img);
  // console.dir(data.encodings[0].data);
  // console.dir(data);
});
itemCount.forEach(e => e.addEventListener("input", inputEventHandler));
