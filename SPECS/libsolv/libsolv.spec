# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsolv
Version:        0.7.35
Release:        %autorelease
Summary:        A free package dependency solver using a satisfiability algorithm
License:        BSD-3-Clause
URL:            https://github.com/openSUSE/libsolv
#!RemoteAsset
Source:         https://github.com/openSUSE/libsolv/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# https://github.com/openSUSE/libsolv/pull/602
Patch0:         0001-Python-Provide-dist-info-metadata.patch

BuildOption(conf):  -DFEDORA=1
BuildOption(conf):  -DENABLE_COMPLEX_DEPS=ON
BuildOption(conf):  -DENABLE_RPMDB=ON
BuildOption(conf):  -DENABLE_RPMDB_BYRPMHEADER=ON
BuildOption(conf):  -DENABLE_RPMDB_LIBRPM=ON
BuildOption(conf):  -DENABLE_RPMPKG_LIBRPM=ON
BuildOption(conf):  -DENABLE_RPMMD=ON
BuildOption(conf):  -DUSE_VENDORDIRS=ON
BuildOption(conf):  -DWITH_LIBXML2=ON
BuildOption(conf):  -DENABLE_LZMA_COMPRESSION=ON
BuildOption(conf):  -DENABLE_BZIP2_COMPRESSION=ON
BuildOption(conf):  -DENABLE_ZSTD_COMPRESSION=ON
BuildOption(conf):  -DENABLE_ZCHUNK_COMPRESSION=ON
BuildOption(conf):  -DENABLE_CONDA=ON
BuildOption(conf):  -DENABLE_SUSEREPO=ON
BuildOption(conf):  -DENABLE_COMPS=ON
BuildOption(conf):  -DENABLE_PERL=ON
BuildOption(conf):  -DENABLE_RUBY=OFF
BuildOption(conf):  -DENABLE_PYTHON=ON
BuildOption(conf):  -DENABLE_APPDATA=OFF
BuildOption(conf):  -DENABLE_HELIXREPO=ON
BuildOption(conf):  -DENABLE_DEBIAN=OFF
BuildOption(conf):  -DENABLE_ARCHREPO=OFF

BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zck)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  swig
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  perl-macros

%description
libsolv is a free package dependency solver using a satisfiability algorithm.
It uses a dictionary approach to store and retrieve package and dependency
information, and satisfiability for resolving dependencies. This package
contains the core C/C++ library and command-line tools.

%package        devel
Summary:        Development files for libsolv
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(rpm)

%description    devel
Development files for the libsolv library.

%package     -n python-solv
Summary:        Python bindings for the %{name} library
Provides:       python3-solv
%{?python_provide:%python_provide python3-solv}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-solv
Python bindings for the %{name} library.

%files
%license LICENSE*
%{_libdir}/lib*.so.*
%{_bindir}/deltainfoxml2solv
%{_bindir}/dumpsolv
%{_bindir}/installcheck
%{_bindir}/mergesolv
%{_bindir}/repomdxml2solv
%{_bindir}/rpmdb2solv
%{_bindir}/rpmmd2solv
%{_bindir}/rpms2solv
%{_bindir}/testsolv
%{_bindir}/comps2solv
%{_bindir}/conda2solv
%{_bindir}/susetags2solv
%{_bindir}/updateinfoxml2solv
%{_bindir}/repo2solv
%{_bindir}/solv
%{_bindir}/helix2solv
%{_mandir}/man1/*
%{_mandir}/man3/lib*.3*
%{perl_vendorarch}/solv.pm
%{perl_vendorarch}/solv.so

%files devel
%{_libdir}/lib*.so
%{_includedir}/solv/
%{_libdir}/pkgconfig/libsolv.pc
%{_libdir}/pkgconfig/libsolvext.pc
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake

%files -n python-solv
%{python3_sitearch}/_solv.so
%{python3_sitearch}/solv.py
%{python3_sitearch}/solv-%{version}.dist-info/

%changelog
%{?autochangelog}
