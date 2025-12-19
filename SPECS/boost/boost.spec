# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: haswell <haswell@haswells-MacBook-Air.local>
#
# SPDX-License-Identifier: MulanPSL-2.0

# works strangely if implemented with:
# %define version_enc %(echo "%{version}"|tr \. _)
%define version_enc 1_89_0

Name:           boost
Summary:        The free peer-reviewed portable C++ source libraries
Version:        1.89.0
Release:        %autorelease
License:        BSL-1.0 AND MIT AND Python-2.0.1
URL:            http://www.boost.org
#!RemoteAsset
Source0:        https://archives.boost.io/release/%{version}/source/%{name}_%{version_enc}.tar.gz
Source1:        b2.1
# Adjusting build optimization flags for rpm build
Patch0:         0001-boost-1.81.0-build-optflags.patch
# Remove rpath from builds
Patch1:         0002-boost-1.78.0-no-rpath.patch
# Modify b2 build flags
Patch2:         0003-boost-1.78.0-b2-build-flags.patch

# to make this package usable ASAP, boost-mpi, boost-numpy
# boost-mpich is not built
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel
BuildRequires:  python3-devel
BuildRequires:  icu4c-devel
BuildRequires:  bison
BuildRequires:  zstd-devel
# use autotools to reduce abundant % procedures
# boost uses its own build system called b2, however
BuildSystem:    autotools

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been included in the C++ 2011 standard and
others have been proposed to the C++ Standards Committee for inclusion
in future standards.)

%package build
Summary:        Cross platform build system for C++ projects

%description build
Boost.Build is an easy way to build C++ projects, everywhere. You name
your pieces of executable and libraries and list their sources.  Boost.Build
takes care about compiling your sources with the right options,
creating static and shared libraries, making pieces of executable, and other
chores -- whether you are using GCC, MSVC, or a dozen more supported
C++ compilers -- on Windows, OSX, Linux and commercial UNIX systems.

%package devel
Summary:        The Boost C++ headers and shared development libraries
Requires:       %{name}
Requires:       icu4c-devel

%description devel
Headers and shared object symbolic links for the Boost C++ libraries.

%conf
./bootstrap.sh --with-icu
%set_build_flags
cat > ./tools/build/src/user-config.jam << EOF
import os ;
# use build system flags
local CXXFLAGS = [ os.environ CXXFLAGS ] ;
local LDFLAGS = [ os.environ LDFLAGS ] ;
using gcc : : : <compileflags>%(CXXFLAGS) <linkflags>%(LDFLAGS) ;
# help build system to find python3
using python : %{python3_version} : /usr/bin/python3 : /usr/include/python%{python3_version} : : : ;
EOF

%build
./b2 -d+2 -q %{?_smp_mflags} \
    --without-mpi --without-graph_parallel --build-dir=out \
    variant=release threading=multi debug-symbols=on pch=off \
    python=%{python3_version} \
    stage
# build Boost.build
pushd tools/build
./bootstrap.sh
popd

%install
./b2 -d+2 -q %{?_smp_mflags} \
    --without-mpi --without-graph_parallel --build-dir=out \
    --prefix=%{buildroot}%{_prefix} \
    --libdir=%{buildroot}%{_libdir} \
    variant=release threading=multi debug-symbols=on pch=off \
    python=%{python3_version} \
    install

# install Boost.build
pushd tools/build
./b2 --prefix=%{buildroot}%{_prefix} --bindir=%{buildroot}%{_bindir} install

# rename b2 to boost-build while keeping a symlink
mv %{buildroot}%{_datadir}/b2 %{buildroot}%{_datadir}/boost-build
pushd %{buildroot}%{_datadir}
ln -s ./boost-build b2
popd
popd

# install b2 man pages
install -p -m 644 %{SOURCE1} -D %{buildroot}%{_mandir}/man1/b2.1
mkdir -p %{buildroot}%{_docdir}/boost

# cleanup unnecessary files
rm -rf %{buildroot}%{_libdir}/lib*.a
rm -rf %{buildroot}%{_datadir}/boost_predef

# No check
%check

%files
%license LICENSE_1_0.txt
%{_libdir}/lib*.so*

%files build
%license LICENSE_1_0.txt
%{_datadir}/%{name}-build/
%{_datadir}/b2
%{_bindir}/b2
%{_mandir}/man1/b2.1*

%files devel
%license LICENSE_1_0.txt
%{_includedir}/%{name}
%{_libdir}/cmake

%changelog
%{?autochangelog}
