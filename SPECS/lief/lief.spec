# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lief
Version:        1.0.0
Release:        %autorelease
Summary:        Library to inspect and modify executable formats
License:        Apache-2.0 AND BSL-1.0 AND CC0-1.0 AND MIT
URL:            https://lief.re/
VCS:            git:https://github.com/lief-project/LIEF
#!RemoteAsset:  sha256:2cf412695ff739d82e129db441e5c2025f3bb4873a3d3a1d3dd4cf300b682abd
Source0:        https://github.com/lief-project/LIEF/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DLIEF_SO_VERSION:BOOL=ON
BuildOption(conf):  -DLIEF_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DLIEF_TESTS:BOOL=ON
BuildOption(conf):  -DLIEF_USE_MELKOR:BOOL=OFF

BuildRequires:  cmake >= 3.24
BuildRequires:  gcc-c++
BuildRequires:  cmake(Catch2) >= 3.12.0
BuildRequires:  ninja

%description
LIEF reads and modifies ELF, PE, Mach-O, COFF and Android executable formats.
It provides C and C++ interfaces for binary analysis and resource injection.

%package        devel
Summary:        Development files for LIEF
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and build metadata for applications that use LIEF.

%prep -a
# Use the configured library directory; https://github.com/lief-project/LIEF/blob/1.0.0/cmake/LIEF.pc.in.
sed -i 's|${prefix}/lib|@CMAKE_INSTALL_FULL_LIBDIR@|' cmake/LIEF.pc.in
sed -i 's/FetchContent_MakeAvailable(Catch2)/find_package(Catch2 3.12.0 REQUIRED)/' tests/unittests/CMakeLists.txt

%install -a
install -Dpm0644 %{_vpath_builddir}/_deps/lief_utfcpp-src/LICENSE bundled-licenses/utfcpp
install -Dpm0644 %{_vpath_builddir}/_deps/lief_expected-src/COPYING bundled-licenses/expected
install -Dpm0644 %{_vpath_builddir}/_deps/lief_spdlog_project-src/LICENSE bundled-licenses/spdlog

%check
# Run tests without the separate binary corpus; https://github.com/lief-project/LIEF/blob/1.0.0/tests/dl_samples.py.
%{_vpath_builddir}/tests/unittests/unittests '~[elf]~[pe]~[binarystream]~[oat]'

%files
%doc README.md
%license LICENSE bundled-licenses/
%{_libdir}/libLIEF.so.1
%{_libdir}/libLIEF.so.1.*

%files devel
%{_includedir}/LIEF/
%{_libdir}/libLIEF.so
%{_libdir}/cmake/LIEF/
%{_libdir}/pkgconfig/LIEF.pc

%changelog
%autochangelog
