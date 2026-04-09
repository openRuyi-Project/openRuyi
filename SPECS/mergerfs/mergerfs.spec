# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mergerfs
Version:        2.41.1
Release:        %{autorelease}
Summary:        A FUSE union filesystem
License:        MIT
URL:            https://github.com/trapexit/mergerfs
#!RemoteAsset
Source0:        https://github.com/trapexit/mergerfs/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-no_chown_during_install.patch

BuildOption(build):  LIBDIR=%{_libdir}
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  SBINDIR=%{_sbindir}
BuildOption(install):  LIBDIR=%{_libdir}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  libtool

%description
mergerfs is similar to mhddfs, unionfs, and aufs. Like mhddfs in that it also
uses FUSE. Like aufs in that it provides multiple policies for how to handle
behavior.

%conf
# do not ./configure

%check
# do not make check

%files
%doc README.md
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*.1*
%{_libdir}/mergerfs

%changelog
%autochangelog
