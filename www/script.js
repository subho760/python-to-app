const btn = document.getElementById('dragon-btn');
const hole = document.getElementById('dragon-hole');
const canvas = document.getElementById('dragon-canvas');
const ctx = canvas.getContext('2d');

// Set canvas size
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

let dragonActive = false;
let holeX = window.innerWidth / 2;
let holeY = window.innerHeight / 2;

// Target position for the head to move towards
let targetX = holeX;
let targetY = holeY;

// Dragon segment details
const N = 15; // Number of body segments
let segments = [];

// Initialize segments tucked away inside the hole location
function initSegments() {
    segments = [];
    for (let i = 0; i < N; i++) {
        segments.push({ x: holeX, y: holeY, radius: i === 0 ? 16 : 14 - i * 0.5 });
    }
}
initSegments();

// Phase 1: Tap Button -> Morph to Hole
btn.addEventListener('click', () => {
    btn.style.transform = "scale(0)";
    setTimeout(() => {
        btn.classList.add('hidden');
        hole.classList.remove('hidden');
        setTimeout(() => {
            hole.classList.add('active');
            dragonActive = true;
            // Skeleton head pops up looking slightly out
            targetX = holeX;
            targetY = holeY - 15; 
        }, 50);
    }, 400);
});

// Phase 2: Screen Tap Processing
window.addEventListener('touchstart', handleTap);
window.addEventListener('mousedown', handleTap);

function handleTap(e) {
    if (!dragonActive) return;
    
    // Get correct pointer coordinates
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;

    // Check if user tapped directly on the Dragon's Head
    const head = segments[0];
    const distToHead = Math.hypot(clientX - head.x, clientY - head.y);

    if (distToHead < 30 && (head.x !== holeX || head.y !== holeY)) {
        // Phase 3: Head Tapped -> Return to Hole and reset button
        targetX = holeX;
        targetY = holeY;
        return;
    }

    // Set new target for dragon to fly towards
    targetX = clientX;
    targetY = clientY;
}

// Animation loop handling physics and rendering
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (dragonActive) {
        // 1. Move the Dragon Head towards target smoothly
        segments[0].x += (targetX - segments[0].x) * 0.1;
        segments[0].y += (targetY - segments[0].y) * 0.1;

        // Check if returning dragon reached home base hole
        if (targetX === holeX && targetY === holeY && Math.hypot(segments[0].x - holeX, segments[0].y - holeY) < 2) {
            resetToButton();
        }

        // 2. Make body segments trail sequentially behind the leader
        for (let i = 1; i < N; i++) {
            const prev = segments[i - 1];
            const curr = segments[i];
            
            // Calculate distance between current and previous segment
            const dx = prev.x - curr.x;
            const dy = prev.y - curr.y;
            const distance = Math.hypot(dx, dy);
            const targetDist = 18; // Desired distance between pieces

            if (distance > targetDist) {
                // Drag segment along
                curr.x += (dx / distance) * (distance - targetDist);
                curr.y += (dy / distance) * (distance - targetDist);
            }
        }

        // 3. Render Dragon Graphics
        for (let i = N - 1; i >= 0; i--) {
            ctx.beginPath();
            ctx.arc(segments[i].x, segments[i].y, segments[i].radius, 0, Math.PI * 2);
            
            if (i === 0) {
                // Dragon Head Styling (Glow-in-the-dark green face)
                ctx.fillStyle = '#00ff87';
                ctx.shadowColor = '#00ff87';
                ctx.shadowBlur = 15;
            } else if (i === 4 || i === 8) {
                // Mid fins
                ctx.fillStyle = '#14aa6b';
                ctx.shadowBlur = 5;
            } else {
                // Trail scales
                ctx.fillStyle = 'rgba(0, 255, 135, ' + (1 - i / N) + ')';
                ctx.shadowBlur = 0;
            }
            ctx.fill();
            ctx.closePath();
        }
        ctx.shadowBlur = 0; // reset blur for other processes
    }

    requestAnimationFrame(animate);
}

function resetToButton() {
    dragonActive = false;
    hole.classList.remove('active');
    setTimeout(() => {
        hole.classList.add('hidden');
        btn.classList.remove('hidden');
        setTimeout(() => {
            btn.style.transform = "scale(1)";
            initSegments();
        }, 50);
    }, 400);
}

animate();

