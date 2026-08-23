<div align="center">

<img src="./assets/banner_header.svg" width="100%"/>

**[0] whoami\*&nbsp;&nbsp;&nbsp;[1] skills&nbsp;&nbsp;&nbsp;[2] projects&nbsp;&nbsp;&nbsp;[3] status&nbsp;&nbsp;&nbsp;[4] contact**&nbsp;&nbsp;·&nbsp;&nbsp;120×32&nbsp;&nbsp;·&nbsp;&nbsp;zsh

</div>

<br>

<!-- ══════════ PANE 0 — whoami ══════════ -->
<img src="./assets/headers/pane_whoami.svg" width="100%"/>

<table width="100%">
<tr>
<td width="68%" valign="top">

```console
$ whoami
karima — DevOps & SRE Engineer

$ cat philosophy.txt
Infrastructure should be automated, observable and boring.
If it's exciting, it's probably an incident.

$ echo $CURRENT_FOCUS
platform-reliability · gitops-delivery · alerts→root-cause

$ uptime
up 4 years,  load average: 0.42, 0.31, 0.28
```

</td>
<td width="32%" align="center" valign="top">

<img src="./assets/headers/webcam_bar.svg" width="190"/>

<img src="./assets/karima_pixel_avatar_circle.gif" width="150" alt="Karima pixel avatar"/>

`[LIVE]` 🟢

[![followers](https://img.shields.io/github/followers/KarimaTaira?style=flat-square&label=followers&color=5CF19E&labelColor=0A0E14)](https://github.com/KarimaTaira)
![views](https://komarev.com/ghpvc/?username=KarimaTaira&style=flat-square&color=F2B84B&labelColor=0A0E14&label=views)

</td>
</tr>
</table>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=17&duration=3000&pause=900&color=5CF19E&center=true&vCenter=true&width=660&lines=kubectl+apply+-f+reliability.yaml;terraform+plan+%E2%86%92+terraform+apply+%E2%86%92+sleep;observability+is+not+optional;git+push+%E2%86%92+deploy+%E2%86%92+observe+%E2%86%92+improve" alt="Typing SVG" />

</div>

<br>

<!-- ══════════ PANE 1 — skills ══════════ -->
<img src="./assets/headers/pane_skills.svg" width="100%"/>

```console
$ ls -l ./skills --group-by=domain

drwxr-xr-x  cloud-infra/     aws · terraform · kubernetes(eks) · helm · kustomize
drwxr-xr-x  delivery/        github-actions · argo-cd · gitops · release-eng
drwxr-xr-x  observability/   prometheus · grafana · opentelemetry · loki · tempo
drwxr-xr-x  reliability/     slo-design · alerting · incident-response · triage

4 directories, 21 tools

$ tree ./stack -L 1
stack/
├── cloud/          aws · terraform · eks
├── containers/     docker · kubernetes · helm
├── delivery/       github-actions · argo-cd
├── observability/  prometheus · grafana · loki · tempo
├── languages/      python · bash
└── data/           postgres · nginx
```

<br>

<!-- ══════════ PANE 2 — projects ══════════ -->
<img src="./assets/headers/pane_projects.svg" width="100%"/>

```console
$ git log --stat --author=karima --oneline

a3f9c21  feat(cloud-infra): AWS/EKS platform, IaC end-to-end
         terraform/  eks/  modules/          | 128 ++++++++++++++++++
         → reliability, cost optimization, automation over manual toil

7b2e440  feat(observability): metrics, logs and distributed traces
         prometheus/  grafana/  tempo/       |  96 ++++++++++++
         → incident diagnosis: hours → minutes

e51d8a3  feat(gitops): Argo CD delivery pipeline
         argocd/  helm/  .github/workflows/  |  74 +++++++++
         → every release repeatable, reviewable, reversible

3 commits, 3 files changed, 298 insertions(+)
```

<br>

<!-- ══════════ PANE 3 — status ══════════ -->
<img src="./assets/headers/pane_status.svg" width="100%"/>

```console
$ systemctl status karima.service

● karima.service — DevOps & SRE Engineer
     Loaded: loaded (/etc/systemd/system/karima.service; enabled)
     Active: active (running)
   Main PID: 1337 (kubectl)
     Status: "watching prod, sleeping fine"

$ tail -f ~/status.log
```

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=KarimaTaira&show_icons=true&hide_border=true&theme=tokyonight&bg_color=0F1520&title_color=5CF19E&icon_color=F2B84B&text_color=7A8699" width="58%"/>

</div>

<br>

<!-- ══════════ PANE 4 — contact ══════════ -->
<img src="./assets/headers/pane_contact.svg" width="100%"/>

```console
$ curl -s https://karima.dev/health | jq
{
  "cloud":          "ok",
  "kubernetes":     "ok",
  "cicd":           "ok",
  "observability":  "ok",
  "coffee":         "critical"
}

$ connect --with=karima
resolving endpoints... 3 found
```

<div align="center">

**[`→ linkedin`](https://www.linkedin.com/in/KarimaTaira)** &nbsp;&nbsp;·&nbsp;&nbsp; **[`→ email`](mailto:taira.karima21@gmail.com)** &nbsp;&nbsp;·&nbsp;&nbsp; **[`→ github`](https://github.com/KarimaTaira)**

</div>

<br>

<div align="center">

**[0] whoami&nbsp;&nbsp;&nbsp;[1] skills&nbsp;&nbsp;&nbsp;[2] projects&nbsp;&nbsp;&nbsp;[3] status\*&nbsp;&nbsp;&nbsp;[4] contact**&nbsp;&nbsp;·&nbsp;&nbsp;karima@devops-01&nbsp;&nbsp;·&nbsp;&nbsp;exit 0

<sub>built with ☕, YAML, and a questionable amount of `kubectl`.</sub>

</div>

<img src="./assets/banner_footer.svg" width="100%"/>