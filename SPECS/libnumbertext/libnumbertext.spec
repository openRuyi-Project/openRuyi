# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnumbertext
Version:        1.0.11
Release:        %autorelease
Summary:        Spell out numbers and currency amounts in words
License:        BSD-3-Clause AND LGPL-3.0-or-later
URL:            https://github.com/Numbertext/libnumbertext
#!RemoteAsset:  sha256:5dcb4db3b2340f81f601ce86d8d76b69e34d70f84f804192c901e4b7f84d5fb0
Source0:        https://github.com/Numbertext/libnumbertext/releases/download/%{version}/libnumbertext-%{version}.tar.xz
# The Croatian and Serbian Soros rules use LGPL-3.0-or-later, which incorporates GPL-3.0.
Source1:        lgpl-3.0.txt
Source2:        gpl-3.0.txt
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  make

%description
libnumbertext applies language-specific spelling rules to numeric
values and currency amounts. The spellout utility exposes the same rules
on the command line.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
cp -p %{SOURCE1} COPYING.LESSER
cp -p %{SOURCE2} COPYING.GPL3

%files
%doc AUTHORS README.md
%license COPYING COPYING.LESSER COPYING.GPL3
%{_bindir}/spellout
%{_datadir}/libnumbertext/
%{_libdir}/libnumbertext-1.0.so.*

%files devel
%{_includedir}/libnumbertext/
%{_libdir}/libnumbertext-1.0.so
%{_libdir}/pkgconfig/libnumbertext.pc

%changelog
%autochangelog
