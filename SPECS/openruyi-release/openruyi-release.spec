# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openruyi-release
Version:        2
Release:        %autorelease
Summary:        openRuyi release files
License:        MulanPSL-2.0
URL:            https://www.openruyi.cn
Source0:        issue.conf
Source1:        os-release.conf

Provides:       system-release
Provides:       openRuyi-release

%description
This package contains the release files for openRuyi.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_prefix}/lib
install -c -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/issue
echo -e "openRuyi (%{_target_cpu}) - Kernel %%r (%%t)." > %{buildroot}%{_sysconfdir}/issue.net
install -c -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release
touch %{buildroot}%{_sysconfdir}/motd

%files
%defattr(644,root,root,755)
%{_prefix}/lib/os-release
%{_sysconfdir}/os-release
%config(noreplace) %{_sysconfdir}/motd
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net

%changelog
%autochangelog
