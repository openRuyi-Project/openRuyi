# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libidn2
Version:        2.3.8
Release:        %autorelease
Summary:        Support for Internationalized Domain Names (IDN) based on IDNA2008
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/libidn/#libidn2
VCS:            git:https://gitlab.com/libidn/libidn2
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz.sig
#!RemoteAsset
Source2:        https://josefsson.org/key-20190320.txt#/%{name}.keyring
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig

%description
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%package        devel
Summary:        Include Files and Libraries mandatory for Development
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%install -a
rm -rf %{buildroot}/%{_datadir}/gtk-doc/

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING*
%{_libdir}/libidn2.so.*
%doc AUTHORS ChangeLog NEWS README.md
%{_infodir}/libidn*
%{_bindir}/idn2
%{_mandir}/man1/idn2.1%{?ext_man}

%files devel
%license COPYING*
%{_libdir}/libidn2.so
%{_libdir}/pkgconfig/libidn2.pc
%{_includedir}/*.h
%{_mandir}/man3/*

%changelog
%autochangelog
