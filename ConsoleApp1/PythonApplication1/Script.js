let h = new Date().getHours() > 9 ? new Date().getHours() : "0" + new Date().getHours();
let m = new Date().getMinutes() > 9 ? new Date().getMinutes() : "0" + new Date().getMinutes();
document.getElementById('currentTime').innerText = h + ":" + m;

interact('.rotation-handle')
    .draggable({
        onstart: function (event) {
            var box = event.target.parentElement;
            var rect = box.getBoundingClientRect();

            // store the center as the element has css `transform-origin: center center`
            box.setAttribute('data-center-x', rect.left + rect.width / 2);
            box.setAttribute('data-center-y', rect.top + rect.height / 2);
            // get the angle of the element when the drag starts
            box.setAttribute('data-angle', getDragAngle(event));
        },
        onmove: function (event) {
            var box = event.target.parentElement;

            var pos = {
                x: parseFloat(box.getAttribute('data-x')) || 0,
                y: parseFloat(box.getAttribute('data-y')) || 0
            };

            var angle = getDragAngle(event);

            // update transform style on dragmove
            box.style.transform = 'translate(' + pos.x + 'px, ' + pos.y + 'px) rotate(' + angle + 'rad' + ')';
        },
        onend: function (event) {
            var box = event.target.parentElement;

            // save the angle on dragend
            box.setAttribute('data-angle', getDragAngle(event));
        },
    })

function getDragAngle(event) {
    var box = event.target.parentElement;
    var startAngle = parseFloat(box.getAttribute('data-angle')) || 0;
    var center = {
        x: parseFloat(box.getAttribute('data-center-x')) || 0,
        y: parseFloat(box.getAttribute('data-center-y')) || 0
    };
    var angle = Math.atan2(center.y - event.clientY,
        center.x - event.clientX);

    return angle - startAngle;
}
function OpenCamera()
{
    let CameraIp=""; //Camera IP must Place Here
    window.open("CameraIp");
}
