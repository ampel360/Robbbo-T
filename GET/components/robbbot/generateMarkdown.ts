export function generateMarkdown(logs: { code: string; description: string; status: string }[]) {
  const now = new Date().toLocaleString('es-ES');

  const table = logs
    .map(log => `| ${log.code} | ${log.description} | ${log.status} |`)
    .join('\n');

  const status = logs.some(l => l.status.includes('❌')) ? '⚠️ Requiere atención' : '🟢 Operativo';

  return `
# ✅ Robbbo-T Operational Success Log

**Última actualización**: ${now}

## Escenarios registrados

| Código | Evento | Resultado |
|--------|--------|-----------|
${table}

---

**Estado del Sistema**: ${status}

Versión: \`ROBBO-T-GAIA-ICSDB-001\`
`;
}
