# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define lname  libattr1
Name:           attr
Version:        2.5.2
Release:        %autorelease
Summary:        Commands for Manipulating Extended Attributes
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://savannah.nongnu.org/projects/attr/
#!RemoteAsset
Source:         https://download-mirror.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz

Patch1:         0001-bypass-wrong-output-when-enabled-selinux.patch
Patch2:         0002-dont-skip-security.evm-when-copy-xattr.patch
BuildRequires:  pkgconfig
BuildRequires:  perl
Conflicts:      xfsdump < 2.0.0
BuildSystem:    autotools
BuildOption(conf): --enable-static
BuildOption(conf): --disable-silent-rules

%description
A set of tools for manipulating extended attributes on file system
objects, in particular getfattr(1) and setfattr(1). An attr(1) command
is also provided, which is largely compatible with the SGI IRIX tool of
the same name.

%package -n %{lname}
Summary:        A dynamic library for filesystem extended attribute support
Obsoletes:      libattr < %{version}-%{release}
Provides:       libattr = %{version}-%{release}

%description -n %{lname}
This package contains the libattr.so dynamic library, which contains
the extended attribute library functions.

%package -n libattr-devel
Summary:        Header files for libattr
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Provides:       attr-devel = %{version}-%{release}
Obsoletes:      attr-devel < %{version}-%{release}

%description -n libattr-devel
This package contains the libraries and header files needed to develop
programs which make use of extended attributes. For Linux programs, the
documented system call API is the recommended interface, but an SGI
IRIX compatibility interface is also provided.

%package -n libattr-devel-static
Summary:        Static libraries for libattr development
Requires:       libattr-devel = %{version}
Provides:       libattr-devel:%{_libdir}/libattr.a

%description -n libattr-devel-static
This package contains the static library of libattr which is needed for
staticallly linking to programs that make use of extended attributes.

%check
%make_build check

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license doc/COPYING*
%doc doc/CHANGES
%exclude %{_docdir}/%{name}/CHANGES
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/COPYING.LGPL
%{_mandir}/man1/*.1*
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr

%files -n %{lname}
%license doc/COPYING*
%{_libdir}/libattr.so.1*
%config %{_sysconfdir}/xattr.conf

%files -n libattr-devel
%license doc/COPYING*
%{_includedir}/attr/
%{_libdir}/pkgconfig/libattr.pc
%{_libdir}/libattr.so
%{_mandir}/man3/*.3*

%files -n libattr-devel-static
%license doc/COPYING*
%{_libdir}/libattr.a

%changelog
%{?autochangelog}
