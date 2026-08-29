# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libthai
Version:        0.1.29
Release:        %autorelease
Summary:        Thai language support routines
License:        LGPL-2.1-or-later
URL:            https://linux.thai.net/plone/TLWG/libthai/
VCS:            git:https://github.com/tlwg/libthai
#!RemoteAsset:  sha256:fc80cc7dcb50e11302b417cebd24f2d30a8b987292e77e003267b9100d0f4bcd
Source0:        http://linux.thai.net/pub/thailinux/software/libthai/libthai-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(datrie-0.2)

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package        devel
Summary:        Thai language support routines
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libthai-devel package includes the header files and developer docs
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%files
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/lib*.so.*
%{_datadir}/libthai

%files devel
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libthai.pc

%changelog
%autochangelog
