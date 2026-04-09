# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           createrepo_c
Version:        1.2.1
Release:        %autorelease
Summary:        Creates a common metadata repository
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/createrepo_c
#!RemoteAsset
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Part of https://github.com/rpm-software-management/createrepo_c/pull/438
Patch0:         0001-fix-build-with-cmake-4.patch

BuildOption(conf):  -DWITH_ZCHUNK=ON
BuildOption(conf):  -DWITH_LIBMODULEMD=ON
BuildOption(conf):  -DWITH_DRPM=ON

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libxml2-devel
BuildRequires:  xz
BuildRequires:  bash-completion-devel
BuildRequires:  zchunk
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zck)
BuildRequires:  pkgconfig(modulemd-2.0)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(drpm)

Provides:       createrepo = %{version}-%{release}

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package        libs
Summary:        Library for repodata manipulation

%description    libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package        devel
Summary:        Library for repodata manipulation
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package     -n python-%{name}
Summary:        Python bindings for the createrepo_c library
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       %{name}-libs = %{version}-%{release}

%description -n python-%{name}
Python bindings for the createrepo_c library.

%build -a
# Build docs
%cmake_build -t doc-c

%install -a
ln -sr %{buildroot}%{_bindir}/createrepo_c %{buildroot}%{_bindir}/createrepo
ln -sr %{buildroot}%{_bindir}/mergerepo_c %{buildroot}%{_bindir}/mergerepo
ln -sr %{buildroot}%{_bindir}/modifyrepo_c %{buildroot}%{_bindir}/modifyrepo

%files
%doc README.md
%{_mandir}/man8/createrepo_c.8*
%{_mandir}/man8/mergerepo_c.8*
%{_mandir}/man8/modifyrepo_c.8*
%{_mandir}/man8/sqliterepo_c.8*
%{_datadir}/bash-completion/completions/
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c
%{_bindir}/createrepo
%{_bindir}/mergerepo
%{_bindir}/modifyrepo

%files libs
%license COPYING
%{_libdir}/libcreaterepo_c.so.*

%files devel
%{_libdir}/libcreaterepo_c.so
%{_libdir}/pkgconfig/createrepo_c.pc
%{_includedir}/createrepo_c/

%files -n python-%{name}
%doc examples/python/*
%{python3_sitearch}/createrepo_c/
%{python3_sitearch}/createrepo_c-*-py%{python3_version}.egg-info

%changelog
%autochangelog
