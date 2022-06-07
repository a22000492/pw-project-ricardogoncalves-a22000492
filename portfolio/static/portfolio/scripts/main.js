"use strict";

const APP = {
  zeroFill: function(num) {
    return ('0' + num).slice(-2);
  },
  init: function() {
    const timeSlot = document.querySelector('.time-slot');
    const _this = this;
    setInterval(() => {
      const now = new Date();
      const fullTime = ` | ${_this.zeroFill(now.getUTCDate())}/${_this.zeroFill((now.getMonth() + 1))}/${now.getFullYear()} ${_this.zeroFill(now.getHours())}:${_this.zeroFill(now.getMinutes())}:${_this.zeroFill(now.getSeconds())}`;
      timeSlot.innerText = fullTime;
    }, 1000);
  },
};

document.addEventListener('DOMContentLoaded', APP.init());
