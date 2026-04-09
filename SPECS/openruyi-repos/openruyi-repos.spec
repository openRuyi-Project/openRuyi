# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%if %{undefined _vendor_repo_url}
%global _vendor_repo_url https://repo.build.openruyi.cn/openruyi/\\$basearch/
%endif

Name:           openruyi-repos
Version:        3
Release:        %autorelease
Summary:        openRuyi repository files
License:        MulanPSL-2.0
URL:            https://www.openruyi.cn

Provides:       system-repos
Provides:       openRuyi-repos

%description
This package contains the repository files for %{_vendor}.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/

cat >> %{_vendor}.repo <<EOF
[Base]
name=%{_vendor} Base
baseurl=%{_vendor_repo_url}
enabled=1
gpgcheck=0
EOF

cat %{_vendor}.repo

install -c -m 644 %{_vendor}.repo %{buildroot}%{_sysconfdir}/yum.repos.d/%{_vendor}.repo

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum.repos.d/%{_vendor}.repo

%changelog
%autochangelog
