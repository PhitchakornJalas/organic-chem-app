/**
 * ฟังก์ชันสำหรับแปลงข้อความสูตรเคมีให้มีตัวห้อย (Subscript) อัตโนมัติ
 * รองรับตัวเลข, ตัวแปร n, และเครื่องหมายบวก/ลบ ในสูตรทั่วไป
 */
function applySubscripts() {
  const formulas = document.querySelectorAll('.formula-render');

  formulas.forEach(el => {
    let text = el.innerText;

    // Regex ตัวนี้จะมองหา:
    // 1. ตัวอักษรธาตุ ([A-Z][a-z]?)
    // 2. ตามด้วยกลุ่มของ ตัวเลข, n, +, - ที่ผสมกันอยู่ ([0-9n+\-]+)
    let formatted = text.replace(/([A-Z][a-z]?)([0-9n+\-]+)/g, '$1<sub>$2</sub>');

    el.innerHTML = formatted;
  });
}

// เรียกใช้งานเมื่อโครงสร้าง DOM โหลดเสร็จสมบูรณ์
document.addEventListener('DOMContentLoaded', applySubscripts);