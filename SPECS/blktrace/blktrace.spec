# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       f9bd00dfbd67ce62ca6df6f55d6275b523cd0b39
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           blktrace
Version:        1.3.0+git20251126.%{shortcommit}
Release:        %autorelease
Summary:        Block IO tracer
License:        GPL-2.0-or-later
URL:            https://brick.kernel.dk/snaps
#!RemoteAsset
Source0:        https://brick.kernel.dk/snaps/%{name}-git-20251211002502.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags} %{?build_ldflags}"
BuildOption(build):  all
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  mandir=%{_mandir}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libaio)
# BuildRequires:  librsvg-devel
BuildRequires:  pkgconfig(python3)

# Requires:       librsvg-tools

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations up to user space. This is
valuable for diagnosing and fixing performance or application problems
relating to block layer io.

# no configure script
%conf

# no tests.
%check

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%changelog
%autochangelog
