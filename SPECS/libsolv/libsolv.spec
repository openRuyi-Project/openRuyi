# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:                  libsolv
Version:               0.7.35
Release:               %autorelease
Summary:               A free package dependency solver using a satisfiability algorithm
License:               BSD-3-Clause
URL:                   https://github.com/openSUSE/libsolv
#!RemoteAsset
Source:                https://github.com/openSUSE/libsolv/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:           cmake

BuildOption(conf):           -DFEDORA=1
BuildOption(conf):           -DENABLE_COMPLEX_DEPS=ON
BuildOption(conf):           -DENABLE_RPMDB=ON
BuildOption(conf):           -DENABLE_RPMDB_BYRPMHEADER=ON
BuildOption(conf):           -DENABLE_RPMDB_LIBRPM=ON
BuildOption(conf):           -DENABLE_RPMPKG_LIBRPM=ON
BuildOption(conf):           -DENABLE_RPMMD=ON
BuildOption(conf):           -DUSE_VENDORDIRS=ON
BuildOption(conf):           -DWITH_LIBXML2=ON
BuildOption(conf):           -DENABLE_LZMA_COMPRESSION=ON
BuildOption(conf):           -DENABLE_BZIP2_COMPRESSION=ON
BuildOption(conf):           -DENABLE_ZSTD_COMPRESSION=ON
BuildOption(conf):           -DENABLE_ZCHUNK_COMPRESSION=ON
BuildOption(conf):           -DENABLE_CONDA=ON
BuildOption(conf):           -DENABLE_SUSEREPO=ON
BuildOption(conf):           -DENABLE_COMPS=ON
BuildOption(conf):           -DENABLE_PERL=ON          # Requires: swig, perl-devel
BuildOption(conf):           -DENABLE_RUBY=OFF         # Requires: swig, ruby-devel
BuildOption(conf):           -DENABLE_PYTHON=ON        # Requires: swig, python3-devel
BuildOption(conf):           -DENABLE_APPDATA=OFF      # Requires: pkgconfig(appstream-glib)
BuildOption(conf):           -DENABLE_HELIXREPO=ON     # Requires: pkgconfig(sqlite3)
BuildOption(conf):           -DENABLE_DEBIAN=OFF
BuildOption(conf):           -DENABLE_ARCHREPO=OFF


# BuildRequires:       swig perl-devel ruby-devel python3-devel
# BuildRequires:       pkgconfig(appstream-glib) pkgconfig(sqlite3)

BuildRequires:         pkgconfig(openssl) pkgconfig(yaml-0.1)
BuildRequires:         libzstd-devel
BuildRequires:         pkgconfig(zck)
BuildRequires:         cmake gcc-c++ ninja pkgconfig(rpm) zlib-devel
BuildRequires:         libxml2-devel xz-devel bzip2-devel
BuildRequires:         swig perl-devel python3-devel pkgconfig(sqlite3) perl-macros

%description
libsolv is a free package dependency solver using a satisfiability algorithm.
It uses a dictionary approach to store and retrieve package and dependency
information, and satisfiability for resolving dependencies. This package
contains the core C/C++ library and command-line tools.

%package               devel
Summary:               Development files for libsolv
Requires:              %{name} = %{version}
Requires:              rpm-devel

%description devel
Development files for the libsolv library.

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
%{_mandir}/man1/*
%{_mandir}/man3/lib*.3*
%{perl_vendorarch}/solv.pm
%{perl_vendorarch}/solv.so

%files devel
%{_libdir}/lib*.so
%{_includedir}/solv/
%{_libdir}/pkgconfig/lib*.pc
%dir %{_datadir}/cmake/Modules/
%{_datadir}/cmake/Modules/FindLibSolv.cmake

%changelog
%{?autochangelog}
