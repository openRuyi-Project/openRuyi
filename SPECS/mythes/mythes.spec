# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mythes
Version:        1.2.6
Release:        %autorelease
Summary:        Thesaurus lookup library
License:        BSD-Mark-Modifications
URL:            https://github.com/hunspell/mythes
#!RemoteAsset:  sha256:97bd2ba5738aebdba1bc31f30f1be42f1404386c94105ad5990d839a1311c8a5
Source0:        https://github.com/hunspell/mythes/releases/download/v%{version}/mythes-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(hunspell)

%description
MyThes retrieves synonyms and definitions from indexed thesaurus files.
The th_gen_idx.pl utility creates indexes from dictionary data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/th_gen_idx.pl
%{_libdir}/libmythes-1.2.so.*

%files devel
%{_includedir}/mythes.hxx
%{_libdir}/libmythes-1.2.so
%{_libdir}/pkgconfig/mythes.pc

%changelog
%autochangelog
