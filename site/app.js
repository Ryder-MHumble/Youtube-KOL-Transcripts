const repoBase = "https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts/blob/main/";

const els = {
  summaryText: document.querySelector("#summaryText"),
  heroMetrics: document.querySelector("#heroMetrics"),
  queryInput: document.querySelector("#queryInput"),
  accountInput: document.querySelector("#accountInput"),
  personInput: document.querySelector("#personInput"),
  statusSelect: document.querySelector("#statusSelect"),
  resetButton: document.querySelector("#resetButton"),
  resultCount: document.querySelector("#resultCount"),
  resultsBody: document.querySelector("#resultsBody"),
  accountCount: document.querySelector("#accountCount"),
  accountChips: document.querySelector("#accountChips"),
  peopleCount: document.querySelector("#peopleCount"),
  personChips: document.querySelector("#personChips"),
  moduleGrid: document.querySelector("#moduleGrid"),
  detailPanel: document.querySelector("#detailPanel"),
  latestPublished: document.querySelector("#latestPublished"),
  uniqueVideoCount: document.querySelector("#uniqueVideoCount"),
  importedCount: document.querySelector("#importedCount"),
  analysisCount: document.querySelector("#analysisCount"),
  selectionHint: document.querySelector("#selectionHint"),
  schemaBlock: document.querySelector("#schemaBlock code"),
};

let siteData = null;
let visibleRecords = [];
let selectedKey = "";

function normalize(value) {
  return String(value || "").normalize("NFKC").toLowerCase().trim();
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function repoUrl(path) {
  return repoBase + String(path || "").split("/").map(encodeURIComponent).join("/");
}

function formatNumber(value) {
  return new Intl.NumberFormat("zh-CN").format(Number(value || 0));
}

function statusLabel(status) {
  if (status === "imported") return "归档纳入";
  if (status === "canonical") return "本地验证";
  return status || "未标注";
}

function statusClass(status) {
  return status === "imported" ? "is-imported" : "is-canonical";
}

function peopleText(record) {
  return record.featured_people && record.featured_people.length ? record.featured_people.join("、") : "未标注";
}

function recordKey(record) {
  return record.video_id || record.source_id || record.path;
}

function idText(record) {
  if (record.video_id) return `video_id: ${record.video_id}`;
  if (record.source_id) return `source_id: ${record.source_id}`;
  return "来源标识：仓库路径";
}

function internalLinks(record) {
  const links = [
    `<a class="pill-link" href="${repoUrl(record.path)}" target="_blank" rel="noreferrer">逐字稿</a>`,
    `<a class="pill-link" href="${repoUrl(`accounts/${record.account_slug}.md`)}" target="_blank" rel="noreferrer">账号页</a>`,
  ];
  if (record.analysis_path) {
    links.splice(1, 0, `<a class="pill-link" href="${repoUrl(record.analysis_path)}" target="_blank" rel="noreferrer">分析</a>`);
  }
  return links.join("");
}

function renderMetrics(data) {
  const counts = data.counts;
  const sourceRecords = counts.source_records || counts.unique_video_ids || data.records.length;
  els.summaryText.textContent = `最新发布：${counts.latest_published || "未标注"} · 当前公开索引 ${formatNumber(sourceRecords)} 条记录`;

  const metrics = [
    ["逐字稿文件", counts.transcript_files],
    ["检索条目", sourceRecords],
    ["账号索引", counts.account_pages],
    ["人物索引", counts.people_pages || data.people.length],
  ];
  els.heroMetrics.innerHTML = metrics
    .map(
      ([label, value]) => `
        <div class="metric-card">
          <strong>${formatNumber(value)}</strong>
          <span>${escapeHtml(label)}</span>
        </div>
      `,
    )
    .join("");

  els.latestPublished.textContent = counts.latest_published || "未标注";
  els.uniqueVideoCount.textContent = formatNumber(counts.unique_video_ids);
  els.importedCount.textContent = formatNumber(counts.imported_transcripts);
  els.analysisCount.textContent = formatNumber(counts.analysis_files);

  els.schemaBlock.textContent = JSON.stringify(
    {
      counts: {
        transcript_files: counts.transcript_files,
        source_records: sourceRecords,
        unique_video_ids: counts.unique_video_ids,
        non_youtube_sources: counts.non_youtube_sources,
        account_pages: counts.account_pages,
        indexed_people: counts.people_pages || data.people.length,
        people_markdown_files: counts.people_markdown_files,
        analysis_files: counts.analysis_files,
        imported_records: counts.imported_transcripts,
      },
      record: {
        title: "标题",
        account_name: "账号",
        source_id: "source_id",
        video_id: "video_id",
        status: "canonical | imported",
        path: "仓库内逐字稿路径",
      },
    },
    null,
    2,
  );
}

function renderModules(data) {
  const counts = data.counts;
  const sourceRecords = counts.source_records || counts.unique_video_ids || data.records.length;
  const modules = [
    ["逐字稿库", counts.transcript_files, "完整 Markdown 逐字稿，带元数据与时间戳。"],
    ["检索目录", sourceRecords, "按 video_id / source_id 去重后的公开查询条目。"],
    ["分析库", counts.analysis_files, "结构化 KOL 分析、观点抽取和交叉引用。"],
    ["账号索引", counts.account_pages, "按发布账号聚合访谈，支持账号级检索。"],
    ["人物节点", counts.people_pages || data.people.length, "按 featured_people 组织的 KOL / 嘉宾索引。"],
    ["归档纳入", counts.imported_transcripts, "已纳入仓库的归档语料，状态与来源标识保留。"],
  ];

  els.moduleGrid.innerHTML = modules
    .map(
      ([title, count, text]) => `
        <article class="module-card">
          <span>${formatNumber(count)}</span>
          <h3>${escapeHtml(title)}</h3>
          <p>${escapeHtml(text)}</p>
        </article>
      `,
    )
    .join("");
}

function renderChips(data) {
  els.accountCount.textContent = `${formatNumber(data.accounts.length)} 个`;
  els.peopleCount.textContent = `${formatNumber(data.people.length)} 个`;

  const accounts = [...data.accounts]
    .sort((a, b) => b.transcript_count - a.transcript_count || a.name.localeCompare(b.name, "zh-CN"))
    .slice(0, 14);
  const people = [...data.people]
    .sort((a, b) => b.appearance_count - a.appearance_count || a.name.localeCompare(b.name, "zh-CN"))
    .slice(0, 14);

  els.accountChips.innerHTML = accounts
    .map(
      (account) => `
        <button class="chip" type="button" data-filter="account" data-value="${escapeHtml(account.name)}">
          <span>${escapeHtml(account.name)}</span>
          <strong>${formatNumber(account.transcript_count)}</strong>
        </button>
      `,
    )
    .join("");

  els.personChips.innerHTML = people
    .map(
      (person) => `
        <button class="chip" type="button" data-filter="person" data-value="${escapeHtml(person.name)}">
          <span>${escapeHtml(person.name)}</span>
          <strong>${formatNumber(person.appearance_count)}</strong>
        </button>
      `,
    )
    .join("");
}

function currentFilters() {
  return {
    query: normalize(els.queryInput.value),
    account: normalize(els.accountInput.value),
    person: normalize(els.personInput.value),
    status: normalize(els.statusSelect.value),
  };
}

function matches(record, filters) {
  const searchText = normalize(record.search_text);
  const people = normalize(peopleText(record));
  const account = normalize(`${record.account_name} ${record.account_slug} ${record.title} ${record.search_text}`);
  const status = normalize(record.status || "canonical");
  if (filters.query && !searchText.includes(filters.query)) return false;
  if (filters.account && !account.includes(filters.account)) return false;
  if (filters.person && !`${people} ${searchText}`.includes(filters.person)) return false;
  if (filters.status && status !== filters.status) return false;
  return true;
}

function renderResults() {
  if (!siteData) return;
  const filters = currentFilters();
  visibleRecords = siteData.records.filter((record) => matches(record, filters));
  els.resultCount.textContent = `${formatNumber(visibleRecords.length)} / ${formatNumber(siteData.records.length)} 条`;

  if (!visibleRecords.length) {
    selectedKey = "";
    els.resultsBody.innerHTML = `<div class="empty">没有匹配结果。可以尝试只输入账号、人物名或 video_id 的一部分。</div>`;
    renderDetail(null);
    return;
  }

  if (!visibleRecords.some((record) => recordKey(record) === selectedKey)) {
    selectedKey = recordKey(visibleRecords[0]);
  }

  els.resultsBody.innerHTML = visibleRecords
    .map((record) => {
      const key = recordKey(record);
      const selected = key === selectedKey;
      const variantLabel = record.variant_count > 1 ? ` · ${record.variant_count} 个版本` : "";
      return `
        <article class="record-card ${selected ? "is-selected" : ""}" tabindex="0" role="button" aria-pressed="${selected}" data-key="${escapeHtml(key)}">
          <div class="record-main">
            <span class="badge ${statusClass(record.status || "canonical")}">${escapeHtml(statusLabel(record.status || "canonical"))}</span>
            <h3>${escapeHtml(record.title)}</h3>
            <p>${escapeHtml(idText(record))}${escapeHtml(variantLabel)}</p>
          </div>
          <dl class="record-meta">
            <div><dt>账号</dt><dd>${escapeHtml(record.account_name || "未标注")}</dd></div>
            <div><dt>人物</dt><dd>${escapeHtml(peopleText(record))}</dd></div>
            <div><dt>发布</dt><dd>${escapeHtml(record.published || "未标注")}</dd></div>
          </dl>
          <div class="record-links">${internalLinks(record)}</div>
        </article>
      `;
    })
    .join("");

  renderDetail(visibleRecords.find((record) => recordKey(record) === selectedKey));
}

function renderDetail(record) {
  if (!record) {
    els.selectionHint.textContent = "没有选中条目";
    els.detailPanel.innerHTML = `
      <div class="detail-empty">
        <p class="eyebrow">详情</p>
        <h2>等待选择</h2>
        <p>筛选结果为空，调整关键词后会自动显示第一条匹配记录。</p>
      </div>
    `;
    return;
  }

  els.selectionHint.textContent = record.title;
  const variants =
    record.variant_paths && record.variant_paths.length
      ? record.variant_paths.map((path) => `<li>${escapeHtml(path)}</li>`).join("")
      : `<li>${escapeHtml(record.path)}</li>`;

  els.detailPanel.innerHTML = `
    <p class="eyebrow">当前条目</p>
    <h2>${escapeHtml(record.title)}</h2>
    <div class="detail-status">
      <span class="badge ${statusClass(record.status || "canonical")}">${escapeHtml(statusLabel(record.status || "canonical"))}</span>
      <span>${escapeHtml(idText(record))}</span>
    </div>
    <dl class="detail-list">
      <div><dt>账号</dt><dd>${escapeHtml(record.account_name || "未标注")}</dd></div>
      <div><dt>人物</dt><dd>${escapeHtml(peopleText(record))}</dd></div>
      <div><dt>发布时间</dt><dd>${escapeHtml(record.published || "未标注")}</dd></div>
      <div><dt>逐字稿路径</dt><dd>${escapeHtml(record.path)}</dd></div>
      <div><dt>分析路径</dt><dd>${escapeHtml(record.analysis_path || "未生成")}</dd></div>
    </dl>
    <div class="detail-links">${internalLinks(record)}</div>
    <details class="variant-box">
      <summary>仓库版本路径：${formatNumber(record.variant_count || 1)} 个</summary>
      <ul>${variants}</ul>
    </details>
  `;
}

function selectRecord(key) {
  selectedKey = key;
  renderResults();
}

function bindEvents() {
  [els.queryInput, els.accountInput, els.personInput, els.statusSelect].forEach((el) => {
    el.addEventListener("input", renderResults);
  });

  els.resetButton.addEventListener("click", () => {
    els.queryInput.value = "";
    els.accountInput.value = "";
    els.personInput.value = "";
    els.statusSelect.value = "";
    renderResults();
    els.queryInput.focus();
  });

  document.addEventListener("click", (event) => {
    const chip = event.target.closest(".chip");
    if (chip) {
      if (chip.dataset.filter === "account") {
        els.accountInput.value = chip.dataset.value || "";
      }
      if (chip.dataset.filter === "person") {
        els.personInput.value = chip.dataset.value || "";
      }
      renderResults();
      const motion = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
      document.querySelector("#search").scrollIntoView({ block: "start", behavior: motion });
      return;
    }

    const card = event.target.closest(".record-card");
    if (card && !event.target.closest("a")) {
      selectRecord(card.dataset.key);
    }
  });

  document.addEventListener("keydown", (event) => {
    const card = event.target.closest(".record-card");
    if (card && (event.key === "Enter" || event.key === " ")) {
      event.preventDefault();
      selectRecord(card.dataset.key);
    }
  });
}

async function init() {
  bindEvents();
  const response = await fetch("data.json");
  if (!response.ok) throw new Error(`data.json HTTP ${response.status}`);
  siteData = await response.json();
  renderMetrics(siteData);
  renderModules(siteData);
  renderChips(siteData);
  renderResults();
}

init().catch((error) => {
  els.summaryText.textContent = "数据载入失败";
  els.resultsBody.innerHTML = `<div class="empty">${escapeHtml(error.message)}</div>`;
  renderDetail(null);
});
