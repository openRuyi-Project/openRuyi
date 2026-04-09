# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           scdoc
Version:        1.11.3
Release:        %autorelease
Summary:        Tool for generating roff manual pages
License:        MIT
URL:            https://git.sr.ht/~sircmpwn/scdoc
#!RemoteAsset
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  PREFIX=%{_prefix}
BuildOption(install):  PREFIX=%{_prefix} PCDIR=%{_datadir}/pkgconfig %{?_smp_mflags}

BuildRequires:  make
BuildRequires:  sed
BuildRequires:  glibc

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep -a
# Disable static linking
sed -i '/-static/d' Makefile

%conf
# No configure

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
# scdoc is a development tool so no devel
%{_datarootdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
