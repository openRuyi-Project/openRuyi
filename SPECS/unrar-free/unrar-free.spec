# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           unrar-free
Version:        0.3.3
Release:        %autorelease
Summary:        Free software version of the non-free unrar utility
License:        GPL-2.0-or-later
URL:            https://gitlab.com/bgermann/unrar-free
#!RemoteAsset
Source:         https://gitlab.com/bgermann/unrar-free/-/archive/%{version}/unrar-free-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  libtool

%description
unrar-free is a free software version of the non-free unrar utility. This
program is a simple command-line front-end to libarchive, and can list and
extract RAR archives and other formats supported by libarchive.

%package     -n unrar
Summary:        Wrapper package for unrar-free
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n unrar
This package provides a compatibility symlink to use unrar-free as /usr/bin/unrar.

%conf -p
autoreconf -i

%install -a
ln -s unrar-free %{buildroot}%{_bindir}/unrar
ln -s unrar-free.1 %{buildroot}%{_mandir}/man1/unrar.1

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO misc/tarar.pike
%{_bindir}/unrar-free
%{_mandir}/man1/unrar-free.1*

%files -n unrar
%{_bindir}/unrar
%{_mandir}/man1/unrar.1*

%changelog
%autochangelog
