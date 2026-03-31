# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cmake
Version:        4.3.1
Release:        %autorelease
Summary:        Cross-platform make system
License:        BSD and MIT and zlib
URL:            http://www.cmake.org
VCS:            git:https://gitlab.kitware.com/cmake/cmake
#!RemoteAsset:  sha256:0798f4be7a1a406a419ac32db90c2956936fecbf50db3057d7af47d69a2d7edb
Source0:        https://www.cmake.org/files/v4.3/cmake-%{version}.tar.gz
Source1:        macros.cmake
Source2:        macros.buildsystem.cmake
Source3:        cmake.attr
BuildSystem:    autotools

BuildOption(conf):  --no-system-libs

# qt-gui and emacs-lisp features are removed to make cmake usable ASAP
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
# For tests
BuildRequires:  git

Requires:       cmake-data = %{version}-%{release}
Requires:       cmake-rpm-macros = %{version}-%{release}
Requires:       cmake-filesystem = %{version}-%{release}

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.

%package        data
Summary:        Common data-files for cmake
Requires:       cmake = %{version}-%{release}
Requires:       cmake-rpm-macros = %{version}-%{release}
BuildArch:      noarch

%description    data
This package contains common data-files for cmake.

%package        filesystem
Summary:        Directories used by CMake modules

%description    filesystem
This package owns all directories used by CMake modules.

%package        rpm-macros
Summary:        Common RPM macros for cmake
Requires:       rpm
Conflicts:      cmake-data < 3.10.1-2
BuildArch:      noarch

%description    rpm-macros
This package contains common RPM macros for cmake.

%conf
# cmake also need openssl to make FetchContent() usable, but in rpm building
# process we should download all sources in advance
echo "set(CMAKE_USE_OPENSSL OFF)" | cat - CMakeLists.txt > tmpfile && mv tmpfile CMakeLists.txt
./bootstrap --prefix=%{_prefix} --datadir=/share/cmake \
             --docdir=/share/doc/cmake --mandir=/share/man \
             --no-system-libs \
             --parallel=`/usr/bin/getconf _NPROCESSORS_ONLN` \
             --no-system-cppdap \
             --no-system-librhash

%install -a
# install cmake rpm macros
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.cmake
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" -e "s|@@CMAKE_MAJOR_VERSION@@|4|" %{buildroot}%{_rpmmacrodir}/macros.cmake
install -p -m0644 -D %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.buildsystem.cmake

install -p -m0644 -D %{SOURCE3} %{buildroot}%{_fileattrsdir}/cmake.attr

# update cmake rpm macro file timestamp
touch -r %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.cmake
touch -r %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.buildsystem.cmake

# install Copyright and dependencies' Copyright
install -d %{buildroot}%{_libdir}/cmake
find Source Utilities -type f -iname copy\*
cp -p Source/kwsys/Copyright.txt ./Copyright_kwsys
cp -p Utilities/KWIML/Copyright.txt ./Copyright_KWIML
cp -p Utilities/cmlibarchive/COPYING ./COPYING_cmlibarchive
cp -p Utilities/cmliblzma/COPYING ./COPYING_cmliblzma
cp -p Utilities/cmcurl/COPYING ./COPYING_cmcurl
cp -p Utilities/cmlibrhash/COPYING ./COPYING_cmlibrhash
cp -p Utilities/cmzlib/Copyright.txt ./Copyright_cmzlib
cp -p Utilities/cmexpat/COPYING ./COPYING_cmexpat
cp -p Utilities/cmcppdap/LICENSE LICENSE.cppdap
cp -p Utilities/cmcppdap/NOTICE NOTICE.cppdap

# install help files
install -d %{buildroot}%{_docdir}/cmake
cp -pr %{buildroot}%{_datadir}/cmake/Help %{buildroot}%{_docdir}/cmake

# temporary files used to create cmake-filesystem package
find %{buildroot}%{_datadir}/cmake -type d | sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > data_dirs.mf
find %{buildroot}%{_libdir}/cmake -type d | sed -e 's!^%{buildroot}!%%dir "!g' -e 's!$!"!g' > lib_dirs.mf

# remove unnecessary emac lisp files
rm -rf %{buildroot}%{_datadir}/emacs

%check
# Requires network access to run some tests, so exclude them
NO_TEST="CTestTestUpload"
# Exclude CPack component tests
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-default"
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-OnePackPerGroup"
NO_TEST="$NO_TEST|CPackComponentsForAll-RPM-AllInOne"
# curl test may fail
NO_TEST="$NO_TEST|curl"
%ifarch riscv64
# timeout for riscv64
NO_TEST="$NO_TEST|Qt5Autogen.ManySources|Qt5Autogen.MocInclude|Qt5Autogen.MocIncludeSymlink|Qt6Autogen.MocIncludeSymlink"
%endif
bin/ctest %{?_smp_mflags} -V -E "$NO_TEST" --output-on-failure

%files
%doc %dir %{_docdir}/cmake
%license Copyright_* COPYING* LICENSE.rst CONTRIBUTORS.rst
%license LICENSE.cppdap NOTICE.cppdap
%{_bindir}/cmake
%{_bindir}/cpack
%{_bindir}/ctest
%{_libdir}/cmake
%doc %{_docdir}/cmake/*

%files filesystem -f data_dirs.mf -f lib_dirs.mf

%files data
%{_datadir}/cmake
%{_datadir}/aclocal/cmake.m4
%{_datadir}/bash-completion
%{_datadir}/vim/vimfiles/indent/%{name}.vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%exclude %{_datadir}/cmake/Templates/Windows/Windows_TemporaryKey.pfx

%files rpm-macros
%{_fileattrsdir}/cmake.attr
%{_rpmmacrodir}/macros.cmake
%{_rpmmacrodir}/macros.buildsystem.cmake

%changelog
%{?autochangelog}
