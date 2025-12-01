# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           acl
Summary:        Commands for Manipulating POSIX Access Control Lists
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Version:        2.3.2
Release:        %autorelease
URL:            https://savannah.nongnu.org/projects/acl
#!RemoteAsset
Source:         https://download.savannah.nongnu.org/releases/acl/acl-%{version}.tar.xz
#!RemoteAsset
Source1:        https://download.savannah.nongnu.org/releases/acl/acl-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  pkg-config

BuildOption(conf): --disable-static --docdir=%_defaultdocdir/%name

%description
getfacl and setfacl commands for retrieving and setting POSIX access
control lists.

%package        devel
Summary:        Header files for the POSIX ACL library
Requires:       %name = %version
Requires:       glibc-devel
Provides:       acl-devel = %version
Obsoletes:      acl-devel < %version

%description    devel
This package contains all necessary include files and libraries needed
to develop applications that require libacl.

%conf -p
autoreconf -fiv

%install -p
rm -rvf %buildroot/%_defaultdocdir/%name

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license doc/COPYING
%doc doc/extensions.txt doc/libacl.txt doc/CHANGES
%{_docdir}/acl
%license doc/COPYING.LGPL
%_libdir/libacl.so.1*
%_bindir/chacl
%_bindir/getfacl
%_bindir/setfacl
%_mandir/man1/*.1*
%_mandir/man5/*.5*

%files devel
%_includedir/acl/
%_includedir/sys/acl.h
%_libdir/libacl.so
%_mandir/man3/*.3*
%_libdir/pkgconfig/libacl.pc

%changelog
%{?autochangelog}
