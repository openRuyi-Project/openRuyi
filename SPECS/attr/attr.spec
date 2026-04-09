# SPDX-FileCopyrightText: (C) 2025-2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025-2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           attr
Version:        2.5.2
Release:        %autorelease
Summary:        Commands for Manipulating Extended Attributes
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://savannah.nongnu.org/projects/attr/
VCS:            git:https://git.savannah.nongnu.org/git/attr.git
#!RemoteAsset
Source:         https://download-mirror.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz
BuildSystem:    autotools

Patch1:         0001-bypass-wrong-output-when-enabled-selinux.patch
Patch2:         0002-dont-skip-security.evm-when-copy-xattr.patch

BuildOption(conf): --disable-static
BuildOption(conf): --disable-silent-rules

BuildRequires:  pkgconfig
BuildRequires:  perl

%description
A set of tools for manipulating extended attributes on file system
objects, in particular getfattr(1) and setfattr(1). An attr(1) command
is also provided, which is largely compatible with the SGI IRIX tool of
the same name.

%package        devel
Summary:        Development files for attr
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
This package contains the libraries and header files needed to develop
programs which make use of extended attributes. For Linux programs, the
documented system call API is the recommended interface, but an SGI
IRIX compatibility interface is also provided.

%check
%make_build check

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license doc/COPYING*
%doc doc/CHANGES
%{_libdir}/libattr.so.1*
%exclude %{_docdir}/%{name}/CHANGES
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/COPYING.LGPL
%{_mandir}/man1/*.1*
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr

%files devel
%license doc/COPYING*
%config %{_sysconfdir}/xattr.conf
%{_includedir}/attr/
%{_libdir}/pkgconfig/libattr.pc
%{_libdir}/libattr.so
%{_mandir}/man3/*.3*

%changelog
%autochangelog
