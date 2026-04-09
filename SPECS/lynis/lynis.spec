# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: BH1SCW <kongfanjun@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lynis
Version:        3.1.6
Release:        %autorelease
Summary:        Security and system auditing tool
License:        GPL-3.0-only
URL:            https://cisofy.com/lynis/
VCS:            git:https://github.com/CISOfy/lynis
#!RemoteAsset
Source0:        https://cisofy.com/files/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  procps-ng

Requires:       audit
Requires:       e2fsprogs
Requires:       kmod

%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it
performs many individual security control checks. It determines the hardening
state of the machine, detects security issues and provides suggestions to
improve the security defense of the system.

%prep
%autosetup -n %{name}

%build
# Empty build.

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -p default.prf %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
install -p lynis %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -p lynis.8 %{buildroot}%{_mandir}/man8

mkdir -p  %{buildroot}%{_datadir}/%{name}/include/
# Forced by upstream. Otherwise these scripts can't be executed.
install -p include/* %{buildroot}%{_datadir}/%{name}/include/
chmod 644 %{buildroot}%{_datadir}/%{name}/include/*

mkdir -p  %{buildroot}%{_datadir}/%{name}/plugins/
install -p plugins/* %{buildroot}%{_datadir}/%{name}/plugins/

cp -pR db/ %{buildroot}%{_datadir}/%{name}/

mkdir -p %{buildroot}%{bash_completions_dir}
install -p extras/bash_completion.d/lynis %{buildroot}%{bash_completions_dir}/

mkdir -p %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/lynis.log
touch %{buildroot}%{_localstatedir}/log/lynis-report.dat

%check
#./lynis audit system --quick --pentest

%files
%doc CHANGELOG* CONTRIBUTORS* FAQ* README*
%doc extras/systemd/
%license LICENSE
%{_bindir}/lynis
%{bash_completions_dir}/*
%{_datadir}/lynis/
%{_mandir}/man8/lynis.8*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.prf
%ghost %{_localstatedir}/log/lynis.log
%ghost %{_localstatedir}/log/lynis-report.dat

%changelog
%autochangelog
