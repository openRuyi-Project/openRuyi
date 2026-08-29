# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           fio
Version:        3.42
Release:        %autorelease
Summary:        Multithreaded IO generation tool
License:        GPL-2.0-only
URL:            https://fio.readthedocs.io/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/axboe/fio.git
#!RemoteAsset:  sha256:ac126c69fde515a3da3f71817562715df9001e79f2008ed98a17eac340cd3f66
Source0:        http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  libdir=%{_libdir}/fio
BuildOption(install):  INSTALL="install -p"

BuildRequires:  make
BuildRequires:  libaio
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libibverbs)
BuildRequires:  pkgconfig(librdmacm)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)

%description
fio is an I/O tool that will spawn a number of threads or processes doing
a particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%prep -a
sed -e 's,/usr/local/lib/,%{_libdir}/,g' -i os/os-linux.h

%conf
# it's not a regular configure
./configure --disable-optimizations

%files
%doc COPYING REPORTING-BUGS examples MORAL-LICENSE GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
