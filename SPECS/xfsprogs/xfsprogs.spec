# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xfsprogs
Version:        6.16.0
Release:        %autorelease
Summary:        Administration and debugging tools for the XFS file system
License:        GPL-1.0-or-later AND LGPL-2.1-or-later
URL:            https://xfs.wiki.kernel.org
#!RemoteAsset
Source:         http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf): --enable-editline=yes
BuildOption(conf): --enable-blkid=yes
BuildOption(conf): --enable-lto=no

BuildOption(install): DIST_ROOT=%{buildroot}
BuildOption(install): PKG_ROOT_SBIN_DIR=%{_sbindir}
BuildOption(install): PKG_ROOT_LIB_DIR=%{_libdir}
BuildOption(install): install-dev

BuildRequires:  libtool attr-devel gcc gettext-devel acl-devel inih-devel userspace-rcu-devel
BuildRequires:  libedit-devel util-linux-devel
Requires:       libedit
Requires:       python3

%description
xfsprogs are the userspace utilities that manage XFS filesystems.
This package also includes the experimental xfs_scrub utility.

%package        devel
Summary:        Development files for the XFS filesystem library
Requires:       xfsprogs = %{version}
Requires:       util-linux-devel

%description    devel
This package contains the header files for developing applications
that use the XFS filesystem libraries.


%install -a
# remove unused files
find %{buildroot} -type f \( -name "*.a" \) -delete -print
rm -rf %{buildroot}%{_datadir}/doc/xfsprogs/

# no check target
%check

%files
%doc doc/CHANGES README
%{_libdir}/lib*.so.*
%{_sbindir}/*
%{_datadir}/xfsprogs/
%{_datadir}/locale/*/LC_MESSAGES/xfsprogs.mo

%files devel
%dir %{_includedir}/xfs
%{_includedir}/xfs/*.h
%{_libdir}/lib*.so
%{_mandir}/man*/*

%changelog
%{?autochangelog}
