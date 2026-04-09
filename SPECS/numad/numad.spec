# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           numad
Version:        0.5
Release:        %autorelease
Summary:        NUMA user daemon
License:        LGPL-2.1-only
URL:            https://pagure.io/numad
#!RemoteAsset:  git+https://pagure.io/numad#aec1497e2b29f57997ae27351ac01abc25026387
#!CreateArchive
Source0:        %{name}-%{version}git.tar.gz

Patch1:         0001-recognize-m-option-correctly.patch
Patch2:         0002-numad_log-fix-buffer-overflow.patch
Patch3:         0003-avoid-array-index-out-of-bounds.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%systemd_requires

%description
Numad is a deamon that monitors NUMA topology and usage and distributes
loads for good locality for the purpose of providing the best performance,
by avoiding unnecessary latency.

%prep
%autosetup -n %{name}-%{version}git -p1

%build
%make_build CFLAGS="$CFLAGS"

%install
%make_install prefix=%{buildroot}/usr
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 numad.service %{buildroot}%{_unitdir}/
install -p -m 644 numad.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%files
%config(noreplace) %{_sysconfdir}/logrotate.d/numad
%{_bindir}/*
%{_unitdir}/numad.service
%doc %{_mandir}/man8/*

%post
%systemd_post numad.service

%preun
%systemd_preun numad.service

%postun
%systemd_postun numad.service

%changelog
%autochangelog
