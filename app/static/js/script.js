/**
 * ฟังก์ชันสำหรับแปลงข้อความสูตรเคมีให้มีตัวห้อย (Subscript) อัตโนมัติ
 * รองรับตัวเลข, ตัวแปร n, และเครื่องหมายบวก/ลบ ในสูตรทั่วไป
 */
function applySubscripts() {
  const formulas = document.querySelectorAll('.formula-render');

  formulas.forEach(el => {
    let text = el.innerText;

    // ปรับ Regex ใหม่:
    // (?:[A-Z][a-z]?|\)) : ส่วนแรกให้จับ "ธาตุ" หรือ "วงเล็บปิด )"
    // ([0-9n]+(?:[+\-][0-9n]+)*) : ส่วนที่สองจับตัวเลข/n/เครื่องหมาย เหมือนเดิม
    let formatted = text.replace(/(?:([A-Z][a-z]?)|(\)))([0-9n]+(?:[+\-][0-9n]+)*)/g, function(match, element, bracket, subscript) {
        // ถ้าเจอธาตุ ให้เอาธาตุมาต่อด้วยตัวห้อย
        // ถ้าเจอวงเล็บ ให้เอาวงเล็บมาต่อด้วยตัวห้อย
        let prefix = element ? element : bracket;
        return prefix + '<sub>' + subscript + '</sub>';
    });

    el.innerHTML = formatted;
  });
}

// เรียกใช้งานเมื่อโครงสร้าง DOM โหลดเสร็จสมบูรณ์
document.addEventListener('DOMContentLoaded', applySubscripts);