// Interactive App Logic for B2B Pune Market Analytics Dashboard

const areaData = [
  { rank: 1, area_id: 'A001', taluka: 'Chakan', area_name: 'Chakan MIDC Phase 1-4', score: 86.13, category: 'High Opportunity', potential: 85.40, penetration: 21.38, sales: 128400000, gap: 'Distribution Gap', gapScore: 50.0, delayDays: 0.1, responseHrs: 7.2, dealers: 7, rec: 'Expand authorized dealer network, onboard 2+ local tier-1 distributors, and establish a local stocking hub.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 2, area_id: 'A003', taluka: 'Ranjangaon', area_name: 'Ranjangaon MIDC Industrial Hub', score: 76.96, category: 'High Opportunity', potential: 80.21, penetration: 7.20, sales: 48500000, gap: 'Service Gap', gapScore: 80.0, delayDays: 4.2, responseHrs: 64.5, dealers: 1, rec: 'Establish a localized regional micro-warehouse in Ranjangaon MIDC, enforce SLA performance penalties, and optimize dispatch logistics.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 3, area_id: 'A004', taluka: 'Pimpri-Chinchwad', area_name: 'PCPMC Auto Hub', score: 71.08, category: 'Medium Opportunity', potential: 89.63, penetration: 22.70, sales: 162000000, gap: 'Distribution Gap', gapScore: 30.0, delayDays: 0.2, responseHrs: 8.1, dealers: 6, rec: 'Optimize key enterprise customer retention and incentivize dealer expansion into high-tier automotive suppliers.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 4, area_id: 'A002', taluka: 'Talegaon', area_name: 'Talegaon Industrial Area', score: 68.58, category: 'Medium Opportunity', potential: 62.55, penetration: 16.30, sales: 54000000, gap: 'Service Gap', gapScore: 45.0, delayDays: 1.8, responseHrs: 24.0, dealers: 3, rec: 'Improve delivery fleet routing from Chakan hub and increase buffer stock for fast-moving bearings and motors.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 5, area_id: 'A005', taluka: 'Bhosari', area_name: 'Bhosari Industrial Estate', score: 62.18, category: 'Medium Opportunity', potential: 69.88, penetration: 21.21, sales: 98000000, gap: 'Service Gap', gapScore: 25.0, delayDays: 0.3, responseHrs: 9.5, dealers: 5, rec: 'Maintain current strong dealer incentive program while cross-selling automation and safety gear product categories.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 6, area_id: 'A006', taluka: 'Shirur', area_name: 'Shirur Industrial Zone', score: 61.39, category: 'Medium Opportunity', potential: 58.53, penetration: 7.65, sales: 29500000, gap: 'Service Gap', gapScore: 70.0, delayDays: 3.8, responseHrs: 52.0, dealers: 1, rec: 'Partner with regional logistics providers to solve Shirur delivery bottleneck and recruit an additional direct dealer.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 7, area_id: 'A009', taluka: 'Khed', area_name: 'Khed Auto Component Cluster', score: 60.98, category: 'Medium Opportunity', potential: 49.67, penetration: 16.20, sales: 38200000, gap: 'Service Gap', gapScore: 35.0, delayDays: 1.4, responseHrs: 21.5, dealers: 3, rec: 'Target mid-sized metal fabrication units with customized bulk pricing contracts.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 8, area_id: 'A013', taluka: 'Maval', area_name: 'Maval Heavy Fabrication Corridor', score: 60.41, category: 'Medium Opportunity', potential: 52.31, penetration: 16.03, sales: 41000000, gap: 'Service Gap', gapScore: 40.0, delayDays: 1.6, responseHrs: 22.0, dealers: 3, rec: 'Expand product range offering heavy-duty hydraulic pumps and helical gearboxes to heavy fabrication plants.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 9, area_id: 'A007', taluka: 'Baramati', area_name: 'Baramati High-Tech MIDC', score: 56.04, category: 'Medium Opportunity', potential: 44.78, penetration: 16.92, sales: 31000000, gap: 'Service Gap', gapScore: 30.0, delayDays: 1.2, responseHrs: 18.0, dealers: 2, rec: 'Focus sales outreach on agro-processing and textile machinery manufacturers.', cluster: 'Cluster 0: Mature Market Leaders' },
  { rank: 10, area_id: 'A011', taluka: 'Mulshi', area_name: 'Mulshi Light Manufacturing Zone', score: 45.59, category: 'Low Opportunity', potential: 15.02, penetration: 12.24, sales: 18500000, gap: 'Demand Gap', gapScore: 65.0, delayDays: 0.8, responseHrs: 16.0, dealers: 1, rec: 'Adopt a targeted key-account sales strategy rather than broad distribution expansion.', cluster: 'Cluster 3: Low Potential / Niche Markets' },
  { rank: 11, area_id: 'A010', taluka: 'Haveli', area_name: 'Haveli Engineering Belt', score: 40.16, category: 'Low Opportunity', potential: 17.56, penetration: 13.79, sales: 21000000, gap: 'Service Gap', gapScore: 45.0, delayDays: 1.1, responseHrs: 19.5, dealers: 2, rec: 'Maintain existing channel coverage without capital-intensive logistics investments.', cluster: 'Cluster 3: Low Potential / Niche Markets' },
  { rank: 12, area_id: 'A012', taluka: 'Purandar', area_name: 'Purandar Agri & Industrial Park', score: 34.56, category: 'Low Opportunity', potential: 4.37, penetration: 11.54, sales: 12400000, gap: 'Demand Gap', gapScore: 80.0, delayDays: 0.9, responseHrs: 17.0, dealers: 1, rec: 'Serve via remote catalog orders and third-party delivery.', cluster: 'Cluster 3: Low Potential / Niche Markets' },
  { rank: 13, area_id: 'A008', taluka: 'Daund', area_name: 'Daund Logistics & Industrial Belt', score: 29.78, category: 'Low Opportunity', potential: 0.76, penetration: 13.10, sales: 14200000, gap: 'Demand Gap', gapScore: 85.0, delayDays: 0.7, responseHrs: 15.0, dealers: 1, rec: 'Low macro demand density; maintain minimal direct sales coverage.', cluster: 'Cluster 3: Low Potential / Niche Markets' }
];

let matrixChart;

document.addEventListener('DOMContentLoaded', () => {
  renderTable(areaData);
  initMatrixChart(areaData);

  // Auto-select top opportunity area (Ranjangaon or Chakan) for detail card
  selectArea('A003');

  // Event Listeners
  document.getElementById('filter-category').addEventListener('change', filterData);
  document.getElementById('filter-gap').addEventListener('change', filterData);
});

function renderTable(data) {
  const tbody = document.getElementById('table-body');
  tbody.innerHTML = '';

  data.forEach((row) => {
    const tr = document.createElement('tr');
    tr.onclick = () => selectArea(row.area_id);

    let catClass = 'status-low';
    if (row.category === 'High Opportunity') catClass = 'status-high';
    else if (row.category === 'Medium Opportunity') catClass = 'status-medium';

    tr.innerHTML = `
      <td><strong>#${row.rank}</strong></td>
      <td><strong>${row.taluka}</strong></td>
      <td><strong>${row.score.toFixed(1)}</strong></td>
      <td><span class="status-badge ${catClass}">${row.category}</span></td>
      <td>${row.penetration.toFixed(1)}%</td>
      <td><span class="gap-badge">${row.gap}</span></td>
    `;
    tbody.appendChild(tr);
  });
}

function filterData() {
  const catFilter = document.getElementById('filter-category').value;
  const gapFilter = document.getElementById('filter-gap').value;

  const filtered = areaData.filter((row) => {
    const matchCat = catFilter === 'All' || row.category === catFilter;
    const matchGap = gapFilter === 'All' || row.gap === gapFilter;
    return matchCat && matchGap;
  });

  renderTable(filtered);
}

function selectArea(areaId) {
  const item = areaData.find((a) => a.area_id === areaId);
  if (!item) return;

  document.getElementById('detail-selected-area').innerText = `${item.taluka} (${item.area_id})`;

  const detailContent = document.getElementById('detail-content');
  detailContent.innerHTML = `
    <div class="detail-box">
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Industrial Hub Name:</span>
        <strong>${item.area_name}</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Opportunity Score & Tier:</span>
        <strong style="color:var(--accent-blue);">${item.score.toFixed(1)} / 100 (${item.category})</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Market Potential Score:</span>
        <strong>${item.potential.toFixed(1)} / 100</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Current Market Penetration:</span>
        <strong style="color: ${item.penetration < 10 ? 'var(--accent-rose)' : 'var(--accent-emerald)'};">${item.penetration.toFixed(1)}% (Gap: ${(100 - item.penetration).toFixed(1)}%)</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Active Dealer Network:</span>
        <strong>${item.dealers} active dealer(s)</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Avg Delivery Delay:</span>
        <strong style="color:${item.delayDays > 2 ? 'var(--accent-rose)' : 'var(--text-main)'};">${item.delayDays.toFixed(1)} days</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Avg Service Response Time:</span>
        <strong>${item.responseHrs.toFixed(1)} hours</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Primary Root Cause Bottleneck:</span>
        <strong style="color:var(--accent-purple);">${item.gap}</strong>
      </div>
      <div class="detail-metric">
        <span style="color:var(--text-muted);">Scikit-Learn ML Cluster:</span>
        <strong>${item.cluster}</strong>
      </div>
    </div>
    <div class="recommendation-banner">
      <strong>🎯 Strategic Business Recommendation:</strong><br>
      ${item.rec}
    </div>
  `;
}

function initMatrixChart(data) {
  const ctx = document.getElementById('matrixChart').getContext('2d');

  const points = data.map((d) => ({
    x: d.potential,
    y: d.penetration,
    label: d.taluka,
    score: d.score
  }));

  matrixChart = new Chart(ctx, {
    type: 'scatter',
    data: {
      datasets: [
        {
          label: 'Pune Industrial Areas',
          data: points,
          backgroundColor: (ctx) => {
            const val = ctx.raw ? ctx.raw.score : 50;
            if (val >= 75) return '#34d399';
            if (val >= 50) return '#fbbf24';
            return '#f43f5e';
          },
          pointRadius: 10,
          pointHoverRadius: 14
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const p = ctx.raw;
              return `${p.label}: Potential ${p.x.toFixed(1)}, Penetration ${p.y.toFixed(1)}% (Opp Score: ${p.score.toFixed(1)})`;
            }
          }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Market Potential Score (0-100)', color: '#94a3b8' },
          grid: { color: 'rgba(255, 255, 255, 0.1)' },
          ticks: { color: '#94a3b8' },
          min: 0,
          max: 100
        },
        y: {
          title: { display: true, text: 'Current Penetration Rate (%)', color: '#94a3b8' },
          grid: { color: 'rgba(255, 255, 255, 0.1)' },
          ticks: { color: '#94a3b8' },
          min: 0,
          max: 30
        }
      }
    }
  });
}
