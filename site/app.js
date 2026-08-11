const repoBase = "https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts/blob/main/";

const els = {
  summaryText: document.querySelector("#summaryText"),
  metricVideos: document.querySelector("#metricVideos"),
  metricTranscripts: document.querySelector("#metricTranscripts"),
  metricAccounts: document.querySelector("#metricAccounts"),
  metricImported: document.querySelector("#metricImported"),
  queryInput: document.querySelector("#queryInput"),
  accountInput: document.querySelector("#accountInput"),
  personInput: document.querySelector("#personInput"),
  statusSelect: document.querySelector("#statusSelect"),
  resetButton: document.querySelector("#resetButton"),
  resultCount: document.querySelector("#resultCount"),
  resultsBody: document.querySelector("#resultsBody"),
  accountCount: document.querySelector("#accountCount"),
  accountsBody: document.querySelector("#accountsBody"),
  peopleCount: document.querySelector("#peopleCount"),
  peopleBody: document.querySelector("#peopleBody"),
};

let siteData = null;

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
  return repoBase + path.split("/").map(encodeURIComponent).join("/");
}

function statusLabel(status) {
  if (status === "imported") return "外部迁移";
  if (status === "canonical") return "本地";
  return status || "未标注";
}

function peopleText(record) {
  return record.featured_people && record.featured_people.length ? record.featured_people.join("、") : "未标注";
}

function renderMetrics(data) {
  const counts = data.counts;
  els.metricVideos.textContent = counts.source_records || counts.unique_video_ids;
  els.metricTranscripts.textContent = counts.transcript_files;
  els.metricAccounts.textContent = counts.account_pages;
  els.metricImported.textContent = counts.imported_transcripts;
  els.summaryText.textContent = `最新发布：${counts.latest_published || "未标注"} · 按视频 ID / source_id 去重展示 ${counts.source_records || counts.unique_video_ids} 条记录`;
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
  const records = siteData.records.filter((record) => matches(record, filters));
  els.resultCount.textContent = `${records.length} / ${siteData.records.length} 条`;

  if (!records.length) {
    els.resultsBody.innerHTML = `<tr><td class="empty" colspan="6">没有匹配结果</td></tr>`;
    return;
  }

  els.resultsBody.innerHTML = records
    .map((record) => {
      const analysisLink = record.analysis_path
        ? `<a href="${repoUrl(record.analysis_path)}" target="_blank" rel="noreferrer">分析</a>`
        : "";
      const youtubeLink = record.source_url
        ? `<a href="${escapeHtml(record.source_url)}" target="_blank" rel="noreferrer">视频</a>`
        : "";
      const variantLabel = record.variant_count > 1 ? ` · ${record.variant_count} 个版本` : "";
      return `
        <tr>
          <td class="title-cell">
            <strong>${escapeHtml(record.title)}</strong>
            <small>${escapeHtml(record.video_id || record.source_id || "无来源 ID")}${variantLabel}</small>
          </td>
          <td><a href="${repoUrl(`accounts/${record.account_slug}.md`)}" target="_blank" rel="noreferrer">${escapeHtml(record.account_name)}</a></td>
          <td class="people-list">${escapeHtml(peopleText(record))}</td>
          <td>${escapeHtml(record.published || "未标注")}</td>
          <td><span class="badge">${escapeHtml(statusLabel(record.status || "canonical"))}</span></td>
          <td class="link-list">
            <a href="${repoUrl(record.path)}" target="_blank" rel="noreferrer">逐字稿</a>
            ${analysisLink}
            ${youtubeLink}
          </td>
        </tr>
      `;
    })
    .join("");
}

function renderAccounts(data) {
  els.accountCount.textContent = `${data.accounts.length} 个`;
  const rows = [...data.accounts].sort((a, b) => b.transcript_count - a.transcript_count || a.name.localeCompare(b.name, "zh-CN"));
  els.accountsBody.innerHTML = rows
    .map(
      (account) => `
        <tr>
          <td><a href="${repoUrl(account.path)}" target="_blank" rel="noreferrer">${escapeHtml(account.name)}</a></td>
          <td>${account.transcript_count}</td>
          <td>${escapeHtml(account.latest_published || "未标注")}</td>
        </tr>
      `,
    )
    .join("");
}

function renderPeople(data) {
  els.peopleCount.textContent = `${data.people.length} 个`;
  const rows = [...data.people].sort((a, b) => b.appearance_count - a.appearance_count || a.name.localeCompare(b.name, "zh-CN"));
  els.peopleBody.innerHTML = rows
    .map(
      (person) => `
        <tr>
          <td><a href="${repoUrl(person.path)}" target="_blank" rel="noreferrer">${escapeHtml(person.name)}</a></td>
          <td>${person.appearance_count}</td>
          <td>${escapeHtml(person.latest_published || "未标注")}</td>
        </tr>
      `,
    )
    .join("");
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
}

async function init() {
  bindEvents();
  const response = await fetch("data.json");
  siteData = await response.json();
  renderMetrics(siteData);
  renderAccounts(siteData);
  renderPeople(siteData);
  renderResults();
}

init().catch((error) => {
  els.summaryText.textContent = "数据载入失败";
  els.resultsBody.innerHTML = `<tr><td class="empty" colspan="6">${escapeHtml(error.message)}</td></tr>`;
});
