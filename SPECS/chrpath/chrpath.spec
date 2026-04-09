# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           chrpath
Version:        0.18
Release:        %autorelease
Summary:        Modify rpath of compiled programs
License:        GPL-2.0-or-later
URL:            https://codeberg.org/pere/chrpath
#!RemoteAsset
Source0:        %{url}/archive/release-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%conf -p
autoreconf -fi

%install -a
rm -fr %{buildroot}/usr/doc

%files
%doc AUTHORS README NEWS ChangeLog*
%license COPYING
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

%changelog
%autochangelog
