/**
 * ฟังก์ชันสำหรับแปลงข้อความสูตรเคมีให้มีตัวห้อย (Subscript) อัตโนมัติ
 * รองรับตัวเลข, ตัวแปร n, และเครื่องหมายบวก/ลบ ในสูตรทั่วไป
 */
function applySubscripts() {
  const formulas = document.querySelectorAll('.formula-render');

  formulas.forEach(el => {
    let text = el.innerText;

    // Regex ตัวนี้จะแบ่งงานเป็น 2 ส่วน:
    // 1. ([A-Z][a-z]?) : จับตัวธาตุ (C, H, O)
    // 2. ([0-9n]+(?:[+\-][0-9n]+)*) : จับตัวเลขหรือ n 
    //    และจะจับ + หรือ - ก็ต่อเมื่อมีตัวเลข/n ตามหลังต่อเท่านั้น
    let formatted = text.replace(/([A-Z][a-z]?)([0-9n]+(?:[+\-][0-9n]+)*)/g, '$1<sub>$2</sub>');

    el.innerHTML = formatted;
  });
}

// เรียกใช้งานเมื่อโครงสร้าง DOM โหลดเสร็จสมบูรณ์
document.addEventListener('DOMContentLoaded', applySubscripts);